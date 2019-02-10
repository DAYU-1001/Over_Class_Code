import numpy as np
import random
import matplotlib.pyplot as plt

def fun(a,b):
    return (a**2+b**2)

#初始化
popsize=3
popmax=10
popmin=-10
Vmax=2
Vmin=-2
c1=2
c2=2
maxgen=1000

#初始化种群
pop=np.random.random((3,2))*20-10  #初始化种群位置
v=np.random.random((3,2))*4-2     #初始化种群速度

pBest=np.array([pop[0],pop[1],pop[2]])#初始个体最优值的设定

fitness=[[0]]*3           #存放个体fitness

for i in range(popsize):#每个粒子fitness
    fitness[i]=fun(pop[i][0],pop[i][1])

gBest=pop[fitness.index(min(fitness))]#将最小fitness粒子位置放入gBest
fitnesspbest=fitness[:]    #个体历史最优值
fitnessgbest=min(fitness)  #群体fitness最小值

result=[]
#迭代
for i in range(maxgen):
    #粒子速度位置更新
    for j in range(popsize):#速度更新
        v[j]=0.5*v[j]+c1*random.random()*(pBest[j]-pop[j])+c2*random.random()*(gBest-pop[j])
        #越界调整
        if v[j][0]>Vmax:
            v[j][0]=Vmax
        if v[j][1]>Vmax:
            v[j][1]=Vmax
        if v[j][0]<Vmin:
            v[j][0]=Vmin
        if v[j][1]<Vmin:
            v[j][1]=Vmin

    for j in range(popsize):#位置更新
        pop[j]=pop[j]+v[j]
        #越界调整
        if pop[j][0]>popmax:
            pop[j][0]=popmax
        if pop[j][1]>popmax:
            pop[j][1]=popmax
        if pop[j][0]<popmin:
            pop[j][0]=popmin
        if pop[j][1]<popmin:
            pop[j][1]=popmin


    for j in range(popsize):#更新适值
        fitness[j]=fun(pop[j][0],pop[j][1])

    for j in range(popsize):
        if fitness[j]<fitnesspbest[j]:
            pBest[j]=pop[j][:]
            fitnesspbest[j]=fitness[j]

        if fitness[j]<fitnessgbest:
            gBest=pop[j][:]
            fitnessgbest=fitness[j]
    result.append(fitnessgbest)

plt.plot(result)
plt.show()


