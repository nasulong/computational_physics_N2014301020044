# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:46:30 2016

@author: 文龙
"""

from numpy import *
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class Electric():
    
    """
    Two capacitor plates held at V=1(left plate)and V=-1(right plate).The square boundary 
    surrounding the plates is held at V=0
    """ 
    def __init__(self, V1=1, V2=-1, V_boundary=0, n=30):
        self.V1=V1
        self.V2=V2
        self.V_boundary=V_boundary
        self.n=int(n)
        self.V=[[0]*(self.n+1) for i in range(self.n+1)] 
        for j in range(0,self.n+1):
            self.V[0][j]=0
            self.V[self.n][j]=0
        for i in range(0,self.n+1):
            self.V[i][0]=0
            self.V[i][self.n]=0
        for i in range(int(self.n/3),int(self.n/3*2+1)):
            self.V[i][int(self.n/3)]=self.V1
            self.V[i][int(self.n/3*2)]=self.V2

    def update_V(self):     
        self.counter=0
        self.delta_V=0
        self.V_2=self.V

        while True:
            for i in range(1,self.n):
                for j in range(1,self.n):
                    temp_V=(self.V[i-1][j]+self.V[i+1][j]+self.V[i][j-1]+self.V[i][j+1])/4

                    self.V[i][j]=temp_V
                
            for i in range(int(self.n/3),int(self.n/3*2+1)):
                self.V[i][int(self.n/3)]=self.V1
                self.V[i][int(self.n/3*2)]=self.V2
        
            for i in range(1,self.n):
                for j in range(1,self.n):
                    self.delta_V=self.delta_V+abs(self.V_2[i][j]-self.V[i][j])

            self.counter=self.counter+1
            self.V_2=self.V
        
            if self.delta_V < (961*(1.0E-5))and self.counter >1000:
                break
        return (self.counter,self.delta_V,self.V)
        
    def Electric_field(self,x1,x2,y1,y2):  #计算电场矢量 
        self.dx=abs(x1-x2)/self.n
        self.dy=abs(y1-y2)/self.n
        self.Ex=[[0]*(self.n+1) for i in range(self.n+1)] 
        self.Ey=[[0]*(self.n+1) for i in range(self.n+1)] 
        for i in range(1,self.n):
            for j in range(1,self.n):
                self.Ex[i][j]=-(self.V[i][j+1]-self.V[i][j-1])/(2*self.dx)
                self.Ey[i][j]=(self.V[i+1][j]-self.V[i-1][j])/(2*self.dy)
        return (self.Ex,self.Ey)
        
        
    def Potential_picture(self,ax,x1,x2,y1,y2):  #画电势3维图
        self.x=linspace(x1,x2,self.n+1)
        self.y=linspace(y2,y1,self.n+1)
        self.x,self.y=meshgrid(self.x,self.y)
        self.surf=ax.plot_surface(self.x,self.y,self.V, rstride=1, cstride=1, cmap=cm.coolwarm)
        ax.set_xlim(x1,x2)
        ax.set_ylim(y1,y2)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
        ax.set_xlabel('x ',fontsize=14)
        ax.set_ylabel('y ',fontsize=14)
        ax.set_zlabel('V',fontsize=14)
        ax.set_title('Potential',fontsize=18)
        
    def Electric_picture(self,ax1,ax2,x1,x2,y1,y2):    # 画电场图
        self.x=linspace(x1,x2,self.n+1)
        self.y=linspace(y2,y1,self.n+1)
        self.x,self.y=meshgrid(self.x,self.y)
        cs=ax1.contour(self.x,self.y,self.V)
        plt.clabel(cs, inline=1, fontsize=10)
        ax1.set_title('Electric potential near two metal plates',fontsize=18)
        ax1.set_xlabel('x ',fontsize=14)
        ax1.set_ylabel('y ',fontsize=14)
        
        for i in range(1,self.n,1):
            for j in range(1,self.n,1):
                ax2.arrow(self.x[i][j],self.y[i][j],self.Ex[i][j]/40,self.Ey[i][j]/40)             
        ax2.set_xlim(-1,1)
        ax2.set_ylim(-1,1)
        ax2.set_title('Electric field near two metal plates',fontsize=18)
        ax2.set_xlabel('x ',fontsize=14)
        ax2.set_ylabel('y ',fontsize=14)
        
              
# give plot of potential and electric field 
fig=plt.figure(figsize=(10,5))
ax1=plt.axes([0.1,0.1,0.35,0.8])
ax2=plt.axes([0.55,0.1,0.35,0.8])
cmp=Electric(1,-1,0,20)
cmp.update_V()
cmp.Electric_field(-1,1,-1,1)
cmp.Electric_picture(ax1,ax2,-1,1,-1,1)
plt.show()     
# give 3d plot of potential
fig=plt.figure(figsize=(14,7))
ax1= plt.subplot(1,2,1,projection='3d')
cmp=Electric()
cmp.update_V()
cmp.Potential_picture(ax1,-1,1,-1,1)



plt.show(fig)
