#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 05:49:43 2020

@author: cheer
"""
import unittest
import numpy as np
from main_predict import main_prediction

class TestMainprediction(unittest.TestCase):
    
    def test_output_type(self):
        #check if s2t
        final_prediction=main_prediction('不要再閃退了')
        self.assertEqual(type(final_prediction)==list,True)
        self.assertTrue(type(final_prediction[0])==str)
        self.assertTrue(type(final_prediction[1])==np.float32)

if __name__=='__main__':
    unittest.main()