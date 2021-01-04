#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 03:08:26 2020

@author: cheer
"""
from predict_sentiment import sentiment_prediction
from predict_class import class_prediction
import pandas as pd


def main_prediction(txt):
    
    predict_class=class_prediction(txt)
    predict_sentiment=sentiment_prediction(txt)
    
    return([predict_class,predict_sentiment])

def fetch_comments(comment_file):
    df=pd.read_csv(comment_file)
    
    return(df)
    
    

if __name__=='__main__':
    

    test_data=fetch_comments('KKBOX_comments.csv')    
    # for i in range(len(test_data)):
    #     final_prediction=main_prediction(test_data[i])
    #     print('Review: '+test_data[i])
    #     print('問題分類為： '+final_prediction[0])
    #     print('情緒分數為: '+str(final_prediction[1]))
    print(test_data[0])
    
    
