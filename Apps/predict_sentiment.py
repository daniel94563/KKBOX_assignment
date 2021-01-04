# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow import keras
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
import pickle 
from preprocess import text_preprocess


vectroizer=pickle.load(open('../Models/Sentiment/vectorizer_sentiment_model.pickle', "rb"))
ws = WS("../data")


def sentiment_prediction(txt):
    processed_data=text_preprocess(txt)
    if len(processed_data)==0:
        return('No comments!')
    else:
        
        cuttext=[]
        for j in ws([processed_data]):
            cuttext.append(' '.join(j))
            
            
        text_to_tensor= vectroizer.transform(cuttext).todense()
        reload_model=keras.models.load_model('../Models/Sentiment/Trained_sentiment_model',compile=False)
        return(reload_model.predict(text_to_tensor)[0][0])



if __name__=='__main__':
    test_data=['爛到爆了一直閃退','到底什麼時候要修好 聽到一半一直跳出去','好用 支持到爆','沒有要訂了還一直收錢','還行','難用']
    for i in range(len(test_data)):
        print('Sentiment score for '+test_data[i]+' is '+str(sentiment_prediction(test_data[i])))
        
