# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 22:47:24 2016

@author: 文龙
"""

import pylab as pl
import math
class billiard_on_a_square_table():
    """This is a continuation of the ttrajectory of a billiard
    on a square table
    """
    def __init__(self,time_step=0.01,x0=0.2,y0=0,vx0=1,vy0=0.5,steps=20000):
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=time_step
        self.t=[0]
        self.steps=steps
    def backtrack(self,condition,x,y,vx,vy,t):#倒退回溯确定撞击点的函数
        m=0
        while eval(condition):
            x=x+vx*self.dt/100
            y=y+vy*self.dt/100
            m+=1   
        return x,y,self.dt/100*m+t
        
    def calculate(self):
        for i in range(self.steps):
            temp_x=self.x[i]+self.vx[i]*self.dt
            temp_y=self.y[i]+self.vy[i]*self.dt
            temp_vx=self.vx[i]
            temp_vy=self.vy[i]
            self.x.append(temp_x)
            self.y.append(temp_y)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.t.append(self.t[i]+self.dt)
            if(self.x[i+1]>1):
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("x<=1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vx[i+1]=-self.vx[i+1]
            if(self.x[i+1]<-1):
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("x>=1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vx[i+1]=-self.vx[i+1]
            if(self.y[i+1]<-1):
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("y>=-1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vy[i+1]=-self.vy[i+1]
            if(self.y[i+1]>1):
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("y<=1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vy[i+1]=-self.vy[i+1]
        return self.x,self.y
        
    def show_result(self):
        pl.plot(self.x,self.y,"b")
        pl.xlabel('x')
        pl.ylabel('y')
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.title('trajectory of a billiard on a square table')
        pl.show()
                
a=billiard_on_a_square_table()
a.calculate()
a.show_result()               
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
