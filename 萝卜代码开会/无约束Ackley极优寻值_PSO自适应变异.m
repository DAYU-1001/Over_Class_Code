clc;
clear;

%%������ʼ��
c1=1.49445;
c2=1.49445;
maxg=200;    %��������
sizepop=20;  %��Ⱥ��ģ
Vmax=1;
Vmin=-1;
popmax=5;
popmin=-5;

%%������ʼ���Ӻ��ٶ�
for i=1:sizepop
    pop(i,:)=5*rands(1,2);    %��ʼλ��
    V(i,:)=rands(1,2);        %��ʼ�ٶ�
    fitness(i)=Ackley(pop(i,:));%��Ӧ��
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
            k=ceil(2*rand);
            pop(j,k)=rand;
        end
        
        %��Ӧ��ֵ
        fitness(j)=Ackley(pop(j,:));
    end
    for j=1:sizepop
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

plot(result,'Linewidth',2)
title(['��Ӧ������ ''��ֹ����=',num2str(maxg)]);
grid on
xlabel('��������');
ylabel('��Ӧ��');
