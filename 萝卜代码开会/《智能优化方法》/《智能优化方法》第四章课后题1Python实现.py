#�������Ż�������������������˼��  P132
#1 ��������Ľ��������㷨
#�����������P77 ��3.4

#��ʼ��
p=[30,60,25,8,10,40,60]    #7���Ʊ��ļ�ֵ
w=[40,40,30,5,15,35,30]    #7���Ʊ�������
WEIGHT=120                 #��������
T=[[0]*7]*3                #���ɱ�

X=[1,0,0,0,1,1,1]          #��ʼ��/���ӽ�
neighbour=[[0]*7]*7        #���������

max_value=X[0]*p[0]+X[1]*p[1]+X[2]*p[2]+X[3]*p[3]+X[4]*p[4]+X[5]*p[5]+X[6]*p[6]  #���ݳ�ʼ�����
count=0    #���ɱ������

value_list=[]     #��neighbourһһ��Ӧ��¼value
weight_list=[]    #��neighbourһһ��Ӧ��¼weight

#������������  �õ�������value  weight��Ϣ
def Search_Neighbour(good_x):    #���һ�����ӽ�
    #ÿ��ѭ��Ѱ������һ����  ����ѭ�������õ�������value--weight--list
    for i in range(7):
        neighbour[i]=good_x[:]    #��ʼ����----��ֵ����ָ
        #�ı�λֵ
        if neighbour[i][i]==1:
            neighbour[i][i]=0;
        else:
            neighbour[i][i]=1
        
        #����value && weight
        value=weight=0
        for a in range(7):    #����������value-weight
            value+=p[a]*neighbour[i][a]
            weight+=w[a]*neighbour[i][a]

        value_list.append(value)
        weight_list.append(weight)
        print(neighbour[i])
        #����forѭ��ִ����ϣ��õ��������ӽ��value&weight -list�������һһ��Ӧ
    
    print("value:",value_list)
    print("weight:",weight_list)

#��ȡvalue����x����
def Get_Max_Value_x():
    global max_value,count
    #������ϴ,�޳����������������ۿ���
    for i in range(7):
        if weight_list[i]>120:
            value_list[i]=0
            weight_list[i]=0

    #ѭ��ֻ��Ϊ�����һ��else�����⴦��
    #���������ǰ����if�ɽ����ֱ��return�˳�ѭ��
    for i in range(7):
        if (neighbour[value_list.index(max(value_list))] not in T):    #������ֵ���ڽ��ɱ�ֱ�ӷ���
            max_value = max( max(value_list) , max_value )    #������ʷ��ֵ
            T[count%3]=neighbour[value_list.index(max(value_list))][:]
            count+=1
            return neighbour[value_list.index(max(value_list))][:]
        else:
            if max(value_list)>max_value:    #��Ȼ�ڽ��ɱ���������ʷ���Ž⣬ֱ�ӷ���
                max_value=max(value_list)
                T[count%3]=neighbour[value_list.index(max(value_list))][:]
                count+=1
                return neighbour[value_list.index(max(value_list))][:]
            else:    #�ڽ��ɱ���������ʷ���ţ������ƽ���Ѱ�Ҵ��Ž�----�����ӽ�
                weight_list[value_list.index(max(value_list))]=0
                value_list[value_list.index(max(value_list))]=0
                #����ѭ��������Ѱ��

for i in range(5):
    #��һ�ε���
    if i==0:
        print("��һ�ε���")
        Search_Neighbour(X)
        good_x=Get_Max_Value_x()
        print("��ʷ���ֵΪ��",max_value)
        print(T)
    else:
        print("��",i+1,"�ε���")
        value_list=[]
        weight_list=[]
        Search_Neighbour(good_x)
        good_x=Get_Max_Value_x()
        print(max_value)
        print(T)
print(max_value)