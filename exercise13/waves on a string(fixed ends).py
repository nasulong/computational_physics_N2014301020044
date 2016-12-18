# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:46:27 2016

@author: 文龙
"""

import numpy as np
import pylab as pl
import math

class propagate():
    """
    Waves propagating on a string with fixed ends
    """
    def __init__(self,c,dx,length,time,k):
        self.c=c
        self.dx=dx
        self.dt=dx/c
        self.steps=int(length/dx)
        self.time=int(time)
        self.k=k
        self.y=[[0]*(self.steps+1) for i in range(self.time)] 
        for i in range(self.steps):
            self.y[0][i]=math.exp(-self.k*(i*self.dx-0.3)**2)
            self.y[1][i]=math.exp(-self.k*(i*self.dx-0.3)**2)
        self.y[0][0]=0
        self.y[0][self.steps]=0
        self.y[1][0]=0
        self.y[1][self.steps]=0

    def iteration(self):
        r=self.c*self.dt/self.dx
        for n in range(self.time-2):
            for i in range(1,self.steps):
                self.y[n+2][0]=0
                self.y[n+2][self.steps]=0
                self.y[n+2][i]=2*(1-r**2)*self.y[n+1][i]-self.y[n][i]+r**2*(self.y[n+1][i+1]+self.y[n+1][i-1])
        return [self.y[0],self.y[10],self.y[20],self.y[30],self.y[40],self.y[50],self.y[60],self.y[70],self.y[80],self.y[90],self.y[100],self.y[110]]
    
a=propagate(300,0.01,1,130,1000)
b=a.iteration()
for i in range(0,12):
    Y=b[i]
    pl.plot(range(101),Y)
pl.xlabel("x")
pl.ylabel("y")
pl.title("Waves on a string(fixed ends)")
pl.show()
    
    


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
