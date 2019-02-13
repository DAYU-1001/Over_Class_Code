%《MATLAB》智能算法【例3-1】
clc;
clear all;

%初始化参数
maxg=1000;%最大迭代次数
c1=1.5;
c2=2.5;
w=0.5;%惯性权重
N=50;%种群规模
D=30;%维度

%初始化初始种群
%计算每一个粒子位置和速度，并计算fitness
for i=1:N
    x(i,:)=rands(1,D);
    V(i,:)=rands(1,D);
    fitness(i)=fun(x(i,:));
end

[bestfitness index]=min(fitness);
pBest=x;
gBest=x(index,:);

%开始迭代
for i=1:maxg
    for j=1:N
        %更新粒子速度
        V(j,:)=w*V(j,:)+c1*rand*(pBest(j,:)-x(j,:))+c2*rand*(gBest-x(j,:));
        %更新粒子位置
        x(j,:)=x(j,:)+V(j,:);
        %计算适应度值
        fitness(j)=fun(x(j,:));
    end
    for j=1:N
        %更新每个粒子历史最优位置
        if fitness(j)<fun(pBest(j,:))
            pBest(j,:)=x(j,:);
        end
    end
    %更新全局最优位置
    if min(fitness)<bestfitness
        [bestfitness index]=min(fitness);
        gBest=x(index,:);
    end
    result(i)=bestfitness;
end
plot(result)
gBest









