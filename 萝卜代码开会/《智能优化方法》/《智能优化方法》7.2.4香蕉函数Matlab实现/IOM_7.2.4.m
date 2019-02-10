%清空运行环境
clear
clc

%速度更新参数
c1=2;
c2=2;

maxgen=300;%迭代次数
popsize=5;%种群规模

%个体和速度最大最小值
popmax=30;popmin=-30;
Vmax=6;Vmin=-6;

%种群初始化
for i=1:popsize
    %随机产生一个种群
    pop(i,:)=10*rands(1,5);%初始化粒子
    V(i,:)=2*rands(1,5);%初始化速度
    
    %计算粒子适应度值
    fitness(i)=fun(pop(i,:));
end

%寻找初始极值
[bestfitness,bestindex]=min(fitness);
gBest=pop(bestindex,:);%群体极值位置
pBest=pop;
fitnesspbest=fitness;%个体极值适应度值
fitnessgbest=bestfitness;%群体极值适应度值

%迭代寻优
for i=1:maxgen
    %粒子位置和速度更新
    for j=1:popsize
        %速度更新
        V(j,:)=0.5*V(j,:)+c1*rand*(pBest(j,:)-pop(j,:))+c2*rand*(gBest-pop(j,:));
        V(j,find(V(j,:)>Vmax))=Vmax;%越界  合法性调整
        V(j,find(V(j,:)<Vmin))=Vmin;%合法性调整
        
        %粒子位置更新
        pop(j,:)=pop(j,:)+V(j,:);
        pop(j,find(pop(j,:)>popmax))=popmax;%越界调整
        pop(j,find(pop(j,:)<popmin))=popmin;

        %更新适应度
        fitness(j)=fun(pop(j,:));
    end
    
    %更新粒子个体最优和全局最优
    for j=1:popsize
        %个体值更新
        if fitness(j)<fitnesspbest(j)
            pBest(j,:)=pop(j,:);%记录位置
            fitnesspbest(j)=fitness(j);%记录适应度
        end
        %群体值更新
        if fitness(j)<fitnessgbest
            gbest=pop(j,:);%记录位置
            fitnessgbest=fitness(j);
        end
    end
    
    %每代最优值记录到yy中
    result(i)=fitnessgbest;
end

%画出每代最优个体适应度值
plot(result)
title('最优个体适应度值','fontsize',12);
xlabel('进化代数','fontsize',12);
ylabel('适应度值','fontsize',12);

            
        
    



