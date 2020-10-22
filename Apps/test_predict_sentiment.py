#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 05:49:43 2020

@author: cheer
"""
import unittest
from predict_sentiment import sentiment_prediction

class TestPrepredict(unittest.TestCase):
    

    def test_prediction_in_value_bound(self):
        
        #check if value in bound
        prediction_functional=sentiment_prediction('腾讯收购搜狗的交易尘埃落定')
        self.assertEqual(prediction_functional>-1 or prediction_functional<1,True)
        
    def test_predict_reliability(self):
        #reliability test
        prediction_reliable=sentiment_prediction('爛透了一直閃退根本沒辦法用')
        self.assertEqual(prediction_reliable<-0.5,True)   
        
    def test_empty_input(self):
        with self.assertRaises(Exception) as context:
            sentiment_prediction('aaaaa')
        self.assertTrue('Not Chinese or empty value' in str(context.exception))        
    

if __name__=='__main__':
    unittest.main()