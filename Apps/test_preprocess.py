#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 05:49:43 2020

@author: cheer
"""
import unittest
from preprocess import text_preprocess

class TestPreprocess(unittest.TestCase):
    
    def test_simplified_to_traditional(self):
        #check if s2t
        self.assertEqual(text_preprocess('腾讯收购搜狗的交易尘埃落定'),'騰訊收購搜狗的交易塵埃落定')

    def test_filter_non_chinese(self):
        #check if filter non Chinese character
        self.assertEqual(text_preprocess('asdqweqwdqsdqd'),'')
        self.assertEqual(text_preprocess('@#$^&*^&&&'),'')
    
    def test_incorrect_input_type(self):
        with self.assertRaises(Exception) as context:
            text_preprocess(['3'])
        self.assertTrue('invalid input' in str(context.exception))      
    

if __name__=='__main__':
    unittest.main()