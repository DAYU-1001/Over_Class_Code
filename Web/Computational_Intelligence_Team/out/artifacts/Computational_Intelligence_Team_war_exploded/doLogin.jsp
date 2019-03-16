<%@ page language="java" import="java.util.*,java.sql.*,com.wry.jdbc.TestJDBC,com.wry.jdbc.domain.User" pageEncoding="UTF-8"%>
<%@ page import="com.wry.jdbc.dao.UsersDao" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'doLogin.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->

  </head>
  
  <body>
     <%
         //从JSP取值
         String u = request.getParameter("username");
         String p = request.getParameter("password");

//         匹配
         UsersDao usersDao = new UsersDao();
         User user = usersDao.find(u);
//         String uname = user.getUsername();


         if(user!=null){
             String passwd = user.getPassword();
             if(p.equals(passwd)){
                 String result = "登录成功";
                 session.setAttribute("state",result);
                 //页面跳转
                 request.getRequestDispatcher("/manager_page.jsp").forward(request,response);
             }else{
                 String result = "登录失败";
                 session.setAttribute("state",result);
//              request.setAttribute("state",result);
                 request.getRequestDispatcher("/manager_login.jsp").forward(request,response);
             }
         }else{
             request.getRequestDispatcher("/manager_login.jsp").forward(request,response);
         }



     %>
      
  </body>
</html>
