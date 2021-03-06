clc;
clear;

%%参数初始化
c1=1.49445;
c2=1.49445;
maxg=200;    %进化次数
sizepop=20;  %种群规模
Vmax=1;
Vmin=-1;
popmax=5;
popmin=-5;

%%产生初始粒子和速度
for i=1:sizepop
    pop(i,:)=5*rands(1,2);    %初始位置
    V(i,:)=rands(1,2);        %初始速度
    fitness(i)=Ackley(pop(i,:));%适应度
end

%寻找最优个体
[bestfitness bestindex]=min(fitness);
pBest=pop;                  %个体最佳
gBest=pop(bestindex,:);     %全局最佳
fitnesspbest=fitness;       %个体最佳适应度
fitnessgbest=bestfitness;   %全局最佳适应度

%%迭代寻优
for i=1:maxg
    for j=1:sizepop
        
        %速度更新
        V(j,:)=V(j,:)+c1*rand*(pBest(j,:)-pop(j,:))+c2*rand*(gBest-pop(j,:));
        V(j,find(V(j,:)>Vmax))=Vmax;
        V(j,find(V(j,:)<Vmin))=Vmin;
        
        %种群更新
        pop(j,:)=pop(j,:)+0.5*V(j,:);
        pop(j,find(pop(j,:)>popmax))=popmax;
        pop(j,find(pop(j,:)<popmin))=popmin;
        
        %自适应变异
        if rand>0.8
            k=ceil(2*rand);
            pop(j,k)=rand;
        end
        
        %适应度值
        fitness(j)=Ackley(pop(j,:));
    end
    for j=1:sizepop
        %个体最优更新
        if fitness(j)<fitnesspbest(j)
            pBest(j,:)=pop(j,:);
            fitnesspbest(j)=fitness(j);
        end
        
        %群体最优更新
        if fitness(j)<fitnessgbest
            gBest=pop(j,:);
            fitnessgbest=fitness(j);
        end
    end
    result(i)=fitnessgbest;
end

plot(result,'Linewidth',2)
title(['适应度曲线 ''终止代数=',num2str(maxg)]);
grid on
xlabel('进化代数');
ylabel('适应度');
