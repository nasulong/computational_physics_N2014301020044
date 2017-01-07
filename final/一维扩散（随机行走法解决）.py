# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:20:42 2017

@author: 文龙
"""

import numpy as np
import pylab as pl
import random
import math 

class rwalk():
    """
    random-walker distributions in one dimension
    """
    def __init__(self,steps,walkers):
        self.steps=steps
        self.walkers=walkers
        
        self.x=np.zeros(int(self.steps))
        
        self.t=np.linspace(-self.steps,self.steps,2*self.steps+1)
        
        self.x2=[[0]*(2*self.steps+1) for i in range(2)]
        self.x3=0
        
    def calculate(self):
        for n in range(int(self.walkers)):
            self.x3=0
            for i in range(int(self.steps)):
                temp1=random.uniform(0,1)
                if temp1<=0.5:
                    self.x3=self.x3-1
                if temp1>0.5:
                    self.x3=self.x3+1
            y=self.x3
            self.x2[1][int(self.steps+y)]+=1
        x4=[]
        for n in range(len(self.x2[1])):
            
            x4.append(self.x2[1][n]/self.walkers)
        
        return [self.t,x4]     
        
pl.subplot(221)        
a1=rwalk(10,1000)
b1=a1.calculate()
pl.plot(b1[0],b1[1])
pl.xlabel("x")
pl.ylabel("probability")
pl.title("steps=10")

pl.subplot(222)        
a2=rwalk(100,1000)
b2=a2.calculate()
pl.plot(b2[0],b2[1])
pl.xlabel("x")
pl.ylabel("probability")
pl.title("steps=100")

pl.subplot(223)        
a3=rwalk(1000,1000)
b3=a3.calculate()
pl.plot(b3[0],b3[1])
pl.xlabel("x")
pl.ylabel("probability")
pl.title("steps=1000")

pl.subplot(224)        
a4=rwalk(2000,1000)
b4=a4.calculate()
pl.plot(b4[0],b4[1])
pl.xlabel("x")
pl.ylabel("probability")
pl.title("steps=2000")


pl.show()
