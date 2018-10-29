#encoding=utf-8
import MySQLdb
from datetime import datetime

def test_data():
    conn = MySQLdb.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        passwd = "root",
        db = "interface_autotester",
        charset = "utf8"
    )
    cur = conn.cursor()
    conn.select_db('interface_autotester')
    cur.executemany("insert into interface_api(api_name, file_name,r_url, r_method, p_type, rely_db,status,ctime) value(%s,%s,%s,%s,%s,%s,%s,%s)",
            [("用户注册","user_registration","http://39.106.41.11:8080/register/","post","data",1,1,datetime.now()),
             ("用户登录","users_login","http://39.106.41.11:8080/login/","post","data",1,1,datetime.now())]
            )
    conn.commit()
    cur.executemany("insert into interface_test_case(api_id, r_data,rely_data,res_code, data_store, check_point, status,ctime) value(%s,%s,%s,%s,%s,%s,%s,%s)",
            [(1,'{"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}',"",200,'{"request":["username","password"],"response":["code"]}','{"code":"00"}',1,datetime.now()),
             (2,"{'username': 'wcx', 'password': 'wcx123wac'}",'{"1->1":["username","password"]}',200,'{"response":["userid", "token"]}','{"code": "00","username":{"R":"[a-zA-Z]+"}}',1,datetime.now())
             ]
            )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    test_data()