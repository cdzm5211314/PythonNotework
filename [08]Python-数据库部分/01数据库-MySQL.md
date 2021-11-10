 MySQL数据库知识总结

***

### 数据库终端命令行:

- 本地数据库链接: `mysql -u USER -pPASSWORD`  `注:-p与密码之间没有空格`
- 远程数据库链接: `mysql -h IP -P PORT -u USER -pPASSWORD`
- 退出数据库: `exit;`  `quit;`  `\q;`
- 数据库表数据的备份与还原:
  - 备份注: -R -E：备份所有(结构&数据&存储过程&函数&事件&触发器)
  - 数据库某个库的指定表数据备份: `mysqldump -u USER -p dbname table1 table2 ... > localdirname\localtablename.sql `
  - 数据库某个库数据备份: `mysqldump -u USER -p dbname > localdirname\localfilename.sql `
  - 数据库多个库数据备份: `mysqldump -u USER -p --databases dbname1 dbname2 > localdirname\localfilename.sql `
  - 数据库所有库数据备份: `mysqldump -u USER -p --all-databases > localdirname\localfilename.sql `
  - 还原注: 需要先创建数据库,然后再进行数据还原
  - 数据库某个库的指定表数据还原:  `mysql -u USER -p dbname < localdirname\localtablename.sql`
  - 数据库某个库数据还原:  `mysql -u USER -p dbname < localdirname\localfilename.sql`
  - SQL脚本文件还原:  `source localdirname\localfilename.sql`



### 数据库聚合函数:

- avg(fieldname):  求该字段的平均值
- sum(fieldname):  求该字段的总和
- max(fieldname):  求该字段的最大值
- min(fieldname):  求该字段的最小值
- count(fieldname):  统计该字段的记录个数,注: 空值不会被统计



### 数据库常用内置函数:

 - 字符串函数: 
    - length() 字符串占用字节长度: `select length(fieldname) from tablename;`
   - char_length() 字符串包含文字长度:  `select char_length(fieldname) from tablename;`
   - trim() 字符串去掉左右两端的空格:  `select trim(fieldname) from tablename;`
   - mid() 将字符串截取一部分: `select mid(fieldname,1,3) from tablename;`
     - 注: mid(str, start, nums)  str表示被截取的字符串,start表示截取的开始位置(从1开始),nums表示截取的长度
- 数值函数: 
  - round() 四舍五入: `select round(fieldname, num) from tablename;`
    - 注: round(fieldname, num) fieldname被处理的小数,num表示保留几个小数位数
  - floor() 数值向下取整: `select floor(fieldname) from tablename;`
  - ceiling() 数值向上取整: `select ceiling(fieldname) from tablename;`
- 日期时间函数:
  - now() 获取服务器当前日期时间: `select now();`
  - current_date() 获取服务器当前日期: `select current_date();`
  - current_time() 获取服务器当前时间: `select current_time();`
  - to_days() 将日期转换为总天数: `select to_days('2011-11-11');`
  - dayofyear() 求该年已过多少天: `select dayofyear(now());`
  - week() 返回当前日期是第几周:  `select week(now());`



### 数据库运算符:

- 算术运算符: +, -, *, /, %
  - / : 除法运算,返回商,也可写成div
  - %: 求余运算,返回余数,也可写成mod
- 比较运算符:  =, !=, >, >=, <, <=, <>, <=>(安全等于)  
  - 等于运算: =, <=>
  - 不等于运算: !=, <>
- 逻辑运算符: and(逻辑与-&&), or(逻辑或-||), not(逻辑非)
  - and: 两个或多个条件同时成立
  - or: 任意一个条件成立即可
  - not: 表示条件的相反面,即对条件取反
  - 注: 优先级 not > and > or
- 范围与集合: between ... and ..., not between ... and ...,in, not in
  - where fieldname between value1 and value2;  `注: 含有边界值`
  - where fieldname not between value1 and value2;  `注: 含有边界值`
  - where fieldname in (value1, value2);
  - where fieldname not in (value1, value2);
- 空值与空字符串: 
  - 空值: where fieldname is null;
  - 非空值: where fieldname is not null;
  - 空字符串: where fieldname = '';
  - 非空字符串: where fieldname != '';
  - 注: 空值与非空值只能使用`is` 或 `is not`去匹配
  - 注: 空字符串与非空字符串只能使用`=` 或 `!=`去匹配
- 模糊查询与通配符: like, _, %
  - `_`: 匹配单个字符; `%`: 匹配0到多个字符
  - 如: `where fieldname like "%branches/branch_200811/2007282232_.txt%";`
- 位运算符: &(位与), |(位或), ^(位异或), >>(右位移), <<(左位移), ~(位反)
  - 注: 位运算必须先将数据转换为二进制 



### 数据表字段约束:

- 主键约束: `primary key`  注: 字段值唯一不重复且不能为空

- 主键自动增长: `primary key auto_increment`

- 非空约束: `not null` 注: 字段值不能为空,但可以有多个重复的值

- 唯一约束: `unique` 注: 字段值不能重复,但可以有多个重复的null值

- 默认值约束: `default`  注: 当增加数据时没有插如值时,会自动插入默认值 

- 外键约束: `foreign key` 注: 外键是表与表之间的某种约定关系,即外键所在表为从表,关联表为主表 

  - 注: 一对多外键关联:  在多的一方创建外键字段,指向一的一方的主键(即一方为主表,多方为从表)

- 示例如下: 

  ```
  cerate table student(
  	sid int primary key auto_increment,  -- 主键约束并自动增长
  	sname varchar(32) not null,  -- 非空约束
  	suser varchar(128) unique,  -- 唯一约束
  	sage int default 0,  -- 默认值约束
  	foreign key(外键字段名称) references 关联表名称(关联表主键)  -- 外键约束
  );
  ```



### 数据定义语言:  DDL

- 对象： 数据库和数据表 

- 关键词： create, alter, drop, truncate

- 创建数据库: 

  - 简单创建数据库: `create database dbname charset='utf8';`
  - 判断数据库是否存在再创建: `create database if not exists dbname;`
  - 指定字符串与校对规则创建: `create database dbname character set utf8 collate utf8_general_ci;`

- 删除数据库: `drop database dbname;`

- 查询所有数据库: `show databases;`

- 查询创建数据库的定义语句: `show create database dbname;`

- 进入/切换数据库: `use dbname;`

- 查看当前所在数据库: `select database();`

- 创建数据表: 

  ```
  create table table_name(
  	字段名 数据类型 [字段约束条件],
  	字段名 数据类型 [字段约束条件]
  );
  如下示例: 
  create table tablename(
  	field1 int(4) primary key auto_increment,
      field2 varchar(20)
  )default charset='utf8';
  create table tablename(
  	field1 int(4) primary key auto_increment,
      field2 varchar(20)
  )engine=InnoDB, character set utf8,collate utf8_general_ci;
  ```

- 删除数据表: `drop table tablename;`

- 删除数据表(数据): `truncate table student;`

- 查看所有数据表: `show tables;`

- 查看数据表结构: `desc tablename;`

- 查看创建数据表的定义语句: `show create table tablename;`

- 修改数据表结构:

  ```
  # 修改数据表名称: 两种方式
  rename table oldtablename to newtablename;
  alter table oldtablename rename to newtablename;
  # 添加数据表字段
  alter table tablename add fieldname varchar(20);
  # 删除数据表字段
  alter table tablename drop fieldname;
  # 修改数据表字段名称
  alter table tablename change oldfieldname newfieldname varchar(20);
  # 修改数据表字段类型 - int类型
  alter table tablename modify fieldname int;
  ```



### 数据操纵语言: DML

- 对象：记录(行) 
- 关键词：insert, update, delete 
- 数据表插入数据:
  - 插入所有字段数据: `insert into tablename values(fieldname1value, fieldname2value, ...);`
  - 插入某些字段数据: `insert into tablename (fieldname1, fieldname2, ...) values(fieldname1value, fieldname2value, ...); `
  - 插入所有字段的多条数据: `insert into tablename  values(fieldname1value, fieldname2value, ...),(fieldname1value, fieldname2value, ...); `
- 数据表删除数据:
  - 删除所有数据: `delete from tablename;`
  - 根据条件删除数据: `delete form tablename where 过滤条件;`
- 数据表修改数据:
  - 修改所有数据的某一字段的值: `update tablename set fieldname=fieldnamevalue;`
  - 修改所有数据的多个字段的值: `update tablename set fieldname1=fieldvalue1, fieldname2=fieldvalue2;`
  - 修改所有数据中满足过滤条件的某字段的值: `update tablename set fieldname=fieldnamevalue where 过滤条件; `
  - 注: 修改数据表字段值,可以加where过滤条件



### 删除数据表数据: `drop`, `truncate`, `delete`

- drop(属于DDL)直接将数据表直接删除,没有办法找回: `drop table tablename`;
- truncate(属于DDL)直接将数据表数据清空,但会保留数据表结构: `truncate table tablename;` 
  - 注: 删除的数据无法恢复且不能与where过滤条件一块使用
- delete(属于DML)是一条一条的删除数据表数据: `delete from tablename;`
  - 注: 删除的数据可以恢复且常与where过滤条件一块使用,用于删除满足条件的数据

  - 三者在速度上的区别: drop   >   truncate   >   delete



### 数据查询语言: DQL

- 执行顺序：from ---> where ---> group by ---> having ---> order by ---> limit ---> select 
- `group by` 与 `having` 一起使用,可以限制输出的结果,只有满足条件表达式的结果才会显示 
- `having` 和 `where`的区别：
  - where作用于表或视图，是表和视图的查询条件
  - having作用于分组后的记录，用于选择满足条件的组
- select查询示例:
  - 查询结果进行去重: `select distinct fieldname1, fieldname2 from tablename;`
  - 查询时给字段起别名(as可省略): `select fieldname as '字段别名' from tablename;` 
  - where过滤条件查询:
    - 比较运算符过滤条件: `select * from tablename where fieldname > 10000;`
    - 逻辑运算符过滤条件: `select * from tablename where fieldname1='男' and fieldname2 > 10000;`
    - 逻辑运算符过滤条件: `select * from tablename where fieldname1='女' or fieldname2 > 10000;`
    - 逻辑运算符过滤条件: `select * from tablename where not fieldname > 10000;`
    - 范围运算符过滤条件: `select * from tablename where fieldname between 5000 and 8000;`
    - 范围运算符过滤条件: `select * from tablename where fieldname not between 5000 and 8000;`
    - 集合运算符过滤条件: `select * from tablename where fieldname in (5000,8000);`
    - 集合运算符过滤条件: `select * from tablename where fieldname not in (5000,8000);`
    - 模糊与通配符过滤条件: `select * from tablename where fieldname like '_张%';`
    - 空值过滤条件: `select * from tablename where fieldname is null;`
    - 空值过滤条件: `select * from tablename where fieldname is not null;`
    - 空字符串过滤条件: `select * from tablename where fieldname = '';`
    - 空字符串过滤条件: `select * from tablename where fieldname != '';`
  - group by进行分组查询: `select * from tablename group by fieldname;`
  - group by + having查询:  过滤条件中包含聚合函数统计的结果,这样只能使用having关键字
    - `select deptno,avg(salary) from tablename group by deptno having avg(salary) > 9000;`
  - order by进行排序查询:  查询结果默认升序(asc),降序使用desc
    - `select * from tablename order by fieldname1 desc, fieldname2 asc;`
  - limit [start,] nums分页查询: start可选表示从第几条开始,不写默认从0开始,nums表示要查询几行
    -  `select * from tablename limit 2,5;`



### 数据控制语言: DCL

- 创建,修改,删除用户: 
  - 创建用户: `create user 'USERNAME'@'IPADDR' identified by 'PASSWORD';`
    - 注: IPADDR为IP时表示用户只能在指定的IP主机上访问
    - 注: IPADDR为%时表示用户可以在任何主机上进行访问
  - 修改用户: ` rename user 'OLD_USERNAME' to 'NEW_USERNAME';`
  - 删除用户: `drop user 'USERNAME'@'IPADDR';`
- 用户授权与收回: 
  - 用户授权: 所有数据库所有表使用\*.\*, 所有权限使用all或all privileges 
    - 对已有用户进行授权: `grant all privileges on DBNAME.* to USERNAME;`
    - 对未有用户进行授权: `grant all privileges on DBNAME.* to USERNAME@IPADDR identified by PASSWORD;`
    - 对未有用户单独授权: `grant select,insert on DBNAME.* to USERNAME@% identified by PASSWORD;`
    - 更新: `flush privileges;`
  - 权限收回: 使用root用户去撤销权限,否则会报错 
    - 收回用户所有权限: `revoke all privileges on DBNAME.* from USERNAME@IPADDR;`
    - 收回用户某些权限: `revoke select,update on DBNAME.* from USERNAME@IPADDR;`
    - 更新: `flush privileges;`



### 多表关联查询: 

- 笛卡尔积查询结果: 表一数据数 * 表二数据数

  - `select * from from tablename1,tablename2;`

- 自连接查询(单表): join ... on

  - 示例: `select t1.column, t2.column from table as t1 join table as t2 on t1.column = t2.column;`

- 关联表 - 内关联查询:  inner join ... on 

  - 注: 内连接:两个表在连接过程中只返回满足连接条件的行结果
  - 示例: `select table1.column, table2.column from table1, table2 where table1.column = table2.column; `
  - 示例: `select table1.column, table2.column from table1 inner join table2 on table1.column = table2.column;`

- 关联表 - 左关联查询:  left join ... on 

  - 注: 左连接:两个表在连接过程中除返回满足连接条件的行以外,还返回左表中不满足条件的行 
  - 示例: `select table1.column, table2.column from table1 left join table2 on table1.column = table2.column;`

- 关联表 - 右关联查询:  right join ... on 

  - 注: 右链接:两个表在连接过程中除返回满足连接条件的行以外,还返回右表中不满足条件的行 
  - 示例: `select table1.column, table2.column from table1 right join table2 on table1.column = table2.column;`

- 关联表 - 全关联查询:  full join ... on  MySQL不支持

  - 注: 外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回两个表中不满足条件的所有行 

  - 示例: `select table1.column, table2.column from table1 full join table2 on table1.column = table2.column;`

- 注: 关联查询需满足以下条件,两张表有连接关系; 如:一张表的主键与另张表的外键



### 子查询与合并查询 :

- 子查询: in,   not in,   exists,   not exists,   any,   all
  - 注: 子查询在主查询前先执行一次,主查询使用子查询的结果 
  - 注: 子查询总是使用圆括号括起来,子查询可以嵌套在select,insert,update,delete语句中
  - 比较运算符的子查询: `select * from tablename where fieldname >= (select fieldname from tablename where fieldname=1);`
  - in与not in关键字: 主查询语句的条件可能落在子查询语句的结果中 
    - 示例: `select * from tablename where fieldname in (select fieldname from tablename);`
    - 示例: `select * from tablename where fieldname not in (select fieldname from tablename);`
  - exists与not exists关键:  加入子查询查询到记录，则进行外层查询，否则，不执行外层查询 
    - 示例: `select * from tablename where exists (select * from tablename);`
    - 示例: `select * from tablename where not exists (select * from tablename);`
  - any关键字: 表示子查询语句的结果满足主查询语句的其中任一条件 
    - 示例: `select * from tablename where fieldname >= (select fieldname from tablename);`
  - all关键字: 表示子查询语句的结果满足主查询语句的所有条件 
    - 示例: `select * from tablename where fieldname >= (select fieldname from tablename);`
- 合并查询: union,   union all
  - union: 数据库系统会将所有的查询结果合并到一起，然后去掉重复的记录
    - 示例:  `select fieldname from tablename1 union select fieldname from tablename;`
  - union all: 数据库系统会将所有的查询结果合并到一起，不会去除掉重复的记录 
    - 示例: `select fieldname from tablename1 union all select fieldname from tablename2;`



### 视图,索引与存储过程:

- 视图的创建,查看,修改,删除: 
  - 创建视图: `create view VIEWNAME as select * from TABLENAME;`
  - 创建视图: `create view VIEWNAME(VIEWNAME1,VIEWNAME2,...) as select * from TABLENAME;`
  - 创建视图: `create view VIEWNAME as select FIELDNAME1,FIELDNAME2,... from TABLENAME;`
  - 查看视图: `select * from VIEWNAME;`
  - 修改视图: `alert view VIEWNAME as select * from TABLENAME;`
  - 更新视图: `insert into VIEWNAME values(FIELDNAMWVALUE1,FIELDNAMWVALUE2,...);`
  - 更新视图: `update VIEWNAME set FIELDNAME='' where FIELDNAME="";`
  - 更新视图:  `delete from VIEWNAME where FIELDNAME='';`
  - 删除视图: `drop view VIEWNAME1,VIEWNAME2;`
  - 删除视图: `drop view if exists VIEWNAME1,VIEWNAME2;`
- 索引的创建与删除:
  - 注: 索引有普通索引,唯一性索引,全文索引,单列索引,多列索引,空间索引
  - 创建普通索引: `cerate index INDEXNAME on TABLENAME(FIELDNAME);`
  - 创建唯一性索引: `cerate unique index INDEXNAME on TABLENAME(FIELDNAME);`
  - 删除索引: `drop index INDEXNAME on TABLENAME;`

- 存储过程的创建与调用:

  - 存储过程的创建与调用语法:

    ```
    # 存储过程的创建:
    create procedure PROCENAME(PROCEPARAMETER)
    [存储特性]
    begin
    	SQL语句;
    end;
    注: PROCENAME表示存储过程名称,PROCEPARAMETER表示存储过程参数列表
    注: in表示输入参数,out表示输出参数,inout表示即可以输入也可以输出参数,type表示参数类型
    
    # 存储过程的调用:
    call 存储过程名称(参数1,参数2,...);
    注: 对于存储过程提供的临时变量,MySQL规定要加上@开头
    ```

  - 查看存储过程状态: `show procedure status;`

  - 显示存储过程定义: `show create procedure PROCENAME;`

  - 删除存储过程: `drop procedure [if exists] PROCENAME;`

  - 存储过程变量定义: `declare variable_name variable_type;`

    ```
    # 创建存储过程:
    create procedure addnum(in num1 int, in num2 int, out res int)
    begin
    	-- 定义变量可以设置默认值: declare r int default 默认值;
    	-- 定义变量可以使用表字段类型: declare r tablename.fieldname%type default 默认值;
    	declare r int;  
    	set r := num1 + num2;  -- 把两个数的和赋值给变量r, :=与=都支持
    	set res := r;  -- 把计算后的值传递给res
    end;
    # 调用存储过程:
    call addnum(2, 3, @r);
    # 查看调用结果: select @r;
    ```

  - 存储过程分支语句:

    ```
    # 双分支if语句的创建:
    create procedure socrelevel(in socre int, out res varchar(16))
    begin 
        if sorce > 60 then  -- 条件表达式
            set res = '及格';  -- 分支语句
        else
            set res = '不及格';
        end if;
     end;
    # 双分支if语句的调用: call socrelevel(62, @res);
    # 双分支if语句的结果: select @res;
    
    # 多分支if语句的创建:
    create procedure socrelevel(in socre int, out res varchar(16))
    begin 
        if sorce > 100 then
            set res := '你输入的不是百分制分数';
        elseif sorce >= 90 then
        	set res := '你狠优秀';
        elseif sorce >= 80 then
        	set res := '成绩良好';
        elseif sorce >= 70 then
        	set res := '成绩一般';
        elseif sorce >= 60 then
        	set res := '刚好及格';
        elseif sorce >= 0 then
        	set res := '不及格,继续努力';
        else
            set res := '你输入的不是百分制分数';
        end if;
     end;
     # 多分支if语句的调用: call socrelevel(72, @res);
     # 多分支if语句的结果: select @res;
    ```

  - 存储过程循环语句:

    ```
    # while循环语句:
    create procedure printnum()
    begin
    	declare i int default 0;
        while i < 100  -- 循环条件语句
        do 
            select 'hello word';  -- 循环语句体
            set i = i+1;  -- 改变循环变量的值,避免死循环
        end while;
    end;
    # while循环语句的调用: call printnum();
    ```

    

  































