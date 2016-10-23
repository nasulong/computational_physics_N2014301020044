#摘要
---
给定任意的坐标(x,y),得到在一定精度范围内能打到目标的炮弹曲线，并给出最接近的一条.   

#背景
----
* 采用绝热模型，考虑空气阻力的影响，考虑海拔的影响，其中空气阻力***F***drag=-B2V^2,海拔的影响是ρ=ρ0(1-ay/T0)^α,
* 考虑炮弹逆风飞行，***F***drag,x=-B2|V|(Vx-Vwind),***F***drag,y=-B2|V|(Vy),其中|V|为炮弹相对空气的速度的模。   
* 采用欧拉方法近似   

---

#正文
代码[exercise2.10](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise6.problem2.10/exercise6-problem2.10%E5%8A%A0%E5%BC%BA.py)

运行图见下   
![tu1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise6.problem2.10/%E8%BF%90%E8%A1%8C1.png)
![图2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise6.problem2.10/%E8%BF%90%E8%A1%8C2.png)

##举例
##我输入坐标(10000，10000)，初始速度为700m/s,精度取为100米(精度为击打点到目标的距离)，   
得到的几组曲线为![图3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise6.problem2.10/figure_1%E5%87%BB%E6%89%93%E4%BB%BB%E6%84%8F%E7%9B%AE%E6%A0%87.png)    
##曲线族交点即为目标打击点   
##最接近的一组曲线的精确度和角度为
![图4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise6.problem2.10/%E6%95%B0%E6%8D%AE.png)   

给定任一一点，求最小的打击速度，采取扫描速度的方式理论上可以得到   
但由于要保证较小的给定精度，扫描单位就要进可能小，以此带来的就是运算量的激增   
在原代码加上如下代码 
![图 4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise6.problem2.10/%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6.png)   

但由于运算量问题或程序问题，无法得出最小速度

---
#结论

* 主要采取扫描的方法得到能打到目标的曲线参数，gg   
* 给定任一坐标，利用本程序能实现精度内打击，有效性比较高。   
* 给定任一坐标，求最小的打击速度，可同样采取扫描速度的方式，但在要求精度条件下累积的运算量很大，所以不太实用，未展示


---
#致谢

* 计算物理section2.2和section2.3
* 蔡浩老师辛勤教导
