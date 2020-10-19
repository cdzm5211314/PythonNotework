# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/15 10:14


### 示例: 假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表y_03,y_10),那么此时如何寻找出气温和随时间(天)变化的某种规律?

from matplotlib import pyplot, font_manager
import matplotlib

## 设置中文显示
matplotlib.rc('font', family='MicroSoft YaHei')
# my_font = font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", weight='bold')

## 2016年3月份与10月份的每天的最高气温(即y轴数据)
y_03 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

## 3月与10月都是每月31天(即x轴数据)
x_03 = range(1,32)
x_10 = range(41,72)

## 设置图形大小与清晰度
pyplot.figure(figsize=(20,8), dpi=80)

## 绘制散点图,并添加图例说明
pyplot.scatter(x_03, y_03, label='3月份')
pyplot.scatter(x_10, y_10, label='10月份')

## 设置x轴刻度间距,字符串,中文显示,显示的旋转角度
_x = list(x_03) + list(x_10)
_xticks_labels = ['3月{}日'.format(i) for i in x_03]
_xticks_labels += ['10月{}日'.format(i-40) for i in x_10]
pyplot.xticks(_x[::3], _xticks_labels[::3], rotation=45)
# pyplot.xticks(_x, _xticks_labels, rotation=45, fontproperties=my_font)

## 添加图例
pyplot.legend(loc=0)
# pyplot.legend(loc=0, prop=my_font)

## 添加描述信息
pyplot.xlabel("时间")
pyplot.ylabel("温度")
pyplot.title("标题:3月份与10月份每天最高气温情况")

## 展示散点图
pyplot.show()