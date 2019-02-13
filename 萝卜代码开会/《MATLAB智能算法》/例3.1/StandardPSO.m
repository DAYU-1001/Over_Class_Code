%��MATLAB�������㷨����3-1��
clc;
clear all;

%��ʼ������
maxg=1000;%����������
c1=1.5;
c2=2.5;
w=0.5;%����Ȩ��
N=50;%��Ⱥ��ģ
D=30;%ά��

%��ʼ����ʼ��Ⱥ
%����ÿһ������λ�ú��ٶȣ�������fitness
for i=1:N
    x(i,:)=rands(1,D);
    V(i,:)=rands(1,D);
    fitness(i)=fun(x(i,:));
end

[bestfitness index]=min(fitness);
pBest=x;
gBest=x(index,:);

%��ʼ����
for i=1:maxg
    for j=1:N
        %���������ٶ�
        V(j,:)=w*V(j,:)+c1*rand*(pBest(j,:)-x(j,:))+c2*rand*(gBest-x(j,:));
        %��������λ��
        x(j,:)=x(j,:)+V(j,:);
        %������Ӧ��ֵ
        fitness(j)=fun(x(j,:));
    end
    for j=1:N
        %����ÿ��������ʷ����λ��
        if fitness(j)<fun(pBest(j,:))
            pBest(j,:)=x(j,:);
        end
    end
    %����ȫ������λ��
    if min(fitness)<bestfitness
        [bestfitness index]=min(fitness);
        gBest=x(index,:);
    end
    result(i)=bestfitness;
end
plot(result)
gBest









