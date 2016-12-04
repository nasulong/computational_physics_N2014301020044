# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 13:45:24 2016

@author: 文龙
"""
import pylab as pl
import math

def initial(a,e,MP):    #初始化初始的运动速度，使运动轨迹为椭圆
    MS=2*10**(30)
    x0=a*(1+e)
    y0=0
    vx0=0
    vy0=2*math.pi*math.sqrt((1-e)/(a*(1+e))*(1+MP/MS))
    return [x0,y0,vx0,vy0]



class three_body():
    """
    Simulation of the effect of Jupiter on three asteroids
    """

    def __init__(self,xe0,ye0,vex0,vey0,xj0,yj0,vjx0,vjy0):
        self.xe=[xe0]     #带字母e的表示是小行星的数据
        self.ye=[ye0]
        self.vex=[vex0]
        self.vey=[vey0]
        self.xj=[xj0]
        self.yj=[yj0]
        self.vjx=[vjx0]
        self.vjy=[vjy0]
        self.dt=0.005
        self.t=[0]
        self.steps=40000
        self.re=[]
        self.rj=[]
        self.rej=[]
        self.xs=[0]
        self.ys=[0]
        
    

    def calculate(self):
        MS=2*10**30
        MJ=1.9*10**27
        ME=0    #小行星相对于太阳质量可以忽略，Jupiter的运动可以考虑为不受小行星影响
        const1=4*math.pi**2*(MJ/MS)    #先把定值算出来，以后每次循环就不用再计算，加快运算速度
        const2=4*math.pi**2*(ME/MS)
        for i in range(self.steps):
            self.re.append(math.sqrt(self.xe[i]**2+self.ye[i]**2))
            self.rj.append(math.sqrt(self.xj[i]**2+self.yj[i]**2))
            self.rej.append(math.sqrt((self.xe[i]-self.xj[i])**2+(self.ye[i]-self.yj[i])**2))
            temp_vex=self.vex[i]-4*math.pi**2*self.xe[i]*self.re[i]**(-3)*self.dt-const1*(self.xe[i]-self.xj[i])*self.rej[i]**(-3)*self.dt
            self.vex.append(temp_vex)
            
            temp_vey=self.vey[i]-4*math.pi**2*self.ye[i]*self.re[i]**(-3)*self.dt-const1*(self.ye[i]-self.yj[i])*self.rej[i]**(-3)*self.dt
            self.vey.append(temp_vey)
            
            temp_vjx=self.vjx[i]-4*math.pi**2*self.xj[i]*self.rj[i]**(-3)*self.dt-const2*(self.xj[i]-self.xe[i])*self.rej[i]**(-3)*self.dt
            self.vjx.append(temp_vjx)
            
            temp_vjy=self.vjy[i]-4*math.pi**2*self.yj[i]*self.rj[i]**(-3)*self.dt-const2*(self.yj[i]-self.ye[i])*self.rej[i]**(-3)*self.dt
            self.vjy.append(temp_vjy)

            temp_xe=self.xe[i]+self.vex[i+1]*self.dt
            temp_ye=self.ye[i]+self.vey[i+1]*self.dt
            temp_xj=self.xj[i]+self.vjx[i+1]*self.dt
            temp_yj=self.yj[i]+self.vjy[i+1]*self.dt

            self.xe.append(temp_xe)
            self.ye.append(temp_ye)
            self.xj.append(temp_xj)
            self.yj.append(temp_yj)

            self.xs.append(0)   #太阳质量很大，假设为定点
            self.ys.append(0)
            
            self.t.append(self.t[i]+self.dt)
        
        return self.xe,self.ye,self.xj,self.yj,self.xs,self.ys        

    def show_result(self):
        pl.plot(self.xe,self.ye,".")
        pl.plot(self.xj,self.yj,"r")
        pl.plot(self.xs,self.ys,"b")
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        pl.xlim(-5.5,5.5)
        pl.ylim(-5.5,5.5)
        pl.grid(True)
        pl.title('Effect of jupiter on asteroiids')
        pl.show()
        
             


I_j=initial(5.2,0.048,1.9*10**(27))
v=three_body(3,0,0,3.628,I_j[0],I_j[1],I_j[2],I_j[3])
v.calculate()
v.show_result()

