# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:15:19 2016

@author: 文龙
"""

import pylab as pl
import math



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
        self.steps=80000
        self.Θ=[Θ0]
        self.ω=[ω0]
        self.r=[]

    def calculate(self):

        for i in range(self.steps):
            if self.Θ[i]>math.pi:    #确保角度Θ在-π到+π之间
                self.Θ[i]=self.Θ[i]-2*math.pi
            if self.Θ[i]<-math.pi:
                self.Θ[i]=self.Θ[i]+2*math.pi
            else:
                self.Θ[i]=self.Θ[i]

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

        
        return self.x,self.y,self.t,self.Θ,self.ω      

    def show_result1(self):
        pl.plot(self.t,self.Θ,"black")
        pl.xlabel('time(yr)')
        pl.ylabel('theta(radians)')
        pl.xlim(0,8)
        pl.ylim(-4,4)
        pl.grid(True)
        pl.title('Hyperion theta versus time,circular orbit')
        pl.show()
    
   
    def show_result2(self):
        pl.plot(self.t,self.ω,"black")
        pl.xlabel('time(yr)')
        pl.ylabel('omega(radians/yr)')
        pl.xlim(0,8)
        pl.ylim(0,15)
        pl.grid(True)
        pl.title('Hyperion omega versus time,circular orbit')
        pl.show()
      


v=Hyperion(1,0,0,2*math.pi,0,0)    #椭圆轨道只需要把初始的vy改为5HU/Hyperion-year
v.calculate()
v.show_result2()


