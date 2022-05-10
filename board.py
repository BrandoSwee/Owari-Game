# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:26:07 2021

@author: Brandon
"""
import numpy as np

# Board will be a numpy array that
# should start as this: 
# b = np.array([[0, 3, 3, 3, 3, 3, 3],
#               [3, 3, 3, 3, 3, 3, 0]])
class Board(object):
    def __init__(self,b):
        self.b = b
    # Prints a board similar to the one in the example.
    def __repr__(self):
        s = '  '
        for i in range(1 , 7):
            s += str(self.b[0][i])
            s += " "
        s += '\n'
        s += str(self.b[0][0])
        s += '             '
        s += str(self.b[1][6])
        s += '\n'
        s += '  '
        for i in range(0 , 6):
            s += str(self.b[1][i])
            s += " "
        s += '\n'
        return s
    def MakeMove(self, side, pocket):
        ### The numpy was making this hard to think about
        ### I should have made the whole thing one array
        ### It's a little late for that now I suppose.
        if(side == 0):
            m = self.b[side][pocket]
            ### Just incase we loop the whole board.
            self.b[side][pocket] = 0
            temp = pocket
            n = 0
            ### Made the computer's loop second 
            for i in range(1, (m + 1)):
                ## temp should start as 1-6 and decrease
                if(temp == 0):
                    self.b[1][n] += 1
                    n = n + 1
                    if(n == 6):
                        temp = 7
                else:
                    temp = temp - 1
                    self.b[side][temp] += 1
                    ## if last move and not in goal
                    if(i == m and temp != 0):
                        ## Do you only have 1 stone?
                        if(self.b[side][temp] == 1):
                            self.b[0][0] += self.b[1][temp - 1]
                            self.b[1][temp - 1] = 0
                    n = 0
        else:
            m = self.b[side][pocket]
            ### Just incase we loop the whole board.
            self.b[side][pocket] = 0
            temp = pocket + 1
            n = 6
            for i in range(1, (m + 1)):
                ###2nd can handle 6
                if(temp > 6):
                    self.b[0][n] += 1
                    n = n - 1
                    if(n == 0):
                        temp = 0
                else:
                    self.b[side][temp] += 1
                    ### Check for steal
                    if(i == m and temp != 6):
                        if(self.b[side][temp] == 1):
                            self.b[1][6] += self.b[0][temp + 1]
                            self.b[0][temp + 1] = 0
                    temp += 1
                    n = 6
                
    def ValidMove(self, who, num):
        if(self.b[who][num] != 0):
            return True
        return False
    
    def getBoard(self):
        return self.b
    
    def Isover(self):
        tempC = self.b[0][6] + self.b[0][1] + self.b[0][2] + self.b[0][3] + self.b[0][4] + self.b[0][5]
        tempP = self.b[1][0] + self.b[1][2] + self.b[1][3] + self.b[1][4] + self.b[1][5] + self.b[1][1]
        if(tempC == 0):
            self.b[1][6] += tempP
            for i in range(0, 6):
                self.b[1][i] = 0
            return True
        elif(tempP == 0):
            self.b[0][0] += tempC
            for i in range(1, 7):
                self.b[0][i] = 0
            return True
        return False
    def getCost(self):
        #Com will be positive and human is negative.
        PiecesInGoal = 0
        PiecesInGoal += (self.b[0][0]*2)
        PiecesInGoal = PiecesInGoal - (self.b[1][6]*2)
#        EmptySpots = 0
#        for i in range(6):
#            if(self.b[0][i + 1] == 0):
#                EmptySpots += 1
#            if(self.b[1][i]== 0):
#                EmptySpots -= 1
#        oppositeEmptyandsideisgreaterthan2 = 0
#        for i in range(6):
#            if(self.b[0][i + 1] > 2):
#                if(self.b[1][i] == 0):
#                    oppositeEmptyandsideisgreaterthan2 -= (self.b[0][i + 1] - 2)
#            if(self.b[1][i] > 2):
#                if(self.b[0][i + 1] == 0):
#                    oppositeEmptyandsideisgreaterthan2 += (self.b[1][i] - 2)
        tempC = self.b[0][6] + self.b[0][1] + self.b[0][2] + self.b[0][3] + self.b[0][4] + self.b[0][5]
        tempP = self.b[1][0] + self.b[1][2] + self.b[1][3] + self.b[1][4] + self.b[1][5] + self.b[1][1]
        PiecesOnSide = 0
        if(tempC == 0 or tempP == 0):
            PiecesOnSide += tempC*2
            PiecesOnSide -= tempP*2
        else:
            PiecesOnSide += tempC*1.5
            PiecesOnSide -= tempP*1.5
        
        totalcost = PiecesInGoal + PiecesOnSide#+ EmptySpots + oppositeEmptyandsideisgreaterthan2
        return totalcost
    def Results(self):
        print("Game over")
        if(self.b[0][0] > self.b[1][6]):
            print("The computer won", self.b[0][0], "to", self.b[1][6])
        elif(self.b[0][0] == self.b[1][6]):
            print("The game is a tie.")
        else:
            print("You beat the computer",self.b[1][6], "to",self.b[0][0])
            print("Congratulations!")