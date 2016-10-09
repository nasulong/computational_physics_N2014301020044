import pylab as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Nuclei of type A decay into ones of type B，while nuclei of type B decay 
    into ones of type A
    Program to accompany 'Computation Physics' by Cai Hao
    """
    def __init__(self,number_of_A=100,number_of_B=0,time_constant=1,time_of_duration=5,time_step=0.05):
        # unit of time is second
        self.na = [number_of_A]
        self.nb = [number_of_B]
        self.t=[0]
        self.tau=time_constant
        self.dt=time_step
        self.time=time_of_duration
        self.nsteps=int(time_of_duration//time_step+1)
        print("initial_number_of_uranium_A->",number_of_A)
        print("initial_number_of_uranium_B->",number_of_B)
        print("Time_constant->",time_constant)
        print("Time step->",time_step)
        print("total_time->",time_of_duration)
    def calcualtion(self):
        for i in range(self.nsteps):
            temp_A=self.na[i]+(self.nb[i]-self.na[i])/self.tau*self.dt
            temp_B=self.nb[i]+(self.na[i]-self.nb[i])/self.tau*self.dt
            self.na.append(temp_A)
            self.nb.append(temp_B)
            self.t.append(self.t[i]+self.dt)
    def show_result(self):
        pl.plot(self.t,self.na,"g")
        pl.plot(self.t,self.nb,"r")
        pl.xlabel('time ($s$)')
        pl.ylabel('Number')
        pl.xlim(0,self.time)
        pl.title('decay of two nuclei A and B')
        pl.show()
    def store_results(self):
        myfile = open('decay_of_nuclei A and B_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i],"   ", self.na[i],"  ",self.nb[i], file = myfile)
        myfile.close()
a=uranium_decay()
a.calcualtion()
a.show_result()
a.store_results()
