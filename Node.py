# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:36:54 2021

@author: Brandon
"""

class Node(object):
    def __init__(self):
        self.alpha = float('-inf')
        self.beta = float('inf')
        #self.Ntype = Ntype
