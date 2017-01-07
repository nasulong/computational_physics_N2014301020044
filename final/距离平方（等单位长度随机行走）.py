# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:57:41 2017

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
    def __init__(self,steps,walkers):
        self.walkers=walkers
        self.steps=steps
        self.numbers=[]
        self.x=np.zeros(int(walkers))
        self.temp=np.zeros(int(walkers))
        self.t=[0]
        self.x_aver=[0]
    def simulate(self):
        for i in range(int(self.steps)):
            for n in range(int(self.walkers)):
                temp1=random.uniform(0,1)
                if temp1<=0.5:
                    self.x[n]=self.x[n]-1
                if temp1>0.5:
                    self.x[n]=self.x[n]+1
                self.temp[n]=self.x[n]**2
            self.x_aver.append(np.sum(self.temp)/(int(self.walkers)))
            self.t.append(self.t[i]+1)
        
        return [self.t,self.x_aver]     
        
a1=rwalk(100,2000)
a2=rwalk(100,4000)
b1=a1.simulate()
b2=a2.simulate()
pl.plot(b1[0],b1[1],"r.")
pl.plot(b2[0],b2[1],"b.")
pl.xlabel("step number")
pl.ylabel("average of the square displacement")
pl.title("random walk in one dimension")
z=np.polyfit(b2[0],b2[1],1)      #线性拟合
p=np.poly1d(z)
print(p)
pl.show()

#拟合结果0.9994 x + 0.2927
