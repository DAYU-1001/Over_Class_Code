import requests
import re
from collections import Counter
from pyecharts import Pie,Bar3D


#获取html文本
def GetHtml():
    url='https://www.softqilu.com/show-3-1920.htm'
    header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.5.0.17997'}
    r=requests.get(url,headers=header)
    r.encouding='utf-8'
    html=r.text
    return html

#清洗数据
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

#得到学校-奖项
def GetSchoolRank(html):
    school_rank=re.findall('<td width=99>(.*?)</td>.*?<td width=77>(.*?)</td>',html)
    return school_rank

#获取所有获奖（参与）学校名称，并统计次数
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
        if i[1]=='一等奖':
            rank1+=1
        elif i[1]=='二等奖':
            rank2+=1
        elif i[1]=='三等奖':
            rank3+=1
        elif i[1]=='完成奖':
            rankf+=1
    rank_num.append(3)
    rank_num.append(rank1)
    rank_num.append(rank2)
    rank_num.append(rank3)
    rank_num.append(rankf)

    return rank_num

#提取school num作为两个独立的列表
def GetList(school_num):
    school=[]
    num=[]
    for i in school_num:
        school.append(i[0])
        num.append(i[1])
    return school,num

#生成3D坐标x字典
def Create3DPointDic_x(school):
    dic_x={}
    x_axis=[]
    for i in range(len(school)):
        dic_x[school[i]]=i
        x_axis.append(school[i])
    
    return dic_x,x_axis




#获取3D柱状图的三维坐标列表
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

    











#绘制玫瑰饼图
def PaintRosePie(school,number,name):
    
    pie = Pie(name, title_pos='center', width=900)
    pie.add(
        "获奖情况",
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

#绘制3D柱状图
def Paint3DBar(points,x_axis,name):
    bar3d = Bar3D(name, width=1200, height=600)
    y_axis = ["一等奖", "二等奖", "三等奖", "完成奖"]
    
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add(
    "获奖情况",
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


html=GetHtml()     #获取html
html=Clean(html)        #清洗数据

all_school_rank=GetSchoolRank(html)[1:]      #得到学校-奖项的列表

#所有参赛学校各自获奖次数
all_school_num=SchoolCount(all_school_rank)     #得到所有参赛学校各自获奖次数--针对全部奖项
school,num=GetList(all_school_num)     #得到用于绘制的school和num列表
PaintRosePie(school,num,"山东软件大赛参赛学校获奖情况统计")      #绘制所有参赛学校各自获奖次数饼图

rank_num=GetEveryRankNum(all_school_rank)    #获取各奖段学校数



#一等奖
rank1_school_rank=all_school_rank[rank_num[0]:rank_num[0]+rank_num[1]]      #一等奖学校-奖项
rank1_school_num=SchoolCount(rank1_school_rank)          #一等奖学校获奖数及排序
rank1_school,rank1_num=GetList(rank1_school_num)
PaintRosePie(rank1_school,rank1_num,"山东软件大赛一等奖学校获奖情况统计")

#二等奖
rank2_school_rank=all_school_rank[rank_num[0]+rank_num[1]:rank_num[0]+rank_num[1]+rank_num[2]]      #二等奖学校-奖项
rank2_school_num=SchoolCount(rank2_school_rank)          #二等奖学校获奖数及排序
rank2_school,rank2_num=GetList(rank2_school_num)
PaintRosePie(rank2_school,rank2_num,"山东软件大赛二等奖学校获奖情况统计")

#三等奖
rank3_school_rank=all_school_rank[rank_num[0]+rank_num[1]+rank_num[2]:rank_num[0]+rank_num[1]+rank_num[2]+rank_num[3]]      #三等奖学校-奖项
rank3_school_num=SchoolCount(rank3_school_rank)          #三等奖学校获奖数及排序
rank3_school,rank3_num=GetList(rank3_school_num)
PaintRosePie(rank3_school,rank3_num,"山东软件大赛三等奖学校获奖情况统计")

#完成奖
rankf_school_rank=all_school_rank[-rank_num[4]:]      #完成奖学校-奖项
rankf_school_num=SchoolCount(rankf_school_rank)          #完成奖学校获奖数及排序
rankf_school,rankf_num=GetList(rankf_school_num)
PaintRosePie(rank3_school,rank3_num,"山东软件大赛完成奖学校获奖情况统计")


dic_x,x_axis = Create3DPointDic_x(school)
points1=Get3DList(rank1_school,rank1_num,dic_x,0)#一等奖点
points2=Get3DList(rank2_school,rank2_num,dic_x,1)#二等奖点
points3=Get3DList(rank3_school,rank3_num,dic_x,2)#三等奖点
pointsf=Get3DList(rankf_school,rankf_num,dic_x,3)#完成奖点

points=points1+points2+points3+pointsf

print(points)
Paint3DBar(points,x_axis,"山软获奖情况3DBar")