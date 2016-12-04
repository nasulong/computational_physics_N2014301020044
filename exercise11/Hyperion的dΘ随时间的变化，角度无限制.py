# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:26:17 2016

@author: 文龙
"""


import pylab as pl
import math
import numpy as np


class Hyperion():
    """
    Tumblinng of Hyperion 
    """

    def __init__(self,x0,y0,vx0,vy0,Θ0,ω0):
        self.x=[x0]     
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=0.0001
        self.t=[0]
        self.steps=120000
        self.Θ=[Θ0]
        self.ω=[ω0]
        self.r=[]

    def calculate(self):

        for i in range(self.steps):
            self.r.append(math.sqrt(self.x[i]**2+self.y[i]**2))
            temp_vx=self.vx[i]-4*math.pi**2*self.x[i]*self.r[i]**(-3)*self.dt
            self.vx.append(temp_vx)
            temp_x=self.x[i]+self.vx[i+1]*self.dt
            temp_vy=self.vy[i]-4*math.pi**2*self.y[i]*self.r[i]**(-3)*self.dt
            self.vy.append(temp_vy)
            temp_y=self.y[i]+self.vy[i+1]*self.dt
            self.x.append(temp_x)
            self.y.append(temp_y)

            temp_ω=(self.ω[i]-self.dt*12*math.pi**2*self.r[i]**(-5)*(self.x[i]*math.sin(self.Θ[i])-self.y[i]*math.cos(self.Θ[i]))*(self.x[i]*math.cos(self.Θ[i])+self.y[i]*math.sin(self.Θ[i])))
            self.ω.append(temp_ω)
            self.Θ.append(self.Θ[i]+self.ω[i+1]*self.dt)
            
            self.t.append(self.t[i]+self.dt)

        
        return[self.x,self.y,self.t,self.Θ,self.ω]     



v1=Hyperion(1,0,0,2*math.pi,0,0) #椭圆轨道只需要把初始vy改变
HY1=v1.calculate()
v2=Hyperion(1,0,0,2*math.pi,0.01,0) 
HY2=v2.calculate()
Θ1=HY1[3]
Θ2=HY2[3]
t=HY1[2]
dΘ=np.array(HY2[3])-np.array(HY1[3])

pl.plot(t,dΘ,"g")
pl.xlabel('time(yr)')
pl.ylabel('dtheta(radians)')
pl.xlim(0,10)
pl.title('Hyperion dtheta versus time,circular orbit')
pl.show()
    



    


