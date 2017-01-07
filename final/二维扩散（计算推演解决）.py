# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:37:46 2017

@author: 文龙
"""

"""
Created on Sat Jan  7 09:58:47 2017

@author: 文龙
"""
import numpy as np
import pylab as pl
import random
import math 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


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
        
        self.z=[[0]*(2*self.steps+1) for i in range(2*self.steps+1)] 
        self.z[self.steps][self.steps]=1
        
        for i in range(0,2*self.steps+1):
            self.z[0][i]=0
            self.z[2*self.steps][i]=0
        for i in range(0,2*self.steps+1):
            self.z[i][0]=0
            self.z[i][2*self.steps]=0

        
        
        

    def iteration(self):
        for j in range(self.steps):
            for n in range(1,2*self.steps):
                for i in range(1,2*self.steps):
                    self.z[n][i]=(self.z[n][i-1]+self.z[n][i+1]+self.z[n-1][i]+self.z[n+1][i])/4
                    self.z[n][0]=0
                    self.z[n][2*self.steps]=0
            

        return [self.z,self.xx]


    def diffusion_picture(self,ax,x1,x2,y1,y2):  
        self.x=np.linspace(-self.steps,self.steps,2*self.steps+1)
        self.y=np.linspace(-self.steps,self.steps,2*self.steps+1)
        self.x,self.y=np.meshgrid(self.x,self.y)
        self.surf=ax.plot_surface(self.x,self.y,self.z)
        ax.set_xlim(-100,100)
        ax.set_ylim(-100,100)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
        ax.set_xlabel('x ',fontsize=14)
        ax.set_ylabel('y ',fontsize=14)
        ax.set_zlabel('density',fontsize=14)
        ax.set_title('diffusion,t=100',fontsize=18)
      
fig=plt.figure(figsize=(14,7))
ax1= plt.subplot(1,1,1,projection='3d')
m1=diffusion(1,0.25,1,100)
m1.iteration()
m1.diffusion_picture(ax1,-1,1,-1,1)

plt.show(fig)
