/**
 * Created by Administrator on 2015/5/12.
 */

import com.mysql.jdbc.*;
import com.mysql.jdbc.Driver;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.text.SimpleDateFormat;
import java.util.*;
import java.sql.*;
import java.util.Date;


public class ActiveUsers  {

    public ActiveUsers() {
    }

    public void getData() {
        String driver = "com.mysql.jdbc.Driver";
        String url79 = "jdbc:mysql://58.83.130.79:3308/skyhotel";
        String user79 = "query";
        String password79 = "qureybyno";


        String url89 = "jdbc:mysql://58.83.130.89:3306/gtgj";
        String user89 = "querynew" ;
        String password89 = "query1216" ;
        String yestoday =  "'" + this.getYestoday() + "'" ;

        try {
            Class.forName(driver);
//            Connection conn79 = DriverManager.getConnection(url79, user79, password79);
            Connection conn = DriverManager.getConnection(url89, user89, password89);
//            Connection conn = conn89;
            if (!conn.isClosed()) {
//                System.out.println("successed connectiong to the Database");

//                String sql = "select * from sys_user";
                String sql = "SELECT count(DISTINCT userid) num FROM user_statistics " +
                        "where DATE_FORMAT(end_time,'%Y%m%d')>=" + yestoday ;

                System.out.println(sql);

                Statement statement = conn.createStatement();
                ResultSet rs = statement.executeQuery(sql);

                String num = null;
                BufferedWriter bw = new BufferedWriter(new FileWriter("out.txt"));
                while (rs.next()) {
                    num = rs.getString("num");
                    bw.write(this.getYestoday() + "\n");
                    bw.write(num + "\n");
                    System.out.println(num);
                }
                bw.flush();
                bw.close();
//
                rs.close();
                conn.close();
            }
        } catch (ClassNotFoundException e) {
            System.out.println("Sorry,can`t find the Driver!");
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (java.io.IOException e){
            e.printStackTrace();
        }

    }

    public String getYestoday(){


        Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DATE,   -1);

        String yesterday = new SimpleDateFormat( "yyyyMMdd").format(cal.getTime());
        System.out.println(yesterday);
        return yesterday;

    }

    public static void main(String[] args){
        ActiveUsers object = new ActiveUsers();
        object.getYestoday();
        object.getData();
//        object.getData();
//        System.out.print("hello world!");
    }

}
