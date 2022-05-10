# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:36:32 2021

author: Brandon Sweeney
email: bpsweeney@alaska.edu

"""
import numpy as np
from board import Board
from Computer import Computer
import copy

def GetWhoMovesFirst():
    print("Player or computer move first?")
    firstMove = input("P or C: ")
    if(firstMove == 'P' or firstMove == 'p'):
        GetHumanPlayerMove()
    else:
        GenerateComputerPlayerMove()
        
def GetHumanPlayerMove():
    stopGame = False
    print(Game)
    print("Pick a pocket you would like to move.")
    print("It's 0-5 left to right. You are the bottom player")
    print("and you will go counterclock-wise.")
    print("If you want to stop playing type 100.")
    while True:
        try:
            playerMove = int(input("0-5:"))
        except ValueError:
            playerMove = 1000
        if(playerMove >= 0 and playerMove < 6):
            if(Game.ValidMove(1,playerMove)):
                Game.MakeMove(1,playerMove)
                break
            else:
                print("That pocket has 0 stones.")
                print("Try again")
        elif(playerMove == 100):
            stopGame = True
            break
        else:
            print("Not a valid move.")
            print("Try again")
    
    if(stopGame):
        print("Thank you for playing.")
    elif(Game.Isover()):
        Game.Results()
    else:
        GenerateComputerPlayerMove()

def GenerateComputerPlayerMove():
    print(Game)
    Com = Computer(copy.deepcopy(Game), 0)
    # I suspect this function may take some time.
    val, cMove = Com.generateMove(8, "Max")
    Game.MakeMove(0, cMove)
    print("Computer moves pocket number", comMove[cMove - 1])
    if(Game.Isover()):
        Game.Results()
    else:
        GetHumanPlayerMove()
    
# Global Game Board.
Game = Board(np.array([[0, 3, 3, 3, 3, 3, 3],
                       [3, 3, 3, 3, 3, 3, 0]]))
#Game = Board(np.array([[16, 0, 0, 1, 0, 0, 0],
#                       [0, 0, 5, 3, 0, 0, 10]]))
#Used when saying the computer move.
comMove = [12,11,10,9,8,7]
#comMove = [5,4,3,2,1,0]
print(Game)
print("Player will always be on the south side in this game.")
GetWhoMovesFirst()
