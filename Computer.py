# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:50:25 2021

@author: Brandon
"""
from Node import Node
from board import Board
import numpy as np
import copy

class Computer():
    def __init__(self, g, index):
        self.g = g
        self.i = index
        self.n = Node()
    ## I choose to follow a function on wikipedia instead of the book.
    ##This  ##https://en.wikipedia.org/wiki/Alpha-beta_pruning
    ## Made a few minor changes, but I think it's working?
    def generateMove(self, lim, t):
        if(lim == 0):
            ## Prints were used to give me 
            ## some confidence that my program was working.
            ##print("lim is zero go back with cost")
            return self.g.getCost(), self.i;
        validMove = False
        if(t == "Max"):
            val = float('-inf')
            move = None
            for i in range(6):
                if(self.g.ValidMove(0, i + 1)):
                    validMove = True
                    bo = copy.deepcopy(self)
                    bo.i = i + 1
                    bo.g.MakeMove(0, i + 1)
                    ### num is a throw away value.
                    temp, num = bo.generateMove(lim-1,"Min")
                    ##print("Got a value at", lim, i)
                    ## Will prioritize right hand side moves first.
                    ## The computer is the top player.
                    ## Could be be bad or good.
                    if(temp > val):
                        val = temp
                        self.n.alpha = val
                        move = bo.i
                    if(val >= self.n.beta):
                        self.n.alpha = val
                        break
            ##This means we are at the cutoff and need to generate the cost.
            ## Could have also been if(move == none) probably.
            if(validMove == False):
                return self.g.getCost(), self.i;
            return self.n.alpha, move
        else:
            val = float('inf')
            move = None
            for i in range(6):
                if(self.g.ValidMove(1,i)):
                    validMove = True
                    bo = copy.deepcopy(self)
                    bo.i = i
                    bo.g.MakeMove(1, i)
                    temp, num = bo.generateMove(lim-1,"Max")
                    if(temp < val):
                        val = temp
                        self.n.beta = val
                        move = bo.i
                    if(val <= self.n.alpha):
                        self.n.beta = val
                        break
                    self.n.beta = val
            ##This means we are at the cutoff and need to generate the cost.
            if(validMove == False):
                return self.g.getCost(), self.i;
            return self.n.beta, move