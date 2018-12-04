import requests
import re
from collections import Counter



url='http://www.ischool.sdnu.edu.cn/index/xyxw.htm'
r=requests.get(url)
r.encoding='utf-8'
html=r.text
        
word=re.findall(r"\w+",html,re.I)
cntr=Counter(word)


print(cntr.most_common()[0:10])