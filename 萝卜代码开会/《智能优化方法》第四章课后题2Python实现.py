#�������Ż�������������������˼��  P132
#2.����ѡַ����

#��ʼ��
r=[9,8,4,5]    #�ĸ�����ռ�����
p=[3,2,4,1]    #�ĸ��ص�ؼ�
P=70           #��˾�����ʽ���
X=[1,3,2,4]    #��ʼ��  ����[�Ǳ�]ѡ�ڵص�[λֵ]
T=[[]*4]*3     #���ɱ�
neighbour=[[0]*4]*6    #�����  �����СΪ6
min_price=p[X[0]-1]*r[0]+p[X[1]-1]*r[1]+p[X[2]-1]*r[2]+p[X[3]-1]*r[3]

#��һ�����ӽ��������
def SearchNeighbour(x):
    for count in range(6):
        neighbour[count]=x[:]
    #����X��������ѡַ  �����СΪ6
    neighbour[0][0],neighbour[0][1]=neighbour[0][1],neighbour[0][0]
    neighbour[1][0],neighbour[1][2]=neighbour[1][2],neighbour[1][0]
    neighbour[2][0],neighbour[2][3]=neighbour[2][3],neighbour[2][0]
    neighbour[3][1],neighbour[3][2]=neighbour[3][2],neighbour[3][1]
    neighbour[4][1],neighbour[4][3]=neighbour[4][3],neighbour[4][1]
    neighbour[5][2],neighbour[5][3]=neighbour[5][3],neighbour[5][2]
   
p_list=[]
#����ÿ���滮�ܻ���--�õ���neighbourһһ��Ӧ��p_list
def GetPrice():
    global p_list    #�����
    p_list=[]
    for i in range(6):
        price=0
        for j in range(4):#�ĸ�����
            price+=r[j]*p[neighbour[i][j]-1]
        p_list.append(price)
    
    
Tcount=0
#Ѱ�����Ž�
def Get_Min_Price():
    global Tcount,min_price
    #��ϴ����������  �õ������Ͽ��õ�����
    for i in range(6):
        if p_list[i]>P:
            p_list[i]=200    #200ֻ����Ϊһ��������û��ʵ������
    
    for i in range(6):
        if neighbour[p_list.index(min(p_list))] not in T:    #���������Сֵ���ڽ��ɱ�
            min_price=min(min_price,min(p_list))    #������ʷ��ֵ
            T[Tcount%3]=neighbour[p_list.index(min(p_list))][:]    #��¼������ɱ�
            Tcount+=1
            return neighbour[p_list.index(min(p_list))][:]
        else:    
            #�����Сֵ������ʷ��Сֵ,�����ӽ���,ֱ��return
            if min(p_list)<=min_price:    
                min_price=min(p_list)
                T[Tcount%3]=neighbour(p_list.index(min(p_list)))[:]
                Tcount+=1
                return neighbour[p_list.index(min(p_list))][:]
            else:    #������Сֵ�ڽ��ɱ��Ҳ�������ʷ����ֵ��ȡ����,�����ӽ�
                p_list[p_list.index(min(p_list))]=200

for i in range(5):
    if i==0:
        print("��1�ε���")
        SearchNeighbour(X)
        print(neighbour)
        GetPrice()
        print(p_list)
        good_x=Get_Min_Price()
        print(T)
        print(min_price)
    else:
        print("��",i+1,"�ε���")
        SearchNeighbour(good_x)
        print(neighbour)
        GetPrice()
        print(p_list)
        good_x=Get_Min_Price()
        print(T)
        print(min_price)
