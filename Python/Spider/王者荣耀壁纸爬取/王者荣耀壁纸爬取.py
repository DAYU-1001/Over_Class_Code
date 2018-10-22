import requests
import json
with open(r'C:\Users\HP\Desktop\herolist.json','r',encoding='utf-8') as ff:
    jsonFile = json.load(ff)

heroNumber = len(jsonFile)

for m in range(heroNumber):#爬取全部请选择range(len(jsonFile))
    eName = jsonFile[m]['ename']
    cName = jsonFile[m]['cname']
    skinName = jsonFile[m]['skin_name'].split('|')
    skinNumber = len(skinName) 
    for n in range(1,skinNumber+1):
        #大图
        pictureUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(eName)+'/'+str(eName)+'-bigskin-'+str(n)+'.jpg'
        #小图
        #pictureUrl = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/'+str(eName)+'/'+str(eName)+'-smallskin-'+str(n)+'.jpg'
        picture = requests.request('get',pictureUrl).content
        with open('C:\\Users\\HP\\Desktop\\王者荣耀图片\\'+cName+'-'+skinName[n-1]+'.jpg','wb') as f:
            f.write(picture)
        print(cName+'-'+skinName[n-1])
   
