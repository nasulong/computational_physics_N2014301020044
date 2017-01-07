# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:48:37 2017

@author: 文龙
"""
import numpy as np
import pylab as pl
import random
import math 


class diffusion():
    """
    time evolution calculated from the diffusion equation in one dimension
    """
    def __init__(self,D,dt,dx,steps):
        self.D=D
        self.dx=dx
        self.dt=dt
        self.steps=steps
        self.xx=np.linspace(-self.steps,self.steps,2*self.steps+1)
        self.y=[[0]*(2*self.steps+1) for i in range(self.steps+1)] 

        self.y[0][self.steps]=1
        self.y[0][0]=0
        self.y[0][2*self.steps]=0

    def iteration(self):
        m=self.D*self.dt/(self.dx**2)
        for n in range(self.steps):
            for i in range(1,2*self.steps):
                
                self.y[n+1][i]=self.y[n][i]+m*(self.y[n][i+1]+self.y[n][i-1]-2*self.y[n][i])
                self.y[n+1][0]=0
                self.y[n+1][2*self.steps]=0

        return [self.y[self.steps],self.xx]
pl.subplot(221)   
a1=diffusion(1,0.5,1,100)
b1=a1.iteration()
pl.plot(b1[1],b1[0])
pl.xlabel("x")
pl.ylabel("density")
pl.xlim(-100,100)
pl.title("diffusion in one dimension,steps=100")

pl.subplot(222)   
a1=diffusion(1,0.5,1,300)
b1=a1.iteration()
pl.plot(b1[1],b1[0])
pl.xlabel("x")
pl.ylabel("density")
pl.xlim(-100,100)
pl.title("diffusion in one dimension,steps=300")

pl.subplot(223)   
a1=diffusion(1,0.5,1,600)
b1=a1.iteration()
pl.plot(b1[1],b1[0])
pl.xlabel("x")
pl.ylabel("density")
pl.xlim(-100,100)
pl.title("diffusion in one dimension,steps=600")

pl.subplot(224)   
a1=diffusion(1,0.5,1,1000)
b1=a1.iteration()
pl.plot(b1[1],b1[0])
pl.xlabel("x")
pl.ylabel("density")
pl.xlim(-100,100)
pl.title("diffusion in one dimension,steps=1000")
