# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:43:59 2016

@author: 文龙
"""
import numpy as np
import pylab as pl
import math 

class propagate():
    """
    A spectrum analysis of waves on a string in which two ends are held fixed.Assume 
    an initial Gaussian wavepacket located
    40 percent from one end
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
            self.y[0][i]=math.exp(-self.k*(i*self.dx-0.4)**2)
            self.y[1][i]=math.exp(-self.k*(i*self.dx-0.4)**2)
        self.y[0][0]=0
        self.y[1][0]=0
        self.y[0][self.steps]=0
        self.y[1][self.steps]=0
        self.y1=[]
        self.y1.append(self.y[0][5])
        self.y1.append(self.y[1][5])
        self.t=[0]
        self.t.append(self.dt*1)
        
    def iteration(self):
        r=self.c*self.dt/self.dx
        for n in range(self.time-2):
            for i in range(1,self.steps):
                self.y[n+2][i]=2*(1-r**2)*self.y[n+1][i]-self.y[n][i]+r**2*(self.y[n+1][i+1]+self.y[n+1][i-1])
                self.y[n+2][0]=0
                self.y[n+2][self.steps]=0
            self.y1.append(self.y[n+2][5])
            self.t.append((n+2)*self.dt)
        return [self.y1,self.t,self.dt]
    
a=propagate(300,0.01,1,1300,1000)
b=a.iteration()
pl.subplot(121)
pl.plot(b[1],b[0])
pl.xlabel("Time(s)")
pl.ylabel("Signal")
pl.title("String signal versus time")

pl.subplot(122)
y=abs(np.fft.rfft(b[0]))**2
x=np.linspace(0,int(1/b[2]/2),len(y))
pl.plot(x,y)
pl.xlabel("Frequency(Hz)")
pl.ylabel("Powre")
pl.xlim(0,3000)
pl.title("Power spectrum")
pl.show()
    
