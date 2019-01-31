%������л���
clear
clc

%�ٶȸ��²���
c1=2;
c2=2;

maxgen=300;%��������
popsize=5;%��Ⱥ��ģ

%������ٶ������Сֵ
popmax=30;popmin=-30;
Vmax=6;Vmin=-6;

%��Ⱥ��ʼ��
for i=1:popsize
    %�������һ����Ⱥ
    pop(i,:)=10*rands(1,5);%��ʼ������
    V(i,:)=2*rands(1,5);%��ʼ���ٶ�
    
    %����������Ӧ��ֵ
    fitness(i)=fun(pop(i,:));
end

%Ѱ�ҳ�ʼ��ֵ
[bestfitness,bestindex]=min(fitness);
gBest=pop(bestindex,:);%Ⱥ�弫ֵλ��
pBest=pop;
fitnesspbest=fitness;%���弫ֵ��Ӧ��ֵ
fitnessgbest=bestfitness;%Ⱥ�弫ֵ��Ӧ��ֵ

%����Ѱ��
for i=1:maxgen
    %����λ�ú��ٶȸ���
    for j=1:popsize
        %�ٶȸ���
        V(j,:)=0.5*V(j,:)+c1*rand*(pBest(j,:)-pop(j,:))+c2*rand*(gBest-pop(j,:));
        V(j,find(V(j,:)>Vmax))=Vmax;%Խ��  �Ϸ��Ե���
        V(j,find(V(j,:)<Vmin))=Vmin;%�Ϸ��Ե���
        
        %����λ�ø���
        pop(j,:)=pop(j,:)+V(j,:);
        pop(j,find(pop(j,:)>popmax))=popmax;%Խ�����
        pop(j,find(pop(j,:)<popmin))=popmin;

        %������Ӧ��
        fitness(j)=fun(pop(j,:));
    end
    
    %�������Ӹ������ź�ȫ������
    for j=1:popsize
        %����ֵ����
        if fitness(j)<fitnesspbest(j)
            pBest(j,:)=pop(j,:);%��¼λ��
            fitnesspbest(j)=fitness(j);%��¼��Ӧ��
        end
        %Ⱥ��ֵ����
        if fitness(j)<fitnessgbest
            gbest=pop(j,:);%��¼λ��
            fitnessgbest=fitness(j);
        end
    end
    
    %ÿ������ֵ��¼��yy��
    result(i)=fitnessgbest;
end

%����ÿ�����Ÿ�����Ӧ��ֵ
plot(result)
title('���Ÿ�����Ӧ��ֵ','fontsize',12);
xlabel('��������','fontsize',12);
ylabel('��Ӧ��ֵ','fontsize',12);

            
        
    



