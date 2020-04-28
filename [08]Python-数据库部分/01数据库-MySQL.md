### SQL语言的分为四大类:
- DQL(数据查询语言): 如 select
- DML(数据操作语言): 如 insert,update,delete
- DDL(数据定义语言): 如 create,alert,drop
- DCL(数据控制语言): 如 grant,revoke

### 终端命令行链接数据库:
> 本地链接: mysql -u用户名 -p密码  
> 远程链接: mysql -h主机IP地址 -u用户名 -p密码  
> 断开与数据库链接: exit; quit; \q;

### 数据库数据的导入导出:
> 终端命令行导出: mysqldump -u用户名 -p 数据库名 > 本地目录位置\导出的文件名称.sql  
> 终端命令行导入: mysql -u用户名 -p 数据库名 < 本地目录位置\导入的文件名称.sql  
> SQL脚本文件导入: source SQL脚本文件路径 

### 数据库用户授权管理:
- 创建用户: create user "用户名"@"localhost" identified by "密码";
- 注: localhost表示本地访问;% 表示可远程访问
    > CREATE USER 'myuser'@'localhost' IDENTIFIED BY '123456';  
    CREATE USER 'myuser'@'172.20.0.0' IDENDIFIED BY '123456';  
    CREATE USER 'myuser'@'%' IDENTIFIED BY '123456'; 
- 用户授权: grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option; 
- 注: 权限列表(all、privileges),库.表(\*.*): *表示所有库的所有表
    > GRANT privileges ON maindataplus.* TO 'myuser'@'%';  
    GRANT all ON \*.\* TO 'myuser'@'%' WITH GRANT OPTION;
    
### 数据库的基本操作
- 创建数据库(并指定字符集): `create database 数据库名称 character set utf8;`
- 进入/切换数据库: `use 数据库名称;`
- 查看已有数据库: `show databases;`
- 查看创建库的语句: `show create database 数据库名称;`
- 查看当前所在数据库: `select database();`
- 查看数据库中已有表: `show tables;`
- 删除数据库: `drop database 数据库名称;`

### 表的基本操作:
- 创建表: create table 表名(
       	字段名 数据类型,
       	字段名 数据类型,
       	...
       	字段名 数据类型
       	)default charset='utf8';
- 查看表结构: desc 表名;
- 删除表: drop table 表名; drop table 表名1,表名2,表名3;
- 修改表名称: rename table 原表名 to 新表名;
- 查看表的创建语句: show create table 表名;

### 数据库聚合函数:
- avg(字段名): 求该字段平均值
- sum(字段名): 求和
- max(字段名): 最大值
- min(字段名): 最小值
- count(字段名): 统计该字段记录的个数

### 数据库内置函数:
- concat(): 字符串链接  ---> select concat(tname,'的工资是:',sal) from test_table;
- left(str,len): 返回字符串左端的len个字符
- right(str,len): 返回字符串右端的len个字符
- substring(str,pos,len): 返回字符串str的pos位置开始的len个字符
- select substring("abc123",2,3)  ---> "c12"
- ltrim(str): 返回删左端空格的字符串
- rtrim(str): 返回删右端空格的字符串
- 把日期转换为字符串:
    > DATE_FORMAT("日期","格式")  ---> DATE_FORMAT(CURRENT_DATE(),"%Y年%m月%d日")

### 表字段操作: add change drop
- **添加字段(add)**
    - alter table 表名 add 字段名 数据类型;    
    - alter table 表名 add 字段名 数据类型 first;  
    - alter table 表名 add 字段名 数据类型 after 字段名;  
      > alert table test_table add birthday datetime;
- **修改字段名(change)**
    - alter table 表名 change 老字段名 新字段名 新数据类型;
        > alert table test_table change r_name d_name varchar(32);
- **删除字段(drop)**
    - alter table 表名 drop 字段名;
        > alert table test_table drop sex;

### 表数据操作(增删改): DML
- **插入(insert)**
    - 插入某些字段数据: insert into 表名(字段1,字段2,...) values(值1,值2,...);
    - 插入所有字段一条数据: insert into 表名 values(值1,值2,...)
    - 插入所有字段多条数据: insert into 表名 values(值1,值2,...),(值11,值22,...);
- **删除(delete)**
    - delete from 表名 where 条件;  `delete语句后如果不加where条件,所有记录全部清空`
        > delete from 表名;  
        delete from test_table where id = 2;
- **更新(update)**
    - update 表名 set 字段1=值1,字段2=值2,... where 条件;  `必须加where条件`
        > update test_table set tname='zhangsan' where id = 2;
- **查询(select)**
    - select * from 表名 [where 条件];
    - select 字段1,字段名2 from 表名 [where 条件];

### 数据库运算符操作:
- **数值比较/字符比较**
    - 数值比较: = != > >= < <=  
    - 字符比较: = !=  
- **逻辑比较(and 和 or)**
    - and (两个或多个条件同时成立)
    - or (任意一个条件成立即可)
- **范围内比较**
    - between 值1 and 值2;
    - where 字段名 in(值1,值2,...);
    - where 字段名 not in(值1,值2,...);
- **匹配空、非空**
    - 空: where name is null;
    - 非空: where name is not null;
    - 注意: 
        > NULL: 空值,只能用 is 或者 is not 去匹配
        > "": 空字符串,用 = 或者 != 去匹配
- **模糊比较**
    - where 字段名 like 表达式;
    - 表达式: _: 匹配单个字符, %: 匹配0到多个字符

### 表数据操作(查): DQL
- **执行顺序(select ...聚合函数 from 表名)**
    - where ...
    - group by ...
    - having ...
    - order by ...
    - limit ...
- **group by**
    - 作用: 给查询结果进行分组
    - 注意: group by之后的字段名必须要为select之后的字段名,如果select之后的字段名和group by之后的字段不一致,则必须对该字段进行聚合处理(聚合函数)
- **having**
    - 作用: 对查询的结果进行进一步筛选
    - 注意: having语句通常和group by语句联合使用,过滤由group by语句返回的记录集,where只能操作表中实际存在字段,having可操作由聚合函数生成的显示列
- **distinct** 
    - 作用: 不显示字段重复值
    - 注意: distinct和from之间所有字段都相同才会去重,distinct不能对任何字段做聚合处理
- **order by**
    - 作用: 给查询结果进行排序
    - 表达式: order by 字段名 ASC(默认升序)/DESC(降序)
- **limit(永远放在SQL语句的最后写)**  
    - 作用: 限制显示查询记录的个数
    - 语法: 
        > limit n           ---> 显示 n 条记录  
        limit m,n         ---> m 表示从第m+1条记录开始显示,显示 n 条  
        limit(m-1)*n,n    ---> 分页显示: 每页显示n条记录,显示第m页  

### 表数据查询示例:
```
# 查询一张表的所有数据: select * from 表名;
注: *号表示该表的所有字段
如: select * from test_table;

# 查询一张表的某些字段数据: select 字段名1,字段名2 from 表名;
如: select id,tname from test_table;

# 给获取结果的列起别名: as
如: select tname as 姓名 from test_table;
如: select tname 姓名 from test_table;

# 使用算术表达式: 比如表中一个员工工资字段sal,获取所有员工的年薪是多少
如: select tname,sal*12 from test_table;

# 使用distinct去掉重复的数据
如: select distinct 字段名 from 表名;

# 使用order by对查询的结果进行排序: 默认是升序(asc),降序(desc)
如: select tname,sal from test_table order by sal     ---> 默认升序
如: select tname,sal from test_table order by sal desc    ---> 选择降序

# between ... and ...: 大于**** and 小于****(含有边界)
如: select name,english from student where english>=80 and english<=90;
如: select name,english from student where english between 80 and 90;

# or: 或
如: select name,math from student where math=89 or math=90 or math=91;

# in: 在集合中
如: select name,math from student where math in (89,90,91);

# like: 模糊查询     
注: %表示任意长度的任意字符串   _:表示任意的一个字符
如: select * from student where name like '李%';
如: select * from student where name like '__';

# limit:  分页查询, 从第一条数据开始,取5条数据
如: select * from test_table limit 0,5;

```

### 表连接查询: 
- 自连接查询(一张表):
    > select t1.column, t2.column from table as t1 join table as t2 on t1.column1 = t2.column2 
- 注: 内连接与外连接(两张表有连接关系如:一张表的主键与另张表的外键)
- **内连接查询**:  inner join ... on 
    > 示例: select table1.column, table2.column from table1, table2 where table1.column = table2.column;  
    select table1.column, table2.column from table1 inner join table2 on table1.column = table2.column
- **外连接查询**: 左外连接 与 右外连接 与 满外连接
    - 左外连接: 两个表在连接过程中除返回满足连接条件的行以外,还返回左表中不满足条件的行
        > select table1.column, table2.column from table1 left join table2 on table1.column = table2.column
    - 右外连接: 两个表在连接过程中除返回满足连接条件的行以外,还返回右表中不满足条件的行
        > select table1.column, table2.column from table1 right join table2 on table1.column = table2.column
     - 满外连接: 满外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回两个表中不满足条件的所有行
        > select table1.column, table2.column from table1 full join table2 on table1.column = table2.column

### 子查询:
- 特点: 子查询在主查询前执行一次,主查询使用子查询的结果
- 单行子查询: 返回的只有一条记录
    - 对单行子查询可使用单行记录比较运算符: 如: <, >, =, >=, <=, <>, !=
- 多行子查询: 返回的有多条记录
    - 对多行子查询只能使用多行记录比较运算符: 如: all, any, in
        > all 和 子查询返回的所有值比较  
        any 和 子查询返回的任意值比较  
        in 等于列表中的任何一个

### 索引的作用: 
- 在数据库中用来加速对表的查询,通过使用快速路径访问方法快速定位数据,减少磁盘的I/O
- 索引创建以后,在用户撤销它之前并不会用到该索引的名字,但是索引在用户查询时会自动起作用

### 索引创建的两种情况:
- 自动:当在表中定义了一个primary key 或 unique 约束条件时,数据库自动创建一个对应的唯一索引
- 手动:用户可以创建索引以加速查询
     > 如: create index 索引名称 on 表名(字段名称)

### 视图: 是一个虚拟的表
- 可以限制对数据的访问,可以给用户授予表的特定部分的访问权限而不是整个表的访问权限
- 可以使复杂的查询变得简单.在编写查询后,可以方便的重用它而不必知道它的基本查询细节
- 提供了对相同数据的不同显示
- 创建视图: create vive 视图名称 as 查询语句
    > create vive v_emp as (select empno,ename,job from emp);





