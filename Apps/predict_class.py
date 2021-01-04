# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow import keras
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
import pickle 
from preprocess import text_preprocess
import numpy as np


vectroizer=pickle.load(open('../Models/Classify/vectorizer_classify.pickle', "rb"))
ws = WS("../data")


def class_prediction(txt):
    class_dict={0:'無問題',1:'閃退問題',2:'播放問題',3:'帳號問題',4:'其他問題'}
    processed_data=text_preprocess(txt)
    if len(processed_data)==0:
        # raise Exception('Not Chinese or empty value')
        return('not Chinese')
    else:
        
        cuttext=[]
        for j in ws([processed_data]):
            cuttext.append(' '.join(j))
            
            
        text_to_tensor= vectroizer.transform(cuttext).todense()
        reload_model=keras.models.load_model('../Models/Classify/Trained_classify_model',compile=False)
        prediction=reload_model.predict(text_to_tensor)
        pred_list=prediction.tolist()[0]
        return(class_dict[pred_list.index(max(pred_list))])



if __name__=='__main__':
    test_data=['爛到爆了一直閃退','到底什麼時候要修好 聽到一半一直跳出去','好用 支持到爆','沒有要訂了還一直收錢','還行','帳號密碼都打對還一直登不進去']
    for i in range(len(test_data)):
        prediction=class_prediction(test_data[i])

        print('The class of '+test_data[i]+' is '+prediction)
        
