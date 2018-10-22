import requests,re,pymysql.cursors,time

id = 35696234
for n in range(0,1000):
    id+=1
    url = 'http://album.zhenai.com/u/'+str(id)
    html = requests.get(url)
    html.encoding = 'gbk'
    #print(html.text);
    state = re.findall('.bigbox_(.*?) .pag404 {',html.text)
    if (state):
        continue
    age = re.findall('<td><span class="label">年龄：</span>(.*?)</td>',html.text)[0]
    name = re.findall('<h1 class="ceiling-name ib fl fs24 lh32 blue">(.*?)</h1>',html.text)[0]
    gender = re.findall('<td><span class="label">性别：</span><span field="">(.*?)</span></td>',html.text)[0]
    height = re.findall('<td><span class="label">身高：</span>(.*?)</td>',html.text)[0]
    salary = re.findall('<td><span class="label">月收入：</span>(.*?)</td>',html.text)[0]
    marriage = re.findall('<td><span class="label">婚况：</span>(.*?)</td>',html.text)[0]
    school = re.findall('<td><span class="label">学历：</span>(.*?)</td>',html.text)[0]
    workAddress = re.findall('<td><span class="label">工作地：</span>(.*?)</td>',html.text)[0]
    home = re.findall('<td><span class="label">籍贯：</span>(.*?)</td>',html.text)[0]
    job = re.findall('<td><span class="label">职业： </span>(.*?)</td>',html.text)[0]
 
     # 连接MySQL数据库
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='test',charset='gbk', cursorclass=pymysql.cursors.DictCursor)

    # 通过cursor创建游标
    cursor = connection.cursor()
    sql = "INSERT INTO `python` (`user_id`, `name`, `gender`, `age`, `height`, `salary`, `marital`, `school`, `work`, `work_add`, `addresss`) VALUES ('"+str(id)+"', '"+str(name)+"','"+str(gender)+"','"+str(age)+"','"+str(height)+"','"+str(salary)+"','"+str(marriage)+"','"+str(school)+"','"+str(job)+"','"+str(workAddress)+"','"+str(home)+"')"
    cursor.execute(sql)

    # 提交SQL
    connection.commit()

    print(id)