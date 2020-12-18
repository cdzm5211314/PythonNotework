# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:52


# isinstance(object, classinfo)  # 判断object对象是否是已知的classinfo类型
# issubclass(class, classinfo)   # 判断class类是否是classinfo类的子类


## 对象的属性管理函数: 通过字符串的形式操作对象相关的属性
# hasattr(object, name)	            判断object对象中是否存在name属性
# getattr(object, name[, default])	从object对象中获取name属性的值,当属性不存在时,如果给出default参数,则返回default,如果没有给出default 则产生一个AttributeError错误
# setattr(object, name, value)	    给object对象的name属性设置值
# delattr(object, name)	            删除object对象中的name属性, delattr(x, 'y') 等同于 del x.y


