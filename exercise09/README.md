#1、摘要    
---
本次作业，我跟着计算物理书本的脚步模拟绘制了以下几种图：   
* 桌球在方形边界的运动轨迹，不同初始的条件运动出来的轨迹图形也大不一样，对都十分具有对称美     
* 桌球在stadium—shaped 桌子上运动的轨迹图形，不同初始条件，不同α值对图形都有很大影响，并有一定规律   
* 桌球在stadium-shaped 桌子上运动时的取不同α值的庞加莱相图，并有一定规律      
* 两个桌球在stadium-shaped 桌子上运动，初始时他们距离相差0.00001，其他条件一样，他们距离差随时间变化图，并探究不同α值对应   
  求出来的系数λ的变化    
---
#2、背景   
  我们已经探究了单摆的混沌运动，掌握了Euler算法的模拟方法   
  对于桌球的运动，我们了解的是它撞击边界后的反射角等于入射角，未撞击时它的运动方程是   
  ![1](http://p1.bqimg.com/567571/01ce22b74a90804c.png)   
  撞击后，平行于切面的速度大小不变，垂直于切面的速度方向取反，   
  原来的运动速度方程![2](http://p1.bqimg.com/567571/36e70bd5a761b01f.png)   
  撞击后的运动速度方程![3](http://p1.bqimg.com/567571/b413aeb4d43e7f59.png)    
---

#3、主体   
Question 3.30题目：   
Investigate the Lyapunov exponent of the stadium billiard for several values of α. You can do this qualitatively    
by examining the behavior for only one set of initial conditions for each value of α you consider,   
or more quantitatively by averaging over a range of initial conditions for each value of α    

* 桌球在方形边界的运动轨迹   代码：[trajectory of a billiard on a square table](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/trajectory%20of%20a%20billiard%20on%20a%20square%20table.py)   
  ##我取的初始的vx0=1,vy分别等于0.31,0.4，0.5,1，获得了各种不同的对称的图样      
  ![1-1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/vx0%3D1%2Cvy0%3D0.31.png)    
  ![1-2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/vx0%3D1%2Cvy0%3D0.4.png)
  ![1-3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/vx%3D1%2Cvy%3D0.5.png)
  ![1-4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/vx0%3D1%2Cvy0%3D1.png)
  ##图形都十分对称和谐，但不是每一种取值都能大致填满空间     

* 桌球在stadium—shaped 桌子上运动的轨迹图形   代码：[stadium_shaped table](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/stadium_shaped%20table.py)   
  ##我取了四个α值，分别为0,0.1,0.01,0.001，得到的图为   
  ![2-1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/circular%20stadium%20trajectory.png)   
  ![2-2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/stadium_shaped%20table%EF%BC%8C%CE%B1%3D0.1.png)   
  ![2-3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/stadium_shaped%20table%EF%BC%8C%CE%B1%3D0.01.png)   
  ![2-4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/stadium_shaped%20table%EF%BC%8C%CE%B1%3D0.001.png)   
  ##当α=0，即为圆形边界时，中心会有一个小圈空白，图形对称，取其他值时，α越大，图形不对称性越强，且中心的空白消失   

* 桌球在stadium-shaped 桌子上运动时的取不同α值的庞加莱相图    代码：[phase-space plotsfor stadium-shaped tables](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/phase-space%20plotsfor%20stadium-shaped%20tables.py)   
  ![3-1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/pahse-space%20plot%20%CE%B1%3D0.png)   
  ![3-2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/pahse-space%20plot%20%CE%B1%3D0.1.png)   
  ![3-3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/pahse-space%20plot%20%CE%B1%3D0.01.png)   
  ![3-4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/pahse-space%20plot%20%CE%B1%3D0.001.png)  

  ##可以看到，随着α变大，相图越来越杂乱，越来越混沌   

* 两个桌球在stadium-shaped 桌子上运动，初始时他们距离相差0.00001，其他条件一样，他们距离差随时间变化图，并探究不同α值对应   
  求出来的系数λ的变化    代码:[divergence of the trajectories](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/divergence%20of%20the%20trajectories.py)     
  ##初始坐标分别是（0.2，0）和（0.20001,0）最后他们的距离越来越远，体现了运动的混沌。α=0,0.1,0.01,0.001的图像分别为：   
  ![4-1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/separation%2C%CE%B1%3D0.png)   
  ![4-2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/separation%2C%CE%B1%3D0.1.png)   
  ![4-3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/separation%2C%CE%B1%3D0.01.png)   
  ![4-4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise09/separation%2C%CE%B1%3D0.001.png)   
  随着α变大，系数λ将变大，α等于0时，它为 0，α=0.001时，它也极小，α=0.01时，取了一系列峰值点用计算机线性拟合的到α大约等于0.02   

---
#4、结论    
* 桌球在方形边界的运动轨迹，不同初始的条件运动出来的轨迹图形也大不一样，对都十分具有对称美          
* 桌球在stadium—shaped 桌子上运动的轨迹图形，不同初始条件，不同α值对图形都有很大影响，并有，    
  当α=0，即为圆形边界时，中心会有一个小圈空白，图形对称，取其他值时，α越大，图形不对称性越强，且中心的空白消失      
* 桌球在stadium-shaped 桌子上运动时的取不同α值的庞加莱相图，并可以看到，随着α变大，相图越来越杂乱，越来越混沌    
* 两个桌球在stadium-shaped 桌子上运动，初始时他们距离相差0.00001，其他条件一样，他们距离差随时间变化图,随着α变大，系数λ将变大，    
  α等于0时，它为 0，α=0.001时，它也极小，α=0.01时，取了一系列峰值点用计算机线性拟合的到α大约等于0.02   
---      

#5、致谢       
* 计算物理   
* 谭善同学的一些语法格式   

