# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/15 11:47

### 示例:假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,
# 为了展示列表中电影本身的票房以及同其他电影的数据对比情况,应该如何更加直观的呈现该数据?

from matplotlib import pyplot, font_manager
import matplotlib

## 设置中文显示
matplotlib.rc('font', family='MicroSoft YaHei')
# my_font = font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", weight='bold')

x = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
y_14 = [2358,399,2358,362]
y_15 = [12357,156,2045,168]
y_16 = [15746,312,4497,319]

## x轴数据
bar_width = 0.2  # 数据间隔,注意发生条形重叠现象
x_14 = list(range(len(x)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

## 设置图形大小与清晰度
pyplot.figure(figsize=(20,8), dpi=80)

## 绘制条形图(竖状)
pyplot.bar(x_14, y_14, width=bar_width, label='9月14日')
pyplot.bar(x_15, y_15, width=bar_width, label='9月15日')
pyplot.bar(x_16, y_16, width=bar_width, label='9月16日')

## 设置图例
pyplot.legend()

## 设置x轴刻度间距,字符串,中文显示,显示旋转角度
pyplot.xticks(x_15, x)  # 显示在中间位置

## 展示条形图
pyplot.show()
