clc;
clear;

%Լ������MATLAB�����㷨����ѧϰ�ֲᡷp241  pdf-257
%0.072x1+0.063x2+0.057x3+0.05x4+0.032x5+0.0442x6+0.0675x7<=264.4
%128x1+78.1x2+64.1x3+43x4+58.1x5+36.9x6+50.5x7<=67919

%fun��������
%function y = fun( x )
%y=0.072*x(1)+0.063*x(2)+0.057*x(3)+0.05*x(4)+0.032*x(5)+0.0442*x(6)+0.0675*x(7)+7;

%%������ʼ��
c1=1.49445;
c2=1.49445;
maxg=200;    %��������
sizepop=200;  %��Ⱥ��ģ
Vmax=1;
Vmin=-1;
popmax=50;
popmin=-50;

%best_particle number
par_num=7;

%%������ʼ���Ӻ��ٶ�
for i=1:sizepop
    pop(i,:)=1.*rands(1,par_num);    %��ʼλ��
    V(i,:)=1.*rands(1,par_num);        %��ʼ�ٶ�
    fitness(i)=fun(pop(i,:));%��Ӧ��
end

%Ѱ�����Ÿ���
[bestfitness bestindex]=min(fitness);
pBest=pop;                  %�������
gBest=pop(bestindex,:);     %ȫ�����
fitnesspbest=fitness;       %���������Ӧ��
fitnessgbest=bestfitness;   %ȫ�������Ӧ��

%%����Ѱ��
for i=1:maxg
    for j=1:sizepop
        
        %�ٶȸ���
        V(j,:)=V(j,:)+c1*rand*(pBest(j,:)-pop(j,:))+c2*rand*(gBest-pop(j,:));
        V(j,find(V(j,:)>Vmax))=Vmax;
        V(j,find(V(j,:)<Vmin))=Vmin;
        
        %��Ⱥ����
        pop(j,:)=pop(j,:)+0.5*V(j,:);
        pop(j,find(pop(j,:)>popmax))=popmax;
        pop(j,find(pop(j,:)<popmin))=popmin;
   
        %����Ӧ����
        if rand>0.8
            k=ceil(par_num*rand);
            pop(j,k)=rand;
        end
        
        %��Ӧ��ֵ
        if 0.072*pop(j,1)+0.063*pop(j,2)+0.057*pop(j,3)+0.05*pop(j,4)+0.032*pop(j,5)+0.0442*pop(j,6)+0.0675*pop(j,7)<=264.4
            if 128*pop(j,1)+78.1*pop(j,2)+64.1*pop(j,3)+43*pop(j,4)+58.1*pop(j,5)+36.9*pop(j,6)+50.5*pop(j,7)<=69719
                fitness(j)=fun(pop(j,:));
            end
        end

        %�������Ÿ���
        if fitness(j)<fitnesspbest(j)
            pBest(j,:)=pop(j,:);
            fitnesspbest(j)=fitness(j);
        end
        
        %Ⱥ�����Ÿ���
        if fitness(j)<fitnessgbest
            gBest=pop(j,:);
            fitnessgbest=fitness(j);
        end
    end
    result(i)=fitnessgbest;
end

plot(result);
title('��Ӧ������ ');
grid on
xlabel('��������');
ylabel('��Ӧ��');
