# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:55:15 2016

@author: 文龙
"""

import numpy as np
import pylab as pl
import math 

class propagate():
    """
    A spectrum analysis of waves on a guitar string
    """
    def __init__(self,c,dx,length,time,T):
        self.c=c
        self.T=T
        self.dx=dx
        self.dt=dx/c
        self.steps=int(length/dx)
        self.time=int(time)
        self.y=[[0]*(self.steps+1) for i in range(self.time)] 
        for i in range(int(self.steps/5)):
            self.y[0][i]=0.00003*i
            self.y[1][i]=0.00003*i
        for i in range(int(self.steps/5),self.steps+1):
            self.y[0][i]=0.006-(i-int(self.steps/5))*0.0000075
            self.y[1][i]=0.006-(i-int(self.steps/5))*0.0000075

        self.y[0][0]=0
        self.y[1][0]=0
        self.y[0][self.steps]=0
        self.y[1][self.steps]=0
        self.y1=[]
        self.y1.append(self.y[0][15])
        self.y1.append(self.y[1][15])
        self.t=[0]
        self.t.append(self.dt*1)
        
        self.x=np.arange(0,(self.steps+1)*self.dx,self.dx)
        
        self.F_bridge=[]
        self.F_bridge.append(self.T*(self.y[0][1]-self.y[0][0])/self.dx)
        self.F_bridge.append(self.T*(self.y[1][1]-self.y[1][0])/self.dx)

        
    def iteration(self):
        r=self.c*self.dt/self.dx
        for n in range(self.time-2):
            for i in range(1,self.steps):
                self.y[n+2][i]=2*(1-r**2)*self.y[n+1][i]-self.y[n][i]+r**2*(self.y[n+1][i+1]+self.y[n+1][i-1])
                self.y[n+2][0]=0
                self.y[n+2][self.steps]=0
            self.y1.append(self.y[n+2][15])
            self.t.append((n+2)*self.dt)
            
            self.F_bridge.append(self.T*(self.y[n+2][1]-self.y[n+2][0])/self.dx)
        

        return [self.t,self.y1,self.dt,self.y[1000],self.F_bridge,self.x]
    
a=propagate(320,0.00065,0.65,6000,149)
b=a.iteration()

pl.subplot(221)
pl.plot(b[5],b[3])
pl.xlabel("x(m)")
pl.ylabel("y(m)")
pl.xlim(0,0.7)
pl.ylim(-0.006,0.006)
pl.title("guitar pluck:M=1000")

pl.subplot(222)
y=abs(np.fft.rfft(b[1]))**2
x=np.linspace(0,int(1/b[2]/2),len(y))
pl.plot(x,y)
pl.xlabel("Frequency(Hz)")
pl.ylabel("Powre")
pl.xlim(0,3000)
pl.title("Power spectrum")

pl.subplot(223)
pl.plot(b[0],b[4])
pl.xlabel("time(s)")
pl.ylabel("bridge force")
pl.title("force on bridge vs time")



pl.show()
