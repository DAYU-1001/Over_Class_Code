import time
import requests
import re
import json
import xlwt

#数据
DATA = []

first_url ="https://s.taobao.com/search?q=X+box+one&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
html = requests.get(first_url).text
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss',html,re.S)[0][:-6]
content = json.loads(content)
data_list = content['mods']['itemlist']['data']['auctions']

for item in data_list:
    temp = {
        'title': item['title'],
        'price': item['view_price'],
        'fee' : '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'area' : item['item_loc'],
        'name': item['nick'],
        'url' : item['detail_url'],
        }
    DATA.append(temp)

#持久化
f = xlwt.Workbook(encoding='gb2312')
sheet01 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
#写标题
sheet01.write(0,0,'标题')
sheet01.write(0,1,'价格')
sheet01.write(0,2,'是否包邮')
sheet01.write(0,3,'是否天猫')
sheet01.write(0,4,'地区')
sheet01.write(0,5,'店名')
sheet01.write(0,6,'url')
#写内容
for i in range(len(DATA)):
    sheet01.write(i+1,0,DATA[i]['title'])
    sheet01.write(i+1,1,DATA[i]['price'])
    sheet01.write(i+1,2,DATA[i]['fee'])
    sheet01.write(i+1,3,DATA[i]['isTmall'])
    sheet01.write(i+1,4,DATA[i]['area'])
    sheet01.write(i+1,5,DATA[i]['name'])
    sheet01.write(i+1,6,DATA[i]['url'])
    print(DATA[i]['title'])

f.save('淘宝搜索.xls')
