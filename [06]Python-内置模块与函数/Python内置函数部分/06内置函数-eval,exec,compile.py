# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:53


### eval(), exec() 函数:
## eval(source, globals=None, locals=None)  注: 计算指定表达式的值,可以有返回值
# 把一个字符串source当成一个表达式来执行，返回表达式执行后的结果
# 示例如下:
x = 100
y = 200
a = eval('x+y')
print(a)  # 300


## exec(source, globals=None, locals=None)	注: 动态执行Python代码,返回值永远为None
# 把一个字符串source当成程序来执行
# 示例如下:
x = 100
y = 200
s = 'z = x+y; print(z); del z; print("删除成功")'
exec(s)  # 执行s绑定的语句

## 注: eval() 和 exec()的两个参数globals 和 locals:
# 都是用来设置'表达式'或'程序'运行的全局变量和局部变量


### compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

