#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 01:48:39 2020

@author: cheer
"""
from opencc import OpenCC
import re


def text_preprocess(txt):

    
    if type(txt)!=str:
        raise Exception('invalid input')
    cop=re.compile("[^\u4e00-\u9fa5]")
    txt=cop.sub('',txt)
    cc = OpenCC('s2t')
    txt=cc.convert(txt)
    return txt