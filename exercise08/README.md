I am sorry for handing in my homework late.There are some thing wrong with my net and I failed to upload my homework.   

#1.Abstract   
###we have seen that at low driving forces the damped,nonlinear pendulum exhibits simple oscillatory motion,while at high drive it can be chaotic. This raises an obvious question :Exactly howdoes the transition fromsimple to chaotic behaviour take place?It tyrns out that
###the pendulum exhibits transitions to chaotic behaviour at several different values of the driving force. We will consider the behavior at somewhat higer driving forces and explore the transitions numerically.
###Many systems have been found to exhibit chaotic behaviour ,but there appear to be only a few ways in which the transitions from simple to chaotic can occur.The periodic-doubling scenario will be introduced next.   
* problem3.18 calculate the poincare section foor the pendulum as it undergoes the period-doubling route to chaos.Do this for FD=1.4,1.44,1.465   
* problem3.20 calculate the bifurcation diagram for the pendulum in the vicinity of FD=1.35~1.5

---
#2.Background    
###We have constructed some kind of poincare sections in problem3.12. We plotted points at times t≈2πn/Ω   
###The poincare section we got is ![1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/figure_3.12-1.png)    

---
#3.Body 

[the code of problem3.18](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/exercise08_problem3.18.py)
---
###If I don not remove the points corresponding to the initial transient , the pictures I got are(FD=1.4,1.44,1.465):   
![1](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/%E6%9C%AA%E5%91%BD%E5%90%8D.jpg)   
###However, if I remove the points corresponding to the initial transient the attractor in the pperiod-n regime will contain n discerte  points  .![2](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/300.jpg)    

[the code of problem 3.20](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/exercise08_problem3.20.py)   
---
###1.5-1.35=0.15 I divide it into 150 parts.I wait for 300 driving periods so that the initial transients haved decayed away   
###It takes some time to run the program ,but I got the picture finally:![3](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/3.20%E5%9B%BE.png)    

---
#4.Conclusion     
###problem3.18 if I remove the points corresponding to the initial transient the attractor in the pperiod-n regime will contain n discerte points    
###problem3.20.The picture I got shows that the periodic-doubling scenario we have observed with the pendulum is one of these few know routes to chaos.It also explains the 3.18   
###sorry that I have failed to install Vpython ,so i will use the gif:    
![4](https://github.com/nasulong/computational_physics_N2014301020044/blob/master/exercise08/%E5%8D%95%E6%91%86.gif)    

---
#4.Acknowledgement  
* Computational Physics (Second Edition), Nicholas J. Giordano, Hisao Nakanishi;
