# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/14 11:27

# from matplotlib import pyplot as plt
from matplotlib import pyplot


## x轴与y轴数据
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

## 设置中文显示(刻度与信息描述)
# 第一种设置中文字体: matplotlib.rc()  支持windows/linux系统
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',}
# matplotlib.rc('font', **font)
# 第二种设置中文字体: font_manager  支持windows/linux系统/mac系统
# my_font = font_manager.FontProperties(family='MicroSoft YaHei', weight='bold')

## 设置图片大小与清晰度
# 实例化一个figure并传递参数,能够在后台自动使用该figure实例,figsize参数为元组数据,表示宽度和高度
# 图像模糊的时候传入dpi参数,可以让图像更清晰
# pyplot.figure(figsize=(20, 8), dpi=80)

## 绘制折线图
# 注: x与y都是一个可迭代对象,数据一起组成了所要绘制出的坐标
# pyplot.plot(x, y)
# 绘制图形时指定参数说明: color线条颜色,linestyle线条风格,linewidth线条粗细,alpha线条透明度

## 设置x轴与y轴刻度
# pyplot.xticks(x)
# pyplot.xticks(range(2,25))
# pyplot.yticks(range(min(y), max(y)+1))

## 设置x轴刻度,不使用数值,设置为自定义字符串内容
# 注: 刻度数据个数与自定义字符串数据个数保持一致
# pyplot.xticks(list(x)[::3], xticks_labels[::3])

## 设置x轴刻度,不使用数值,设置为自定义字符串内容且显示的样式(即旋转角度)
# pyplot.xticks(list(x)[::5], xticks_labels[::5], rotation=45)

## 设置x轴刻度,不使用数值,设置为自定义字符串内容且显示的样式(即旋转角度),设置中文显示
# 注: fontproperties是第二种设置中文显示方式
# pyplot.xticks(list(x)[::5], xticks_labels[::5], rotation=45, fontproperties=my_font)

## 设置x轴,y轴及折线图的描述信息
# 注: fontproperties是第二种设置中文显示方式
# pyplot.xlabel("x轴描述")
# pyplot.ylabel("y轴描述")
# pyplot.title("折线图的描述信息")

## 绘制网格
# alpha参数设置网格线透明度
# pyplot.grid(alpha=0.2)

## 添加图例
# 注: 需要在绘制折线图的时候指定lable参数
# pyplot.plot(x, y, label="图例说明信息")
# pyplot.legend(prop=my_font)
# 注: 图例默认显示在折线图的右上角,loc参数设置显示位置(即bast或0),prop参数设置中文显示

## 保存图片到本地:
# 注: 保存svg这种矢量图格式,放大不会有锯齿
# 注: 需要在绘制折线图后才能操作保存
# pyplot.savefig("./xxx.png")

## 展示折线图
# pyplot.show()


