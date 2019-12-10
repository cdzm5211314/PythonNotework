# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 16:22


import skvideo.io
import matplotlib.pyplot as plt

# 视频操作库: scikit-video  安装: pip install scikit-video
# 视频由一张张图片组成,一秒24帧,肉眼无法分辨

sk1 = skvideo.io.vread("./03.mp4")
print(type(sk1))  # numpy.ndarray
print(sk1.shape)  # (5685,540,960,3) 四维数组


# 获取视频中的某张图片
plt.imshow(sk1[200])

# 把图片数据写入到视频中
skvideo.io.vwrite("./xxx.mp4", sk1[:500])

