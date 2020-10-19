# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/14 19:31

## 折线图:以折线的上升或下降来表示统计数量的增减变化的统计图
# 特点:能够显示数据的变化趋势，反映事物的变化情况。(变化)

## 直方图:由一系列高度不等的纵向条纹或线段表示数据分布的情况。一般用横轴表示数据范围，纵轴表示分布情况。
# 特点:绘制连续性的数据,展示一组或者多组数据的分布状况(统计)

## 条形图:排列在工作表的列或行中的数据可以绘制到条形图中。
# 特点:绘制连离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别。(统计)

## 散点图:用两组数据构成多个坐标点，考察坐标点的分布,判断两变量之间是否存在某种关联或总结坐标点的分布模式。
# 特点:判断变量之间是否存在数量关联趋势,展示离群点(分布规律)


from matplotlib import pyplot

## 绘制折线图: pyplot.plot(x,y)

## 绘制散点图: pyplot.scatter(x,y)

## 绘制条形图: 竖状 pyplot.bar(x,y,width)   横状 pyplot.barh(x,y,height)

## 绘制直方图: pyplot.hist(x,num_bins)
# 组数: num_bins,将数据分组,当数据在100个以内时,按数据多少常分5-12组
# 组距: bin_width,指每个小组的两个端点的距离
# 即 组数(num_bins) = 极差(max(x)-min(x)) // 组距(bin_width)

## 绘制其他图参考: http://matplotlib.org/gallery/index.html

