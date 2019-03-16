package com.wry.jdbc;

import com.wry.jdbc.domain.User;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.PreparedStatement;
import java.sql.Statement;

public class TestJDBC {
//    String db_uname = null;
//    String db_pword = null;
//    public static void main(String[] args) {
//        //声明Connection对象
//        Connection con;
//        //驱动程序名
//        String driver = "com.mysql.jdbc.Driver";
//        //URL指向要访问的数据库名mydata
//        String url = "jdbc:mysql://localhost:3306/db_users";
//        //MySQL配置时的用户名
//        String user = "root";
//        //MySQL配置时的密码
//        String password = "123456";
//        //遍历查询结果集
//        try {
//            //加载驱动程序
//            Class.forName(driver);
//            //1.getConnection()方法，连接MySQL数据库！！
//            con = DriverManager.getConnection(url,user,password);
//            if(!con.isClosed())
//                System.out.println("Succeeded connecting to the Database!");
//            //2.创建statement类对象，用来执行SQL语句！！
//            Statement statement = con.createStatement();
//            //要执行的SQL语句
//            String sql = "select * from tb_users where username='admintest'";
//            //String sql = "insert into tb_users values('777777','456789')";
//            //String sql = "delete from tb_users where username='456789'";
//            //String sql = "update tb_users set password='000000' where username='456789'";
//
//            //3.ResultSet类，用来存放获取的结果集！！
//            ResultSet rs = statement.executeQuery(sql);
////            System.out.println("-----------------");
////            System.out.println("执行结果如下所示:");
////            System.out.println("-----------------");
////            System.out.println("姓名" + "\t" + "职称");
////            System.out.println("-----------------");
//
//
//            String db_uname = null;
//            String db_pword = null;
//            while(rs.next()){
//                //获取username这列数据
//                db_uname = rs.getString("username");
//                //获取password这列数据
//                db_pword = rs.getString("password");
//                //输出结果
//                System.out.println(db_uname + "\t" + db_pword);
//
//
//            }
//
//            rs.close();
//            con.close();
//        } catch(ClassNotFoundException e) {
//            //数据库驱动类异常处理
//            System.out.println("Sorry,can`t find the Driver!");
//            e.printStackTrace();
//        } catch(SQLException e) {
//            //数据库连接失败异常处理
//            e.printStackTrace();
//        }catch (Exception e) {
//            // TODO: handle exception
//            e.printStackTrace();
//        }finally{
//            System.out.println("数据库数据成功获取！！");
//        }
//    }

//    public String GetUname(){
//        return db_uname;
//    }
//    public String GetPword(){
//        return db_pword;
//    }

public User getInfo() throws Exception{
    //连接数据库
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db_users", "root", "123456");
    Statement st = conn.createStatement();
    //增删改查
    //String sql = "insert into tb_users values('777777','456789')";
    //String sql = "delete from tb_users where username='456789'";
    //String sql = "update tb_users set password='000000' where username='456789'";

    //查
    String sql = "select * from tb_users";


		int state = st.executeUpdate(sql);
//		if(state > 0){
//			System.out.println("执行成功");
//		}else{
//			System.out.println("执行失败");
//		}
    PreparedStatement pstmt = null;
//    ResultSet rs = null;
    ResultSet rs = st.executeQuery(sql);//rs返回的是一整个数据库吗？
    //Users users = null;

    User users = new User();

    while(rs.next()){

        String u = rs.getString("username");
        String p = rs.getString("password");

        users.setUsername(u);
        users.setPassword(p);

        //System.out.println("u="+u);
        //System.out.println("p="+p);
    }
    return users;
}
}
