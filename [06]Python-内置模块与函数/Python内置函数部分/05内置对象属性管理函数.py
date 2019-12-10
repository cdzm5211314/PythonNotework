# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:52


## 对象的属性管理函数: ★★
# hasattr(obj, name)	        用给定的name返回对象obj是否有此属性,此种做法可以避免在getattr(obj, name)时引发错误
# getattr(obj, name[, default])	从一个对象得到对象的属性；getattr(x, 'y') 等同于x.y; 当属性不存在时,如果给出default参数,则返回default,如果没有给出default 则产生一个AttributeError错误
# setattr(obj, name, value)	    给对象obj的名为name的属性设置相应的值value, set(x, 'y', v) 等同于 x.y = v
# delattr(obj, name)	        删除对象obj中的name属性, delattr(x, 'y') 等同于 del x.y


