#《智能优化方法》第四章问题与思考  P132
#2.工厂选址问题

#初始化
r=[9,8,4,5]    #四个工厂占地面积
p=[3,2,4,1]    #四个地点地价
P=70           #公司可用资金量
X=[1,3,2,4]    #初始解  工厂[角标]选在地点[位值]
T=[[]*4]*3     #禁忌表
neighbour=[[0]*4]*6    #邻域解  邻域大小为6
min_price=p[X[0]-1]*r[0]+p[X[1]-1]*r[1]+p[X[2]-1]*r[2]+p[X[3]-1]*r[3]

#求一个种子解的邻域函数
def SearchNeighbour(x):
    for count in range(6):
        neighbour[count]=x[:]
    #交换X两个工厂选址  邻域大小为6
    neighbour[0][0],neighbour[0][1]=neighbour[0][1],neighbour[0][0]
    neighbour[1][0],neighbour[1][2]=neighbour[1][2],neighbour[1][0]
    neighbour[2][0],neighbour[2][3]=neighbour[2][3],neighbour[2][0]
    neighbour[3][1],neighbour[3][2]=neighbour[3][2],neighbour[3][1]
    neighbour[4][1],neighbour[4][3]=neighbour[4][3],neighbour[4][1]
    neighbour[5][2],neighbour[5][3]=neighbour[5][3],neighbour[5][2]
   
p_list=[]
#计算每个规划总花费--得到与neighbour一一对应的p_list
def GetPrice():
    global p_list    #先清空
    p_list=[]
    for i in range(6):
        price=0
        for j in range(4):#四个工厂
            price+=r[j]*p[neighbour[i][j]-1]
        p_list.append(price)
    
    
Tcount=0
#寻找最优解
def Get_Min_Price():
    global Tcount,min_price
    #清洗掉买不起的组合  得到理论上可用的数据
    for i in range(6):
        if p_list[i]>P:
            p_list[i]=200    #200只是作为一个大数，没有实际意义
    
    for i in range(6):
        if neighbour[p_list.index(min(p_list))] not in T:    #如果邻域最小值不在禁忌表
            min_price=min(min_price,min(p_list))    #更新历史最值
            T[Tcount%3]=neighbour[p_list.index(min(p_list))][:]    #记录进入禁忌表
            Tcount+=1
            return neighbour[p_list.index(min(p_list))][:]
        else:    
            #如果最小值优于历史最小值,可无视禁忌,直接return
            if min(p_list)<=min_price:    
                min_price=min(p_list)
                T[Tcount%3]=neighbour(p_list.index(min(p_list)))[:]
                Tcount+=1
                return neighbour[p_list.index(min(p_list))][:]
            else:    #邻域最小值在禁忌表，且不优于历史最优值，取次优,接受劣解
                p_list[p_list.index(min(p_list))]=200

for i in range(5):
    if i==0:
        print("第1次迭代")
        SearchNeighbour(X)
        print(neighbour)
        GetPrice()
        print(p_list)
        good_x=Get_Min_Price()
        print(T)
        print(min_price)
    else:
        print("第",i+1,"次迭代")
        SearchNeighbour(good_x)
        print(neighbour)
        GetPrice()
        print(p_list)
        good_x=Get_Min_Price()
        print(T)
        print(min_price)
