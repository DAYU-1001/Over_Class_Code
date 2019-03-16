<%--
  Created by IntelliJ IDEA.
  User: HP
  Date: 2019/3/10
  Time: 16:58
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>index</title>
    <style type="text/css">
        <!--
        @import url(index.css);/*这里是通过@import引用CSS的样式内容*/
        -->
    </style>
</head>


<body>
<%--标题--%>
<div class="title">
    <%--校徽--%>
    <div class="logo"><a href="index.jsp"><img src="logo_sdnu.png" alt="SDNU LOGO" width="90px" height="90px"/></a></div>
    <%--名称--%>
    <div class="name" ><span style="color: black;font-size: larger">山东师范大学</span>&nbsp;
    <br><span style="color: gray";>计算智能创新实验团队</span></div>
    <div class="search"><input type="text" placeholder="请输入..." id="search" style="color: gray;height:40px;width: 250px;font-size: large;font-family: 等线;padding: 8px;margin-top: 16px;border-color: gainsboro;border-style:solid;border-width: 1px"></div>
</div>

<hr>

<%--目录栏--%>
<div class="cate_container">
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
    <div class="category" align="center"><a>标题哈哈</a></div>
</div>

<%--背景图--%>
<%--<div><img src="BG2018.jpg" width="100%"></div>--%>

<%--主体--%>
<div class="container" >
    <%--左边--%>
    <div class="left">
        <div class="left_1">title</div>
        <div class="left_2">hahahaha</div>
        <div class="left_1">title</div>
        <div class="left_2">hahahahahahaa</div>
    </div>

    <%--右边--%>
    <div class="right">
        <div class="left_1">title</div>
        <div class="right_2">hahahahaa</div>
        <div class="left_1">title</div>
        <div class="right_1">hahahahaa</div>
        <div class="left_1">title</div>
        <div class="right_1">hahahahaa</div>
    </div>
</div>


<%--管理员入口--%>
<%--<div class="container">--%>
<hr>
    <div class="bottom"><a href="manager_login.jsp">管理员入口</a>
    <%--</div>--%>

<%--</div>--%>
<hr>
</body></html>
