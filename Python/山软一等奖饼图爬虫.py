import requests
import re
from collections import Counter
from pyecharts import Pie,Bar3D


#��ȡ��ҳhtml
def GetHTML():
    url='https://www.softqilu.com/show-3-1920.htm'
    r=requests.get(url)
    r.encoding='utf-8'
    html=r.text
    return html

#��ϴ����
def Clean(html):
    html=html.replace('\t','')
    html=html.replace('<span>','')
    html=html.replace('\r','')
    html=html.replace('</span>','')
    html=html.replace('\n','')
    html=html.replace('"','')
    return html


#ͳ�Ƹ���������
def GetNumber(school):
    #�صȽ���һ�Ƚ������Ƚ������Ƚ�����ɽ���Ŀ
    ranks=rank1=rank2=rank3=rankf=0
    rank=[]  #���б�������������
    for i in range(len(school)):
        if school[i][1]=='�صȽ�':
            ranks+=1
        elif school[i][1]=='һ�Ƚ�':
            rank1+=1
        elif school[i][1]=='���Ƚ�':
            rank2+=1
        elif school[i][1]=='���Ƚ�':
            rank3+=1
        elif school[i][1]=='��ɽ�':
            rankf+=1
    rank.append(ranks)
    rank.append(rank1)
    rank.append(rank2)
    rank.append(rank3)
    rank.append(rankf)
    return rank

def PaintPie(name,school,num):
    
    pie = Pie("ɽ���������һ�Ƚ���ѧУͳ��-��ͼ", title_pos='center', width=900)
    pie.add(
        "ɽ��һ�Ƚ���ѧУ",
        school,
        num,
        center=[50, 50],
        is_random=True,
        radius=[30, 75],
        rosetype="area",
        is_legend_show=False,
        is_label_show=True,
    )
    pie.render(name)

#--------------------------------------main()--------------------------------------

html=GetHTML()         #��ȡhtml
html=Clean(html)      #��ϴ����
#��ȡѧУ����&&����&&ȥ��������
school=re.findall(r'<td width=99>(.*?)</td>.*?<td width=77>(.*?)</td>',html)[1:]
rank=GetNumber(school)     #��ȡ�����������

rank1_school=[]    #һ�Ƚ�ѧУ����
rank1_num=[]       #һ�Ƚ���Ӧ��Ŀ

#һ�Ƚ�ѧУ�б�
for i in range(rank[0],rank[0]+rank[1]):
    rank1_school.append(school[i][0])


#��ѧУ��һ�Ƚ�����
rank1_sch_num=Counter(rank1_school)
rank1_sch_num=rank1_sch_num.most_common()
rank1_school=[]
#��ѧУ����Ļ�һ�Ƚ�����
for i in range(len(rank1_sch_num)):
    rank1_num.append(rank1_sch_num[i][1])
    rank1_school.append(rank1_sch_num[i][0])


#����ɽ���������һ�Ƚ���ѧУͳ��-��ͼ
PaintPie('ɽ���������һ�Ƚ�ѧУͳ��-��ͼ.html',rank1_school,rank1_num)








