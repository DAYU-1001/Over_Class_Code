import requests
import re
import time
#该爬虫爬取的是 →微博移动端←
#微博移动端网址：https://passport.weibo.cn/signin/welcome?entry=mweibo&r=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fm.weibo.cn%2F
#我用的是火狐浏览器，开发者工具对json格式文件支持比较好，谁用谁知道
#此代码爬取的是指定微博下热门评论，这里以鹿晗某条微博进行测试



ID = '4259924962078947'
for m in range(0,4):  #这里***替换为想爬取的网页数，一个网页包含8—10条评论信息
    if m ==0:

        #第一页和其他页排版不一样，单独列出
        ##ID从地址栏寻找
        
        url = 'https://m.weibo.cn/single/rcList?format=cards&id='+str(ID)+'&type=comment&hot=1&page=1'
        html = requests.get(url)
        html.json()
        for i in range(len(html.json()[1]['card_group'])):
            comment = html.json()[1]['card_group'][i]['text']
            userName = html.json()[1]['card_group'][i]['user']['screen_name']

            #清洗数据
            useLess1 = re.findall('<a href="(.*?)">',comment)
            useLess2 = re.findall('<a href=\"/n/(.*?)">',comment)
            comment = comment.replace(str(useLess1),'')
            comment = comment.replace(str(useLess2),'')
            comment = comment.replace('<a href="">','')
            comment = comment.replace('<a href=\"/n/">','')
            comment = comment.replace('<a href="/n/'+'userName'+'">','')
            comment = comment.replace('</a>','')
            comment = comment.replace('<a href="/n/">','')
            comment = comment.replace('</i>','')

            #open里为文件存储地址，请更改为目标路径
            #注意两个反斜杠（\\）的转义表示单反斜杠（\）
            #with open('C:\\Users\\HP\\Desktop\\微博评论\\sinaComment.txt','a',encoding = 'utf-8') as ff:
            
                #ff.write(userName+':'+comment+'\n')
            #time.sleep(2)表示间隔两秒再爬取，避免对网站造成过大压力
            time.sleep(0.5)

            print("第1页第%d组数据爬取完毕"%(i+1))
            print(userName+':'+comment+'\n')
            #print(comment+'\n')

    else:
        url = 'https://m.weibo.cn/single/rcList?format=cards&id='+str(ID)+'&type=comment&hot=1&page='+str(m+1)
        html = requests.get(url)
        html.json()
        for i in range(len(html.json()[0]['card_group'])):
            comment = html.json()[0]['card_group'][i]['text']
            userName = html.json()[0]['card_group'][i]['user']['screen_name']
            #清洗数据
            useLess1 = re.findall(r'<a href="(.*?)">',comment)
            useLess2 = re.findall(r'<a href=\"/n/(.*?)">',comment)
            
            comment = comment.replace(str(useLess1),'')
            comment = comment.replace(str(useLess2),'')
            comment = comment.replace('<a href="/n/">','')
            comment = comment.replace('<a href="">','')
            comment = comment.replace('<a href=\"/n/">','')
            comment = comment.replace('<i class="face face_','[表情]')
            comment = comment.replace('icon_','-')
            comment = comment.replace('<a href="/n/'+str(useLess2)+'">','-')
            #文件地址更改同上
            #with open('C:\\Users\\HP\\Desktop\\微博评论\\sinaComment.txt','a',encoding = 'utf-8') as ff:
        
                #ff.write(userName+':'+comment+'\n')
            time.sleep(0.5)
            print("第%d页第%d组数据爬取完毕"%(m+1,i+1))
            print(userName+':'+comment+'\n')
            #print(comment+'\n')
            #print(comment)