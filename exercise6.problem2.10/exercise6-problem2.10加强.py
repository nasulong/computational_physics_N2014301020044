
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:38:24 2016

@author: 龙
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:10:28 2016

@author: 龙
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 22:39:04 2016

@author: 龙
"""
import pylab as pl
import math
class  Trajectory_of_cannon:
    """
    Calculate the trajectory of the cannon shell including
    both air drag and the reduced air density at high altitudes.
    """
    def __init__(self,time_step=0.05,X=0,Y=0,initial_speed=700,initial_angel=30,a=0.0065,α=2.5,V_wind=-4.5):
        self.a=a
        self.α=α
        self.V_wind=V_wind               #逆向风速假定的-4.5m/s
        self.theta=initial_angel
        self.Vx=[math.cos(self.theta*math.pi/180)*initial_speed]
        self.Vy=[math.sin(self.theta*math.pi/180)*initial_speed]
        self.X=[0]
        self.Y=[0]
        self.dt=time_step
        self.t=[0]
        self.C=0.00004                   #C=B2/m=4*10^(-5)m-1
    def calculate(self):
        i=0
        while self.Y[i]>=0:                  #欧拉法计算轨迹，高度对空气密度影响采取的是书上的第一种等温模型
            a_drag_x=-self.C*(self.Vx[i]-self.V_wind)*math.sqrt(math.pow(self.Vx[i]-self.V_wind,2)+math.pow(self.Vy[i],2))
            #上式计算的是不考虑海拔情况下的x轴方向加速度
            a_drag_y=-self.C*(self.Vy[i])*math.sqrt(math.pow(self.Vx[i]-self.V_wind,2)+math.pow(self.Vy[i],2))
            #上式计算的是不考虑海拔情况下的y轴方向加速度
            altitude=math.pow(1-self.a*self.Y[i]/288,self.α)   #采用绝热模型ρ=ρ0（1-ay/T0)^α
            temp_X=self.X[i]+self.Vx[i]*self.dt
            temp_Y=self.Y[i]+self.Vy[i]*self.dt
            self.X.append(temp_X)
            self.Y.append(temp_Y)
            temp_Vx=self.Vx[i]+altitude*a_drag_x*self.dt  
            temp_Vy=self.Vy[i]-9.79*self.dt+altitude*a_drag_y*self.dt
            self.Vx.append(temp_Vx)
            self.Vy.append(temp_Vy)
            self.t.append(self.t[i]+self.dt)
            i+=1
    def show_result(self):      #图上显示结果，单位为米
        pl.plot(self.X,self.Y)
        pl.xlabel("X(m)")
        pl.ylabel("Y(m)")
        pl.xlim(0,30000)
        pl.ylim(0,20000)
        pl.show()


class  attack_target(Trajectory_of_cannon):      #扫描出符合精确度的曲线并打印出最精确的那条线的参数
    def attack(self):
        print("please insert the coordinate of the target x,y")
        self.x=float(input("please insert x:"))
        self.y=float(input("please insert y:"))
        accuracy=float(input("please insert accuracy:"))
        v=float(input("please insert initial speed:"))
        self.theta=0
        m=[]
        n=[]
        
        for j in range(901):
            c=Trajectory_of_cannon(initial_angel=self.theta,initial_speed=v)
            c.calculate()
            for i in range(len(c.X)):
                distance=math.sqrt(math.pow(c.X[i]-self.x,2)+math.pow(c.Y[i]-self.y,2))#精度是达到的点与目标的距离
                if distance <=accuracy:
                    m.append(distance)
                    n.append(self.theta)
                    
                    pl.plot(c.X,c.Y)
                    pl.xlabel("X(m)")
                    pl.ylabel("Y(m)")
                    pl.xlim(0,30000)
                    pl.ylim(0,20000)
                    pl.show()
                    break
                    
                    
                
            self.theta=self.theta+0.1
        for i in range(len(m)):
            if m[i]==min(m):
                I=i

        print(min(m),n[I])     #第一个数是精度，第二个数是曲线角度
        
d=attack_target()
d.attack()




                
                    
                    
                    
            
        
         
            
