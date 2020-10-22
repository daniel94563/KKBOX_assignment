#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 03:08:26 2020

@author: cheer
"""
from predict_sentiment import sentiment_prediction
from predict_class import class_prediction


def main_prediction(txt):
    
    predict_class=class_prediction(txt)
    predict_sentiment=sentiment_prediction(txt)
    
    return([predict_class,predict_sentiment])


if __name__=='__main__':
    
    test_data=['爛到爆了一直閃退','到底什麼時候要修好 聽到一半一直跳出去','好用 支持到爆','沒有要訂了還一直收錢','還行','帳號密碼都打對還不能登進去 搞屁啊']
    
    for i in range(len(test_data)):
        final_prediction=main_prediction(test_data[i])
        print('Review: '+test_data[i])
        print('問題分類為： '+final_prediction[0])
        print('情緒分數為: '+str(final_prediction[1]))
    
    
    