root账号登录，创建数据语句：
CREATE DATABASE IF NOT EXISTS interface_autotester DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

create table interface_api(
    api_id int not null AUTO_INCREMENT comment "自增长主键",
    api_name varchar(50) not null comment "接口的名字",
    file_name varchar(50) not null comment "接口对应的测试脚本名字",
    r_url varchar(50) not null comment "请求接口的URL",
    r_method varchar(10) not null comment "接口请求方式",
    p_type varchar(20) not null comment "传参方式",
    rely_db tinyint default 0 comment "是否依赖数据库",
    status tinyint default 0,
    ctime datetime,
    unique index(api_name),
    primary key(api_id)
)engine=InnoDB default charset=utf8;

删除列:
alter table interface_api drop column rely_db;

alter table interface_api add column rely_db tinyint defalut 0 after status;

insert into interface_api(api_name, r_url, r_method, p_type, status) values('用户注册','http://39.106.41.11:8080/register/','post','form',1)


create table interface_test_case(
    id int not null AUTO_INCREMENT comment "自增长主键",
    api_id int not null comment "对应interface_api的api_id",
    r_data varchar(255) comment "请求接口时传的参数",
    rely_data varchar(255) comment "用例依赖的数据",
    res_code int comment "接口期望响应code",
    res_data varchar(255) comment "接口响应body",
    data_store varchar(255) comment "依赖数据存储",
    check_point varchar(255) comment "接口响应校验依据数据",
    status tinyint default 0 comment "用例执行状态，0不执行，1执行",
    ctime datetime,
    primary key(id),
    index(api_id)
)engine=InnoDB default charset=utf8;

alter table interface_test_case add column mtime datetime after error_info;

insert into interface_test_case(api_id, r_data, res_code, data_store, check_point, status) values(1,'{"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}','00','{"request":["username","password"],"response":["code"]}','{"code":"00"}',1)

https://www.yiibai.com/mysql/foreign-key.html

{"request":["username","password"],"response":["code"]}

create table interface_data_store(
    api_id int not null comment "对应interface_api的api_id",
    case_id int not null comment "对应interface_test_case里面的id",
    data_store varchar(255) comment "存储的依赖数据",
    ctime datetime,
    index(api_id,case_id)
)engine=InnoDB default charset=utf8;

insert into interface_data_store values(1,1,'{"username":"wcx"}',"2018-07-27 12:21:20")