# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:14:46 2017

@author: 文龙
"""

import numpy as np
import pylab as pl
import random
import math 

class cluster():
    """
    cluster
    """
    def __init__(self,steps):
        self.steps=steps
        self.xy=[[0]*(21) for i in range(21)]
        self.xy[10][10]=1
                
    def simulate(self):
        deadend=0
        bingo=0
        x=10
        y=10
        for i in range(self.steps):
            temp=random.uniform(0,1)
            if temp<=0.25:
                if  self.xy[x][y-1]==1:
                    deadend+=1
                    break
                if y-1<0:
                    bingo+=1
                    break
                if y-1>=0 and self.xy[x][y-1]==0:
                    self.xy[x][y-1]=1
                    self.xy[x][y]=1
                    y=y-1
                    
            elif temp<=0.5:
                if  self.xy[x][y+1]==1:
                    deadend+=1
                    break
                if y+1>20:
                    bingo+=1
                    break
                if y+1<=20 and self.xy[x][y+1]==0:
                    self.xy[x][y+1]=1
                    self.xy[x][y]=1
                    y=y+1
                    
            elif temp<=0.75:
                if  self.xy[x-1][y]==1:
                    deadend+=1    
                    break
                if x-1<0:
                    bingo+=1
                    break
                if x-1>=0 and self.xy[x-1][y]==0:
                    self.xy[x-1][y]=1
                    self.xy[x][y]=1
                    x=x-1
                    
            elif temp<=1:
                if  self.xy[x+1][y]==1:
                    deadend+=1    
                    break
                if x+1>20:
                    bingo+=1
                    break
                if x+1<=20 and self.xy[x+1][y]==0:
                    self.xy[x+1][y]=1
                    self.xy[x][y]=1
                    x=x+1
            
            for i in range(21):
                for j in range(21):
                    if self.xy[i][j]!=0:
                        pl.scatter([i],[j],15,color='black')
            pl.xlim(0,20)
            pl.ylim(0,20)
            pl.show()
            i=i+1
        print (str(100*deadend/self.steps)+"%  dead end")
        
        
a=cluster(5)
b=a.simulate()
