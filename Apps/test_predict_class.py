#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 05:49:43 2020

@author: cheer
"""
import unittest
from predict_class import class_prediction

class TestPrepredict(unittest.TestCase):
    

    def test_prediction_w_right_class(self):
        
        #check if the class is right
        prediction_class_one=class_prediction('爛到爆了一直閃退')
        self.assertEqual(prediction_class_one,'閃退問題')  
        
        prediction_class_two=class_prediction('完全沒有辦法播歌！')
        self.assertEqual(prediction_class_two,'播放問題')
        
        prediction_class_three=class_prediction('登入一直登不進去 重新註冊也不能按')
        self.assertEqual(prediction_class_three,'帳號問題')
        
        prediction_class_four=class_prediction('已經沒有在用了還一直扣我的錢')
        self.assertEqual(prediction_class_four,'其他問題')
        
        prediction_class_zero=class_prediction('一起聽的功能真的很棒')
        self.assertEqual(prediction_class_zero,'無問題')
        
    def test_predict_output_type(self):
        #type test
        prediction_type=class_prediction('爛透了一直閃退根本沒辦法用')
        self.assertEqual(type(prediction_type)==str,True)   
        
    def test_empty_input(self):
        with self.assertRaises(Exception) as context:
            class_prediction('aaaaa')
        self.assertTrue('Not Chinese or empty value' in str(context.exception))        
    

if __name__=='__main__':
    unittest.main()