# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-09 16:25

### MySQL数据库安装后的链接:
# 配置配置系统环境变量:   path = 安装目录/bin;
# 命令行终端链接本地数据库: mysql -u 用户名 -p  ---> 回车,然后输入密码
# 命令行终端链接远程数据库: mysql -h 远程ip地址 -u 用户名 -p   ---> 回车,然后输入密码
# 解决MySQL数据库中的乱码问题: default-character-set = utf8

### 使用命令行终端创建一个MySQL用户并授权:
# create user 用户名@localhost identified by '密码'; ---> localhost本地访问
# create user 用户名@% identified by '密码'; ---> %具有远程访问
# 使用命令行终端给创建的用户授权:
# grant all on 数据库名称.* to 用户名@%;

### MySQL数据库的导入导出:
# 使用命令行终端备份(导出)数据: mysqldump -u 用户名 -p 数据库名 > 本地目录位置\导出的文件名称.sql    ---> 回车,输入密码
# mysqldump -u root -p test > c:\test.sql
# 使用命令行终端恢复(导入)数据: mysql -u 用户名 -p 数据库名 < 本地目录位置\导入的文件名称.sql    ---> 回车,输入密码
# mysql -u root -p test < c:\test.sql
# 如果存在一个sql脚本文件,直接执行该文件
# source sql脚本文件路径



# 使用命令行终端进入数据库后的简单操作:
# 创建一个新的数据库:  create database 数据库名称;
# 查看所有数据库:  show databases;
# 进入其中的某个数据库:   use 数据库名称;
# 查看进入的数据库中的所有表:   show tables;


### SQL语言可以做什么?
# 数据库数据的增删改查(CRUD)
# 数据库对象的创建,修改和删除
# 用户权限/角色的授权与取消
# 事务控制

### SQL语言的分类:
# -DQL(数据查询语言): 如 select
# -DML(数据操作语言): 如 insert ,update ,delete
# -DDL(数据定义语言): 如 create ,alert ,drop
# -DCL(数据控制语言): 如 grant ,revoke
# -TCl(事务控制语言): 如 savepoint ,rollback ,set transaction ,commit

# ********************************************************************* #

### DDL(数据定义语言): 如 create(建库,建表),drop(删库,删表),alert(更改表结构)
# 创建数据库: create database 数据库名称;
# 删除数据库: drop database 数据库名称;
# 进入数据库: use 数据库名称;
# 查看当前选择的数据库: show databases;
# 查看当前数据库中的所有表: show tables;
# 创建表: create 表名(列名,类型);
# 如: create test_table(
#   id int auto_increment primary key,  # auto_increment:表示主键自动增长
#   tname varchar(20) not null
# );
# 查询表结构: desc 表名;
# 查看表的创建语句: show create table 表名;
# 修改表名: rename table 原表名 to 新表名;
# 修改表字段类型:  alert table 表名 add|change|drop 列名 类型;
# 给表添加新字段: alert table 表名 add 新加字段名称 新加字段类型;
# 如: alert table test_table add birthday datetime;
# 修改表中的字段: alert table 表名 change 要修改的字段名 修改后的字段名 修改后的字段类型;
# 如: alert table test_table change r_name d_name varchar(32);
# 删除表中的字段: alert table 表名 drop 要删除的字段名;
# 如: alert table test_table drop sex;
# 删除表: drop table 表名;

### DML(数据操纵语言): 如 insert,delete,update
## 插入数据:
# 所有字段插入数据:  insert into 表名 values(...);
# 插入某些字段数据: insert into 表名(列名1,列名2) values(值1,值2)
# 插入多条数据: insert into 表名 values(...)(...)...
## 修改字段的值: update 表名 set 列名1=值1,列名2=值2 where 条件;
# 如: update test_table set tname='zhangsan' where id = 2
## 删除所有数据: delete from 表名;
# 如: delete from test_table;
## 删除某些数据: delete from 表名 where 条件
# 如: delete from test_table where id = 2 ;

### DQL(数据查询语言): 如 select
## 查询一张表的所有数据: select * from 表名; ---> * 号表示该表的所有字段
# 如: select * from test_table;

## 查询一张表的某些字段数据: select 字段名1,字段名2 from 表名;
# 如: select id,tname from test_table;

## 给获取结果的列起别名:
# 如: select tname as 姓名 from test_table;
# 如: select tname 姓名 from test_table;

## 使用算术表达式: 比如表中一个员工工资字段sal,获取所有员工的年薪是多少
# 如: select tname,sal*12 from test_table;

## 使用distinct去掉重复的数据
# 如: select distinct 字段名 from 表名;

## 使用order by 对查询的结果进行排序: 默认是升序(asc),降序(desc)
# 如: select tname,sal from test_table order by sal     ---> 默认升序
# 如: select tname,sal from test_table order by sal desc    ---> 选择降序

## between ... and ... : 大于**** and 小于****(含有边界)
# select name,english from student where english>=80 and english<=90;
# select name,english from student where english between 80 and 90;

## in : 在集合中
# select name,math from student where math=89 or math=90 or math=91;
# select name,math from student where math in (89,90,91);

## like : 模糊查询     %:任意长度的任意字符串    _:任意的一个字符
# select * from student where name like '李%';
# select * from student where name like '__';

## limit : 分页查询
# select * from test_table limit 0,5    ---> 从第一条数据开始,取5条数据

## 聚合函数: count() ,max() ,min() ,sum() ,avg()
# count():表示求表中数据条数
# max(): 表示求某列的最大值
# min(): 表示求某列的最小值
# sum(): 表示求某列的和值
# avg(): 表示求某列的平均值

### MySQL数据库内置函数:
# concat(): 字符串链接   ---> select concat(tname,'的工资是:',sal) from test_table;
# left(str,len): 返回字符串左端的len个字符
# right(str,len): 返回字符串右端的len个字符
# substring(str,pos,len): 返回字符串str的pos位置开始的len个字符
# select substring("abc123",2,3)    ---> "c12"
# ltrim(str): 返回删左端空格的字符串
# rtrim(str): 返回删右端空格的字符串
## 把日期转换为字符串
# DATE_FORMAT("日期","格式")   ---> DATE_FORMAT(CURRENT_DATE(),"%Y年%m月%d日")


### SQL语句的执行顺序: from ---> where ---> group by ---> having ---> select ---> order by

### group by : 将表中数据分成若干组   ---> group by 跟在where语句后面,order by 不能写在group by 的前面
# 统计每个部门的平均工资
# select deptno, avg(sal) from emp group by deptno
# 注: 存在group by 分组,select 子句不能写group by 后面没有跟过的字段,除非这些字段用在了聚合函数中

### having: 过滤语句,只能出现在group by 分组的后面
# 统计每个部门的人数,平均工资,最高工资,但是部门的平均工资不能少于2000
# select deptno,count(1), avg(sal), max(sal) from emp group by deptno having avg(sal) > 2000;


### 索引的作用: 在数据库中用来加速对表的查询,通过使用快速路径访问方法快速定位数据,减少磁盘的I/O
# 索引创建以后,在用户撤销它之前并不会用到该索引的名字,但是索引在用户查询时会自动起作用

### 索引创建的两种情况:
# - 自动:当在表中定义了一个primary key 或 unique 约束条件时,数据库自动创建一个对应的唯一索引
# - 手动:用户可以创建索引以加速查询 如:
# create index 索引名称 on 表名(字段名称)

### 视图: 是一个虚拟的表,作用如下:
# 可以限制对数据的访问,可以给用户授予表的特定部分的访问权限而不是整个表的访问权限
# 可以使复杂的查询变得简单.在编写查询后,可以方便的重用它而不必知道它的基本查询细节
# 提供了对相同数据的不同显示

# 创建视图: create vive 视图名称 as 查询语句
# create vive v_emp as (select empno,ename,job from emp);


### 表连接: 内连接 与 外连接 ---> (两张表有连接关系如:一张表的主键与另张表的外键)
# 内连接:
# select table1.column, table2.column from table1, table2 where table1.column = table2.column
# select table1.column, table2.column from table1 inner join table2 on table1.column = table2.column
# 自连接:(一张表)
# select t1.column, t2.column from table as t1 join table as t2 on t1.column1 = t2.column2
# 外连接: 左外连接 与 右外连接 与 满外连接
# 左外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回左表中不满足条件的行
# select table1.column, table2.column from table1 left join table2 on table1.column = table2.column
# 右外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回右表中不满足条件的行
# select table1.column, table2.column from table1 right join table2 on table1.column = table2.column
# 满外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回两个表中不满足条件的所有行
# select table1.column, table2.column from table1 full join table2 on table1.column = table2.column


### 子查询:
# 子查询语法格式: select 字段列表 from table where 表达式 operator (select 字段列表 from table)
# 子查询特点: 子查询在主查询前执行一次,主查询使用子查询的结果
## 单行子查询: 返回的只有一记录
# 对单行子查询可使用单行记录比较运算符: 如: <, >, =, >=, <=, <>, !=
## 多行子查询:返回的有多条记录
# 对多行子查询只能使用多行记录比较运算符: 如:
# all 和 子查询返回的所有值比较
# any 和 子查询返回的任意值比较
# in 等于列表中的任何一个







