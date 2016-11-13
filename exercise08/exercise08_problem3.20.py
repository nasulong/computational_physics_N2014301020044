# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:27:17 2016

@author: 文龙
"""

import pylab as pl
import math
class  Poincare_sections:
    """
    Program 3.20
    Calculate the bifurcation diagram for the pendulum in the vicinity of FD=1.35
    to 1.5.
    """
    def __init__(self,friction_coefficient=0.5,gravity=9.8,rope_length=9.8,angular_frequency_of_driving_force=2/3,ampulitude=1.35,time_of_step=0.01):
        self.q=friction_coefficient
        self.l=rope_length
        self.g=gravity
        self.Ω=angular_frequency_of_driving_force
        self.FD=ampulitude
        self.dt=time_of_step
        self.t=[0]
        self.ω=[0]
        self.Θ=[0.2]
        self.t2=[]
        self.ω2=[]
        self.Θ2=[]
  
    def calculate(self):
        i=0
        while self.t[i]<3800:
            if self.Θ[i]>math.pi:    #确保角度Θ在-π到+π之间
                self.Θ[i]=self.Θ[i]-2*math.pi
            if self.Θ[i]<-math.pi:
                self.Θ[i]=self.Θ[i]+2*math.pi
            else:
                self.Θ[i]=self.Θ[i]
    
            temp_ω=self.ω[i]+(-self.g/self.l*math.sin(self.Θ[i])-self.q*self.ω[i]+self.FD*math.sin(self.Ω*self.t[i]))*self.dt
            self.ω.append(temp_ω)
            temp_Θ=self.Θ[i]+self.ω[i+1]*self.dt
            self.Θ.append(temp_Θ)
            self.t.append(self.t[i]+self.dt)
            
            x=int((self.Ω*self.t[i])/(2*math.pi))  #确定所选取的周期性时间点t
            y=(self.Ω*self.t[i])/(2*math.pi)
            if abs(x-y)<0.001 and self.t[i]>900*math.pi :#300周期以后取点
                self.t2.append(self.t[i])  #t2,ω2,Θ2为所选取的点的数据列表
                self.ω2.append(self.ω[i])
                self.Θ2.append(self.Θ[i])
                    
            i+=1
           
 
Θ3=[]
listFD=[]
i=0
for i in range(151):
    a=Poincare_sections(ampulitude=1.35+i/1000) 
    a.calculate()
    for j in range(len(a.Θ2)):
        Θ3.append(a.Θ2[j])
        listFD.append(1.35+i/1000)
pl.plot(listFD,Θ3,".")
pl.xlabel("FD")
pl.ylabel("$\\theta$(radians)")
pl.title('Bifurcation diagram $\\theta$ versus FD')
pl.xlim(1.35,1.5)
pl.ylim(0,3.5)
pl.show()




