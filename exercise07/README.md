#摘要   
exercise07分三道题  
* problem3.12探究了选取不同的周期性时间点做出的庞加莱截面（poincare section）的区别
* problem3.13计算比较两个出了初始角度有0.001弧度区别，其他条件都相同的单摆运动区别，     
  做出了角度差dΘ随时间变化图 ，并估计Lyapunov exponent    
* problem3.14重复上个问题的，但现在初始角度相同，不同是阻尼系数q有细微不同，同样比较结果差别和Lyapunov exponent   

---

#背景   
程序所采用的模拟运算都是书中的euler_cromer_calculation   
即
![tu1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/%E5%85%AC%E5%BC%8F1.png)    
  ![图1'](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/%E5%85%AC%E5%BC%8F2.png)

#正文   
##problem3.12    
代码链接[problem3.12](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/exercise07_problem%203.12.py)  
![图2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-12-1%E4%BB%A3%E7%A0%81%E4%B8%8A%E5%8D%8A%E9%83%A8%E5%88%86.png)  
![图3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-12-1%E4%BB%A3%E7%A0%81%E4%B8%8B%E5%8D%8A%E9%83%A8%E5%88%86.png)    

上面写的代码还原了计算物理书上的FIGURE3.9 ，对于不同的周期时间点，如    
驱动力最大的时间点 和 驱动力快π/4的点，只需要改动部分程序    

![图4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-14-%E4%BB%A3%E7%A0%81%E6%94%B9%E5%8A%A8%E4%B8%8A.png)   
![图5](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-12-1%E4%BB%A3%E7%A0%81%E4%B8%8B%E5%8D%8A%E9%83%A8%E5%88%86.png)    

##三种情况的到的庞加莱截面点图见下     

![图6](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3.12-1.png)   
![图7](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3-12-2.png)   
![图8](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3-12-3.png)    

---   

##problem3.13   
代码链接[problem3.13](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/problem3.13.py)   
![13-1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-13-%E4%BB%A3%E7%A0%81%E4%B8%8A%E5%8D%8A%E9%83%A8%E5%88%86%E5%9B%BE.png)   
![13-2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-13-%E4%BB%A3%E7%A0%81%E4%B8%AD%E9%83%A8%E5%88%86%E5%9B%BE.png)   
![13-3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-13-%E4%BB%A3%E7%A0%81%E4%B8%8B%E5%8D%8A%E9%83%A8%E5%88%86%E5%9B%BE.png)      

由于dΘ随时间变化剧烈，所以作图时取不同横纵坐标范围，得到的结果如下     

![13-4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3.13-1.png)    

对于该开始dΘ很小时的情况为   

![13-5](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3.13-2.png)    

做出的log（dΘ）随时间的变化图为     

![13-6](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3.13-3.png)     
无法找到估计Lyapunov exponent 的方法    

---   

##problem3.14   
代码链接[problem3.14](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/exercise07-problem3.14.py)   
由于是承接3.13写的，只需让初始角度一样，但阻尼系数q相差0.001，绝大部分代码同上问   
只需要改动初始值和把后面两次引用的q值改为q1,q2    

![14-1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-14-%E4%BB%A3%E7%A0%81%E6%94%B9%E5%8A%A8%E4%B8%8A.png)    
![14-2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/3-14-%E4%BB%A3%E7%A0%81%E6%94%B9%E5%8A%A8%E4%B8%8B.png)    

所得到的角度差值随时间的变化图见下    

![14-3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3.14-1.png)    
![14-4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise07/figure_3-14-2.png)     

---    

#结论   
* problem3.12 改变选取的时间点，做出的图有较大区别，但跟据百度   
  当Poincare截面上只有一个不动点和少数离散点时，可判定运动是周期的;     
  当Poincare截面上是一封闭曲线时，可判定运动是准周期的;    
  当Poincare截面上是成片的密集点，且有层次结构时，可判定运动处于混沌状态  
  所取的点都判定运动处于混沌状态   
* problem3.13和problem3.14 初始角度或阻尼系数的极小变化，对以后运动产生的影响呈指数放大   
   并且他们的影响也有不同   但本人难以判断Lyapunov exponent（没理解）   

---   

#致谢   
* 计算物理课本    
* 百度百科     








