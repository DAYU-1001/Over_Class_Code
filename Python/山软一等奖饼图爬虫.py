import requests
import re
from collections import Counter
from pyecharts import Pie,Bar3D


#获取网页html
def GetHTML():
    url='https://www.softqilu.com/show-3-1920.htm'
    r=requests.get(url)
    r.encoding='utf-8'
    html=r.text
    return html

#清洗数据
def Clean(html):
    html=html.replace('\t','')
    html=html.replace('<span>','')
    html=html.replace('\r','')
    html=html.replace('</span>','')
    html=html.replace('\n','')
    html=html.replace('"','')
    return html


#统计各奖项人数
def GetNumber(school):
    #特等奖、一等奖、二等奖、三等奖、完成奖数目
    ranks=rank1=rank2=rank3=rankf=0
    rank=[]  #用列表储存各奖项获奖人数
    for i in range(len(school)):
        if school[i][1]=='特等奖':
            ranks+=1
        elif school[i][1]=='一等奖':
            rank1+=1
        elif school[i][1]=='二等奖':
            rank2+=1
        elif school[i][1]=='三等奖':
            rank3+=1
        elif school[i][1]=='完成奖':
            rankf+=1
    rank.append(ranks)
    rank.append(rank1)
    rank.append(rank2)
    rank.append(rank3)
    rank.append(rankf)
    return rank

def PaintPie(name,school,num):
    
    pie = Pie("山东软件大赛一等奖获奖学校统计-饼图", title_pos='center', width=900)
    pie.add(
        "山软一等奖获奖学校",
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

html=GetHTML()         #获取html
html=Clean(html)      #清洗数据
#获取学校名称&&奖项&&去掉标题项
school=re.findall(r'<td width=99>(.*?)</td>.*?<td width=77>(.*?)</td>',html)[1:]
rank=GetNumber(school)     #获取各奖项获奖数量

rank1_school=[]    #一等奖学校名称
rank1_num=[]       #一等奖对应数目

#一等奖学校列表
for i in range(rank[0],rank[0]+rank[1]):
    rank1_school.append(school[i][0])


#各学校获一等奖数量
rank1_sch_num=Counter(rank1_school)
rank1_sch_num=rank1_sch_num.most_common()
rank1_school=[]
#按学校次序的获一等奖次数
for i in range(len(rank1_sch_num)):
    rank1_num.append(rank1_sch_num[i][1])
    rank1_school.append(rank1_sch_num[i][0])


#绘制山东软件大赛一等奖获奖学校统计-饼图
PaintPie('山东软件大赛一等奖学校统计-饼图.html',rank1_school,rank1_num)








