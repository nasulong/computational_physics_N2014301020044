# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:57:49 2017

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
        for i in range(50,51):
            for j in range(50,51):
                self.xy[i][j]=1
                
    def simulate(self):
        for n in range(self.steps):
            temp1=random.randint(0,100)
            temp2=random.randint(0,100)
            if self.xy[temp1][temp2]!=0:
                temp3=random.uniform(0,1)
                if temp3<=0.25:
                    if temp2-1>=0 and self.xy[temp1][temp2-1]==0:
                        self.xy[temp1][temp2-1]=1
                        self.xy[temp1][temp2]=1
                elif temp3<=0.5:
                    if temp2+1<=100 and self.xy[temp1][temp2+1]==0:
                        self.xy[temp1][temp2+1]=1
                        self.xy[temp1][temp2]=1
                elif temp3<=0.75:
                    if temp1-1>=0 and self.xy[temp1-1][temp2]==0:
                        self.xy[temp1-1][temp2]=1
                        self.xy[temp1][temp2]=1
                elif temp3<=1:
                    if temp1+1<=100 and self.xy[temp1+1][temp2]==0:
                        self.xy[temp1+1][temp2]=1
                        self.xy[temp1][temp2]=1
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
