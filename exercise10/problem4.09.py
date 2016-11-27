# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:09:19 2016

@author: 文龙
"""
import pylab as pl
import math
def initial(a,e,MP):
    MS=2*10**(30)
    x0=a*(1+e)
    y0=0
    vx0=0
    vy0=2*math.pi*math.sqrt((1-e)/(a*(1+e))*(1+MP/MS))
    return [x0,y0,vx0,vy0]



class orbits():
    """
    beita=2.05,compare the behavior with different values of 
    the ellipticity of the orbits
    """

    def __init__(self,x0,y0,vx0,vy0):
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=0.001
        self.t=[0]
        self.steps=30000
        self.r=[]
    

    def calculate(self):
        for i in range(self.steps):
            self.r.append(math.sqrt(self.x[i]**2+self.y[i]**2))
            temp_vx=self.vx[i]-4*math.pi**2*self.x[i]*self.r[i]**(-3.05)*self.dt
            self.vx.append(temp_vx)
            temp_x=self.x[i]+self.vx[i+1]*self.dt
            temp_vy=self.vy[i]-4*math.pi**2*self.y[i]*self.r[i]**(-3.05)*self.dt
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
        pl.title('simulation of elliptical orbit')
        pl.xlim(-7,7)
        pl.ylim(-7,7)

        pl.show()
                


I_e=initial(1,0.017,6*10**(24))
e=orbits(I_e[0],I_e[1],I_e[2],8)
e.calculate()
e.show_result()






  
