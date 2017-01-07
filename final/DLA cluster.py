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
        self.xy=[[0]*(101) for i in range(101)]
        self.xy[50][50]=1
                
    def simulate(self):
        x=50
        y=50
        for i in range(self.steps):
            temp=random.uniform(0,1)
            if temp<=0.25:
                if y-1>=0 and self.xy[x][y-1]==0:
                    self.xy[x][y-1]=1
                    self.xy[x][y]=1
                    y=y-1
            elif temp<=0.5:
                if y+1<=100 and self.xy[x][y+1]==0:
                    self.xy[x][y+1]=1
                    self.xy[x][y]=1
                    y=y+1
            elif temp<=0.75:
                if x-1>=0 and self.xy[x-1][y]==0:
                    self.xy[x-1][y]=1
                    self.xy[x][y]=1
                    x=x-1
            elif temp<=1:
                if x+1<=100 and self.xy[x+1][y]==0:
                    self.xy[x+1][y]=1
                    self.xy[x][y]=1
                    x=x+1
            i=i+1
        return self.xy
        
a=cluster(100000)
b=a.simulate()
for i in range(101):
    for j in range(101):
        if b[i][j]!=0:
           pl.scatter([i],[j],6,color='red')
pl.xlim(0,100)
pl.ylim(0,100)

pl.show()
