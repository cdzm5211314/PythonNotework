### URL地址的反向解析: 命名空间(namespace) + 别名(name) [+ 参数]
```
# views视图: 一般与URL重定向一块使用
from django.shortcuts import redirect           # 重定向到另一个URL地址
from django.shortcuts import reverse            # 反向解析URL地址
return redirect(reverse('命名空间:别名')  # 无参数
return redirect(reverse('命名空间:别名', args=(param1,param2))  # 元组类型,位置参数(顺序参数)
return redirect(reverse('命名空间:别名', kwargs={'param1':'value1', 'param2':'value2'}))  # 字典类型,关键字参数

# templates模版:
{% url '命名空间:别名' %}  # 无参数
{% url '命名空间:别名' param1 param2 %}  # 位置参数(顺序参数)
{% url '命名空间:别名' param1=value1 param2=value2 %}  # 关键字参数
```


