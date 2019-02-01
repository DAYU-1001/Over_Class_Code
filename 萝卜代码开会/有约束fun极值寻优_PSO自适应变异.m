clc;
clear;

%约束：《MATLAB智能算法超级学习手册》p241  pdf-257
%0.072x1+0.063x2+0.057x3+0.05x4+0.032x5+0.0442x6+0.0675x7<=264.4
%128x1+78.1x2+64.1x3+43x4+58.1x5+36.9x6+50.5x7<=67919

%fun函数如下
%function y = fun( x )
%y=0.072*x(1)+0.063*x(2)+0.057*x(3)+0.05*x(4)+0.032*x(5)+0.0442*x(6)+0.0675*x(7)+7;

%%参数初始化
c1=1.49445;
c2=1.49445;
maxg=200;    %进化次数
sizepop=200;  %种群规模
Vmax=1;
Vmin=-1;
popmax=50;
popmin=-50;

%best_particle number
par_num=7;

%%产生初始粒子和速度
for i=1:sizepop
    pop(i,:)=1.*rands(1,par_num);    %初始位置
    V(i,:)=1.*rands(1,par_num);        %初始速度
    fitness(i)=fun(pop(i,:));%适应度
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
            k=ceil(par_num*rand);
            pop(j,k)=rand;
        end
        
        %适应度值
        if 0.072*pop(j,1)+0.063*pop(j,2)+0.057*pop(j,3)+0.05*pop(j,4)+0.032*pop(j,5)+0.0442*pop(j,6)+0.0675*pop(j,7)<=264.4
            if 128*pop(j,1)+78.1*pop(j,2)+64.1*pop(j,3)+43*pop(j,4)+58.1*pop(j,5)+36.9*pop(j,6)+50.5*pop(j,7)<=69719
                fitness(j)=fun(pop(j,:));
            end
        end

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

plot(result);
title('适应度曲线 ');
grid on
xlabel('进化代数');
ylabel('适应度');
