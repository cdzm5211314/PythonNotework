# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 9:25

import json

### json格式的字符串 和 Python数据类型 之间的转换
## json.loads(): json格式字符串(js) ---> Python数据类型
# 	                   对象               字典
# 	                   数组               列表
## json.dumps(): Python数据类型 ---> json格式字符串(js)
#                      字典               对象
#                      列表               数组
#                      元组               数组
# 注意: json.dumps()默认使用ascii编码;添加参数ensure_ascii=False,禁用ascii编码


## json.loads(): json格式字符串 ---> Python数据类型
# json格式的对象
jsobject = '{"city":"天地会","name":"步惊云"}'
python_dict = json.loads(jsobject)
print(python_dict,type(python_dict))  # {'city': '天地会', 'name': '步惊云'} <class 'dict'>
# json格式的数组
jsarray = '[1,2,3,4]'
python_list = json.loads(jsarray)
print(python_list,type(python_list))  # [1, 2, 3, 4] <class 'list'>


## json.dumps(): Python数据类型 ---> json格式字符串
# Python类型字典
dict = {"city":"天地会","name":"聂风"}
jsobject = json.dumps(dict,ensure_ascii=False)
print(jsobject,type(jsobject))  # {"city": "天地会", "name": "聂风"} <class 'str'>
# Python类型列表
list = [1,3,5,7,9]
jsarray1 = json.dumps(list)
print(jsarray1,type(jsarray1))  # [1, 3, 5, 7, 9] <class 'str'>
# Python类型元组
tuple = (0,2,4,6,8)
jsarray2 = json.dumps(tuple)
print(jsarray2,type(jsarray2))  # [0, 2, 4, 6, 8] <class 'str'>



