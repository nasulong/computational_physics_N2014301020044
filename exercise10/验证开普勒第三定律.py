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
    planetary motion program,calculate verify Kepler's third law
    """

    def __init__(self,x0,y0,vx0,vy0):
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=0.001
        self.t=[0]
        self.steps=300001
        self.r=[]
        self.x2=[]
        self.y2=[]
        self.t2=[]
        
    

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
            self.t.append(self.t[i]+self.dt)
            if self.y[i+1]<0:
                self.y2.append(self.y[i+1])
                self.x2.append(self.x[i+1])
                self.t2.append(self.t[i+1])
        a=(self.x[0]-self.x2[0])/2
        T=self.t2[0]*2
        print(a,T,T**2/a**3)
        
        return self.x,self.y,self.x2,self.y2
        

    def show_result(self):
        pl.plot(self.x,self.y,".")
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        pl.xlim(-1.5,1.5)
        pl.ylim(-1.5,1.5)
        pl.title('simulation of elliptical orbit')
        pl.show()
                


I_v=initial(0.72,0.007,4.9*10**(24))
v=orbits(I_v[0],I_v[1],I_v[2],I_v[3])
v.calculate()
v.show_result()

I_e=initial(1,0.017,6*10**(24))
e=orbits(I_e[0],I_e[1],I_e[2],I_e[3])
e.calculate()
e.show_result()


I_ma=initial(1.52,0.093,6.6*10**(23))
ma=orbits(I_ma[0],I_ma[1],I_ma[2],I_ma[3])
ma.calculate()
ma.show_result()

I_j=initial(5.2,0.048,1.9*10**(27))
j=orbits(I_j[0],I_j[1],I_j[2],I_j[3])
j.calculate()
j.show_result()

I_s=initial(9.54,0.056,5.7*10**(26))
s=orbits(I_s[0],I_s[1],I_s[2],I_s[3])
s.calculate()
s.show_result()





  
