import requests
import re
import time

#网址
for n in range(1,3):
    #网址 域名
    url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'
    #获取
    html = requests.get(url)
    #编码方式
    html.encoding = 'gb2312'
    #获取
    detail_list = re.findall('<a href="(.*?)" class="ulink">',html.text)
    for m in detail_list:
        url_2 = 'http://www.dytt8.net/'+ m 
        html_2 = requests.get(url_2)
        html_2.encoding = 'gb2312'
        ftp = re.findall('<a href=".*?">(.*?)</a></td>',html_2.text)[0]
        name = re.findall('<font color=#07519a>(.*?)</font></h1></div>',html_2.text)[0]
        with open(r'C:\Users\HP\Desktop\spider\dytt.txt','a',encoding='utf-8') as ff:
            ff.write(ftp+'\n')
        print(name)


        





