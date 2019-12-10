### 终端命令行链接数据库
> 本地链接: mysql -u用户名 -p密码  
> 远程链接: mysql -h主机IP地址 -u用户名 -p密码  
> 断开与数据库链接: exit; quit; \q;
### 数据库数据的导入导出
> 终端命令行导出: mysqldump -u用户名 -p 数据库名 > 本地目录位置\导出的文件名称.sql  
> 终端命令行导入: mysql -u用户名 -p 数据库名 < 本地目录位置\导入的文件名称.sql  
> SQL脚本文件导入: source SQL脚本文件路径 
### 数据库用户授权管理
- 创建用户: create user 用户名@localhost identified by '密码';
- 注: 
    > localhost 表示本地访问  
    > % 表示可远程访问
- 用户授权: grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option; 
- 注: 
    > 权限列表：all privileges 、select 、insert    
    > 库.表 ： \*.*  *表示所有库的所有表
### 数据库的基本操作
- 创建数据库(并指定字符集): create database 数据库名称 character set utf8;
- 查看创建库的语句(字符集): show create database 数据库名称;
- 查看已有数据库: show databases;
- 查看当前所在数据库: select database();
- 切换数据库: use 数据库名称;
- 查看数据库中已有表: show tables;
- 删除数据库: drop database 数据库名称;
### 表的基本操作
- 创建表: create table 表名(
       	字段名 数据类型,
       	字段名 数据类型,
       	...
       	字段名 数据类型
       	);
- 查看表结构: desc 表名;
- 删除表: drop table 表名; drop table 表名1,表名2,表名3;
- 查看已有表的字符集: show create table 表名;

### 表字段操作
- **添加字段(add)**
    - alter table 表名 add 字段名 数据类型;    
    - alter table 表名 add 字段名 数据类型 first;  
    - alter table 表名 add 字段名 数据类型 after 字段名;  
- **删除字段(drop)**
    - alter table 表名 drop 字段名;
- **修改字段类型(modify)**
    - alter table 表名 modify 字段名 新数据类型;
- **表重新命名(rename)**
    - alter table 表名 rename 新表名;       

### 数据库日期时间
- **日期时间数据类型**
    - date ："YYYY-MM-DD"
    - time ："HH:MM:SS"
    - datetime ："YYYY-MM-DD HH:MM:SS"   # 不给值默认返回NULL值
    - timestamp ："YYYY-MM-DD HH:MM:SS"  # 不给值默认返回系统当前时间
- **日期时间函数**
    - now()  返回服务器当前时间
    - curdate() 返回当前日期
    - curtime() 返回当前时间
    - year(date) 返回指定时间的年份
    - date(date) 返回指定时间的日期
    - time(date) 返回指定时间的时间
- **日期时间运算**
    - select * from 表名 where 字段名 运算符 (时间-interval 时间间隔单位);
    - 注: 时间间隔单位：1 day | 2 hour | 1 minute | 2 year | 3 month

### 数据库运算符操作
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

### 表数据管理
- **插入(insert)**
    - insert into 表名 values(值1),(值2),...;
    - insert into 表名(字段1,...) values(值1),...;
- **查询(select)**
    - select * from 表名 [where 条件];
    - select 字段1,字段名2 from 表名 [where 条件];
- **删除(delete)**
    - delete from 表名 where 条件;  # delete语句后如果不加where条件,所有记录全部清空
- **更新(update)**
    - update 表名 set 字段1=值1,字段2=值2,... where 条件;  # 必须加where条件

### 聚合函数
- avg(字段名): 求该字段平均值
- sum(字段名): 求和
- max(字段名): 最大值
- min(字段名): 最小值
- count(字段名): 统计该字段记录的个数

### SQL查询操作
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
        > limit m,n         ---> m 表示从第m+1条记录开始显示,显示 n 条  
        > limit(m-1)*n,n    ---> 分页显示: 每页显示n条记录,显示第m页  

### 多表查询
- select 字段名列表 from 表名列表; (笛卡尔积)
- select 字段名列表 from 表名列表 where 条件;
- 示例: select sheng.s_name,city.c_name from sheng,city where sheng.s_id=city.cfather_id;

### 连接查询
- **内连接查询**
    - 语法格式: select 字段名 from 表1 inner join 表2 on 条件;
    - 示例: select sheng.s_name,city.c_name,xian.x_name from sheng inner join city on sheng.s_id=city.cfather_id inner join xian on city.c_id=xian.xfather_id;
- **外连接查询**
    - 左外连接: 以 左表 为主显示查询结果
    - 左外连接语法: select 字段名 from 表1 left join 表2 on 条件;
    - 右外连接: 以 右表 为主显示查询结果
    - 右外连接语法: select 字段名 from 表1 left join 表2 on 条件;

### 子查询
- 特点: 子查询在主查询前执行一次,主查询使用子查询的结果








