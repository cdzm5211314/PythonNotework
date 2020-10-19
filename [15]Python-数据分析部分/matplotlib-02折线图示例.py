# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/14 15:29

from matplotlib import pyplot
import random
import matplotlib
from matplotlib import font_manager


### 示例: 绘制10点-12点之间每分钟的气温折线图

# 设置折线图中的中文显示问题
# 第一种设置中文字体: matplotlib.rc()  支持windows/linux系统
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',}
# matplotlib.rc('font', **font)
matplotlib.rc('font', family='MicroSoft YaHei', weight='bold')
# 第二种设置中文字体: font_manager  支持windows/linux系统/mac系统
# my_font = font_manager.FontProperties(family='MicroSoft YaHei', weight='bold')

# 每分钟的气温数据,即y轴数据
y = [random.randint(20, 35) for i in range(120)]

# 时间分钟数据,即x轴数据
x = range(0,120)

# 设置图片大小与清晰度
pyplot.figure(figsize=(20,8), dpi=80)

# 绘制折线图
pyplot.plot(x, y)

xticks_labels = ["10点{}分".format(i) for i in range(60)]
xticks_labels += ["11点{}分".format(i) for i in range(60)]

# 设置x轴刻度
# pyplot.xticks(x)

# 设置x轴刻度,并设置对应的字符串显示
# pyplot.xticks(list(x)[::3], xticks_labels[::3])

# 设置x轴刻度,并设置对应的字符串显示,且旋转显示的方式
# rotation控制显示旋转角度
pyplot.xticks(list(x)[::5], xticks_labels[::5], rotation=45)

# 设置x轴刻度,并设置对应的字符串显示,且旋转显示的方式,且中文显示
# pyplot.xticks(list(x)[::5], xticks_labels[::5], rotation=45, fontproperties=my_font)

# 设置x轴与y轴刻描述信息
# 注: 也可以传递参数fontproperties设置中文显示
pyplot.xlabel("时间")
pyplot.ylabel("温度 单位(℃)")
pyplot.title("10点到12每分钟的气温变化情况")

# 展示折线图
pyplot.show()


