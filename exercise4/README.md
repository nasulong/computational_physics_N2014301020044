#1.摘要   
计算物理书习题1.5，假设A，B两种粒子可以衰变成彼此，
衰变率为 dNA/dt=(NB-NA)/ι,dNB/dt=(NA-NB)/ι,初始条件为NA=100，NB=0，ι=1s,
通过程序展现系统最终达到稳定，NA和NB不变，且他们随时间的变化率为0.    

---
#2.背景介绍   
 课上学习了一种欧拉方法近似估计一种粒子的变化，
 泰勒展开近似N（δt）约等于N(0)+ dN*δt/dt    
 以此模拟两种粒子变化。   
 
 ---
#3.正文    
 * 运行程序代码 [problem1.5-untest-decay of A and B](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise4/exercise04-problem1.5-untest.py)   
 ##运行图如下   
 ![图1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise4/exercise04%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE.png)       
 
 
 ##模拟图如下
 ![图2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise4/decay%20of%20A%20and%20B%E6%9C%AA%E6%A3%80%E6%B5%8B%E5%9B%BE.png.png)   
 
 * 运用数学方法 算出的准确曲线与上述欧拉方法进行比较， 可以得到比较图   
    运行的完整代码为[problem1.5-test-decay of A and B](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise4/exercise4.problem1.5-test.py)   
 模拟图见下
 ![图3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise4/decay%20of%20A%20and%20B%E6%A3%80%E6%B5%8B%E5%9B%BE.png.png)   
*  实验获得的数据见[decay_of_nuclei A and B_data.txt](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise4/decay_of_nuclei%20A%20and%20B_data.txt)   
 
 
#4.结论   
  * 系统运行与预期相符，NA和NB最后都不变且不变，他们的变化率为0。   
  * 欧拉方法是一个比较好的近似方法。   


#5致谢    
   代码框架根据蔡老师所讲和 everynote上的教案Chapter 1 A First Numerical Problem而成，感谢！
