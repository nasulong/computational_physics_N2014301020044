# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:55:32 2017

@author: 文龙
"""

import numpy as np
import pylab as pl
import random
import math 

class rwalk():
    """
    simulating one-dimensional random walks and calculating the mean-squared displacement
    """
    def __init__(self,steps):
        self.steps=steps
        self.numbers=[]
        self.x=[0]
        self.t=[0]
    def simulate(self):
        for i in range(int(self.steps)):
            temp1=random.uniform(0,1)
            self.t.append(self.t[i]+1)
            if temp1<=0.5:
                self.x.append(self.x[i]-1)
            if temp1>0.5:
                self.x.append(self.x[i]+1)
            

        
        return [self.t,self.x]     
        
a1=rwalk(100)
a2=rwalk(100)
b1=a1.simulate()
b2=a2.simulate()

pl.plot(b1[0],b1[1],".")
pl.plot(b2[0],b2[1],".")
pl.xlabel("step number")
pl.ylabel("x")
pl.title("random walk in one dimension")

pl.show()
