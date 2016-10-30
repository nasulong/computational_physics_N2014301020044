# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 15:15:09 2016

@author: 文龙
"""

import pylab as pl
import math
class  Poincare_sections:
    """
    Program 3.12
    Construct the poincare sections for some different cases
    and compare them with Figure 3.9
    """
    def __init__(self,friction_coefficient=0.5,gravity=9.8,rope_length=9.8,angular_frequency_of_driving_force=2/3,ampulitude=1.2,time_of_step=0.04):
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
        while self.t[i]<=5000:     
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
            
            x=int(self.Ω*self.t[i]/(2*math.pi))  #确定所选取的周期性时间点t
            y=self.Ω*self.t[i]/(2*math.pi)
            if abs(x-y)<0.01:
                self.t2.append(self.t[i])  #t2,ω2,Θ2为所选取的点的数据列表
                self.ω2.append(self.ω[i])
                self.Θ2.append(self.Θ[i])
            i+=1

            
        
            
            
    def show_result(self):      
        pl.plot(self.Θ2,self.ω2,".")
        pl.xlabel("Θ(radians)")
        pl.ylabel("ω(radians/s")
        pl.xlim(-4,4)
        pl.ylim(-2,1)
        pl.show()
a=Poincare_sections()
a.calculate()
a.show_result()
