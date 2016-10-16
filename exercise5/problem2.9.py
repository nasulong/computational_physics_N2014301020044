import pylab as pl
import math
class  Trajectory_of_cannon:
    """
    Calculate the trajectory of the cannon shell including
    both air drag and the reduced air density at high altitudes.
    """
    def __init__(self,time_step=0.05,X=0,Y=0,initial_speed=700,initial_angel=30):
        self.theta=initial_angel
        self.Vx=[math.cos(self.theta*math.pi/180)*700]
        self.Vy=[math.sin(self.theta*math.pi/180)*700]
        self.X=[0]
        self.Y=[0]
        self.dt=time_step
        self.t=[0]
    def calculate(self):
        i=0
        while self.Y[i]>=0:                  #欧拉法计算轨迹，高度对空气密度影响采取的是书上的第一种等温模型
            V=math.sqrt(math.pow(self.Vx[i],2)+math.pow(self.Vy[i],2))
            temp_X=self.X[i]+self.Vx[i]*self.dt
            temp_Y=self.Y[i]+self.Vy[i]*self.dt
            self.X.append(temp_X)
            self.Y.append(temp_Y)
            temp_Vx=self.Vx[i]-math.exp(-self.Y[i]/10000)*0.00004*V*self.Vx[i]*self.dt
            temp_Vy=self.Vy[i]-9.79*self.dt-math.exp(-self.Y[i]/10000)*0.00004*V*self.Vy[i]*self.dt
            self.Vx.append(temp_Vx)
            self.Vy.append(temp_Vy)
            self.t.append(self.t[i]+self.dt)
            i+=1
    def show_result(self):      #图上显示结果，单位为米
        pl.plot(self.X,self.Y)
        pl.xlabel("X(m)")
        pl.ylabel("Y(m)")
        pl.xlim(0,50000)
        pl.ylim(0,50000)
        pl.show()
    def landing_point(self):              #求着地点
       self.angel_point=dict()
       self.angel_point[self.theta]=self.X[-1]-self.Y[-1]*(self.X[-1]-self.X[-2])/(self.Y[-1]-self.Y[-2])
       print(self.angel_point)
a=Trajectory_of_cannon()      #运行
a.calculate()
a.show_result() 
a.landing_point() 

class Maximum_of_range(Trajectory_of_cannon):   #求解最大的距离
     def line_of_different_angel(self): 
         self.theta=0
         for i in range(91):
             b=Trajectory_of_cannon(initial_angel=self.theta) 
             b.calculate()
             b.show_result()
             b.landing_point()
             self.theta=self.theta+1
b=Maximum_of_range()
b.line_of_different_angel() 
         
            
