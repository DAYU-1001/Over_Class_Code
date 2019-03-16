<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
	String path = request.getContextPath();

	String basePath = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
	<head>
		<base href="<%=basePath%>">

		<title>管理员登录页面</title>
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
	
	    <form action="doLogin.jsp">
	    
	    <br>
	    <br>
		<hr>
	    <br>
	    <br>
		<center>
			<table border="1" width="600" height="50">
				<tr>
					<td align="center"> 
						登录界面    
					</td>
					
					<%
                        String failState = (String)session.getAttribute("result");
                        if(failState == null){

                        }
                        else{
                            String fail = (String)session.getAttribute("result");
                            System.out.println("fail="+fail);


                    %>
                    <%=fail%>
                    <%
					         }
                    %>
					
					
				</tr>
				<tr>
					<td align="center">
						账号:<input type="text" value="admin" name="username" />
					</td>
					
				</tr>
				<tr>
					<td align="center">
						密码:<input type="password" value="123456" name="password" />
					</td>
					
				</tr>
				<tr>
					<td align="right">
						<input type="submit" value="登录">
					</td>
					
				</tr>
				
			</table>
		</center>
		</form>
	</body>
</html>
