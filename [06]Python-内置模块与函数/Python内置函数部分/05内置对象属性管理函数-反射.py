# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:52


# isinstance(obj, cls)  # 判断 obj 是否 是 类cls 的对象
# issubclass(ZiClazz, FuClazz)  # 判断 ZiClazz类 是否 是 FuClazz类 的派生类


## 对象的属性管理函数: ★★ 通过字符串的形式操作对象相关的属性
# hasattr(obj, name)	        判断obj对象中是否存在name属性
# getattr(obj, name[, default])	从obj对象中获取name属性的值,当属性不存在时,如果给出default参数,则返回default,如果没有给出default 则产生一个AttributeError错误
# setattr(obj, name, value)	    给obj对象的name属性设置值
# delattr(obj, name)	        删除obj对象中的name属性, delattr(x, 'y') 等同于 del x.y


