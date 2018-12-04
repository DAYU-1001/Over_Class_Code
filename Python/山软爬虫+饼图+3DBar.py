import requests
import re
from collections import Counter
from pyecharts import Pie,Bar3D


#��ȡhtml�ı�
def GetHtml():
    url='https://www.softqilu.com/show-3-1920.htm'
    header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.5.0.17997'}
    r=requests.get(url,headers=header)
    r.encouding='utf-8'
    html=r.text
    return html

#��ϴ����
def Clean(html):
    html=html.replace('\t','')
    html=html.replace('\r','')
    html=html.replace('"','')
    html=html.replace('\n','')
    html=html.replace('<span>','')
    html=html.replace('</span>','')
    html=html.replace('<span style=white-space:normal;>','')
    html=html.replace('<br />','')
    return html

#�õ�ѧУ-����
def GetSchoolRank(html):
    school_rank=re.findall('<td width=99>(.*?)</td>.*?<td width=77>(.*?)</td>',html)
    return school_rank

#��ȡ���л񽱣����룩ѧУ���ƣ���ͳ�ƴ���
def SchoolCount(school_rank):
    school=[]
    for i in school_rank:
        school.append(i[0])

    school=Counter(school).most_common()
    return school

def GetEveryRankNum(all_school_rank):
    rank_num=[]
    rank1=rank2=rank3=rankf=0
    for i in all_school_rank:
        if i[1]=='һ�Ƚ�':
            rank1+=1
        elif i[1]=='���Ƚ�':
            rank2+=1
        elif i[1]=='���Ƚ�':
            rank3+=1
        elif i[1]=='��ɽ�':
            rankf+=1
    rank_num.append(3)
    rank_num.append(rank1)
    rank_num.append(rank2)
    rank_num.append(rank3)
    rank_num.append(rankf)

    return rank_num

#��ȡschool num��Ϊ�����������б�
def GetList(school_num):
    school=[]
    num=[]
    for i in school_num:
        school.append(i[0])
        num.append(i[1])
    return school,num

#����3D����x�ֵ�
def Create3DPointDic_x(school):
    dic_x={}
    x_axis=[]
    for i in range(len(school)):
        dic_x[school[i]]=i
        x_axis.append(school[i])
    
    return dic_x,x_axis




#��ȡ3D��״ͼ����ά�����б�
def Get3DList(school,num,dic_x,y):
    point=[]
    points=[]
    counter=0
    for i in school:
        point.append(dic_x[i])
        point.append(y)
        point.append(num[counter])
        counter+=1
        points.append(point)
        point=[]
        
    return points

    











#����õ���ͼ
def PaintRosePie(school,number,name):
    
    pie = Pie(name, title_pos='center', width=900)
    pie.add(
        "�����",
        school,
        number,
        center=[50, 50],
        is_random=True,
        radius=[30, 75],
        rosetype="area",
        is_legend_show=True,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )
    pie.render(name+'.html')

#����3D��״ͼ
def Paint3DBar(points,x_axis,name):
    bar3d = Bar3D(name, width=1200, height=600)
    y_axis = ["һ�Ƚ�", "���Ƚ�", "���Ƚ�", "��ɽ�"]
    
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add(
    "�����",
    x_axis,
    y_axis,
    [[d[0], d[1], d[2]] for d in points],
    is_visualmap=True,
    visual_range=[0, 20],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=80,
    grid3d_shading="lambert",
    )
    bar3d.render(name+'.html')



#---------------------------------main()------------------------------------


html=GetHtml()     #��ȡhtml
html=Clean(html)        #��ϴ����

all_school_rank=GetSchoolRank(html)[1:]      #�õ�ѧУ-������б�

#���в���ѧУ���Ի񽱴���
all_school_num=SchoolCount(all_school_rank)     #�õ����в���ѧУ���Ի񽱴���--���ȫ������
school,num=GetList(all_school_num)     #�õ����ڻ��Ƶ�school��num�б�
PaintRosePie(school,num,"ɽ�������������ѧУ�����ͳ��")      #�������в���ѧУ���Ի񽱴�����ͼ

rank_num=GetEveryRankNum(all_school_rank)    #��ȡ������ѧУ��



#һ�Ƚ�
rank1_school_rank=all_school_rank[rank_num[0]:rank_num[0]+rank_num[1]]      #һ�Ƚ�ѧУ-����
rank1_school_num=SchoolCount(rank1_school_rank)          #һ�Ƚ�ѧУ����������
rank1_school,rank1_num=GetList(rank1_school_num)
PaintRosePie(rank1_school,rank1_num,"ɽ���������һ�Ƚ�ѧУ�����ͳ��")

#���Ƚ�
rank2_school_rank=all_school_rank[rank_num[0]+rank_num[1]:rank_num[0]+rank_num[1]+rank_num[2]]      #���Ƚ�ѧУ-����
rank2_school_num=SchoolCount(rank2_school_rank)          #���Ƚ�ѧУ����������
rank2_school,rank2_num=GetList(rank2_school_num)
PaintRosePie(rank2_school,rank2_num,"ɽ������������Ƚ�ѧУ�����ͳ��")

#���Ƚ�
rank3_school_rank=all_school_rank[rank_num[0]+rank_num[1]+rank_num[2]:rank_num[0]+rank_num[1]+rank_num[2]+rank_num[3]]      #���Ƚ�ѧУ-����
rank3_school_num=SchoolCount(rank3_school_rank)          #���Ƚ�ѧУ����������
rank3_school,rank3_num=GetList(rank3_school_num)
PaintRosePie(rank3_school,rank3_num,"ɽ������������Ƚ�ѧУ�����ͳ��")

#��ɽ�
rankf_school_rank=all_school_rank[-rank_num[4]:]      #��ɽ�ѧУ-����
rankf_school_num=SchoolCount(rankf_school_rank)          #��ɽ�ѧУ����������
rankf_school,rankf_num=GetList(rankf_school_num)
PaintRosePie(rank3_school,rank3_num,"ɽ�����������ɽ�ѧУ�����ͳ��")


dic_x,x_axis = Create3DPointDic_x(school)
points1=Get3DList(rank1_school,rank1_num,dic_x,0)#һ�Ƚ���
points2=Get3DList(rank2_school,rank2_num,dic_x,1)#���Ƚ���
points3=Get3DList(rank3_school,rank3_num,dic_x,2)#���Ƚ���
pointsf=Get3DList(rankf_school,rankf_num,dic_x,3)#��ɽ���

points=points1+points2+points3+pointsf

print(points)
Paint3DBar(points,x_axis,"ɽ������3DBar")