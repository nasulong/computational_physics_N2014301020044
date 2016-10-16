#摘要   
   计算以一定速度和角度发射的大炮的运动曲线，考虑两个因素：  
   1. 空气阻力；   
   2.空气密度随海拔高度变化。
   并由程序模拟算出哪个角度发射的大炮运动距离最远。    
   
----   
   #背景介绍
*   我们将空气阻力简单表示成***F***drag=-Bv^2  
*    空气密度随海拔变化为p= p0exp(-y/y0)   
     所以现在的 阻力变为***F*** drag=p/p0****F***drag(y=0)
*    课上已用欧拉方法模拟自行车运动问题和理想状态不受阻力情况下大炮运动轨迹。    
   
#正文    
作业链接[problem2.9](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise5/problem2.9.py)   
运行图见下
![图4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise5/%E8%BF%90%E8%A1%8C%E5%9B%BE.png)

我先试运行的初始角度为30度，得到的曲线如下![图1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise5/figure_of_angel%3D30.png)    
然后我从0度到90度循环运行基本的程序的到全部整角度的轨迹图![图2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise5/figure_of_different_angel.png)   
运行的角度和对应的坠地距离以字典形式显示，比较可知，以46度角 发射时可以得到最大距离，见图![图3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise5/list-of-angel%20and%20range.png)    


#结论   
   考虑空气阻力和海拔高度对空气密度影响时 ，以46度角发射炮弹射程最远.     
#致谢   
 谢谢老师课上教学指导
   
   
