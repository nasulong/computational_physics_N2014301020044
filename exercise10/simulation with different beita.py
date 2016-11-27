# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:09:19 2016

@author: 文龙
"""
import pylab as pl
import math
def initial(a,e,MP,beta):
    MS=2*10**(30)
    x0=a*(1+e)
    y0=0
    vx0=0
    vy0=2*math.pi*math.sqrt((1-e)/(a*(1+e))*(1+MP/MS))
    return [x0,y0,vx0,vy0,beta]



class orbits():
    """
    planetary motion program with different beta
    """

    def __init__(self,x0,y0,vx0,vy0,beta):
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=0.001
        self.t=[0]
        self.steps=2000
        self.r=[]
        self.beta=beta
    

    def calculate(self):
        for i in range(self.steps):
            self.r.append(math.sqrt(self.x[i]**2+self.y[i]**2))
            temp_vx=self.vx[i]-4*math.pi**2*self.x[i]*self.r[i]**(-self.beta-1)*self.dt
            self.vx.append(temp_vx)
            temp_x=self.x[i]+self.vx[i+1]*self.dt
            temp_vy=self.vy[i]-4*math.pi**2*self.y[i]*self.r[i]**(-self.beta-1)*self.dt
            self.vy.append(temp_vy)
            temp_y=self.y[i]+self.vy[i+1]*self.dt
            self.x.append(temp_x)
            self.y.append(temp_y)
            self.t.append(self.t[i]+self.dt)
  
        return self.x,self.y
        
    def show_result(self):
        pl.plot(self.x,self.y,".")
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.title("Mercury,beita=2")
        pl.grid(True)
        pl.show()
                
I=initial(0.39,0.206,2.4*10**(23),2)
a=orbits(I[0],I[1],I[2],I[3],I[4])
a.calculate()
a.show_result()  
