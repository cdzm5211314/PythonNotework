# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 11:10

# XPath语法: 选取节点(标签)
# /     根目录下查找           /title
# //    整个页面查找           //div
# @     某个节点属性           //div[@class="name"]
# text() 标签下的文本内容      /div/a/text()

# XPath语法: 谓语
# /bookstore/book[1]          选取bookstore下的第一个book元素
# /bookstore/book[last()]     选取bookstore下的最后一个book元素
# //book[@price]              选取拥有price属性的book元素

# XPath语法: 通配符
# *         匹配任意节点              //body/*        选取body节点下的所有子节点
# @*        匹配节点中的任何属性      //book[@*]      选取所有带有属性的book元素


