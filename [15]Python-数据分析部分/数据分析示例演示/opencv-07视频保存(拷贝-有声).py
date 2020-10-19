# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-27 19:12

import numpy as np
import cv2

# 加载视频
cap = cv2.VideoCapture("./05.mp4")

# 获取视频的宽度与高度 ---> 1918 1028
w = int(cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)) + 1
h = int(cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)) + 1
# print(w, h) (1918, 1028)

# 保存.mp4格式,并改变视频的尺寸
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter("./yousheng.mp4", fourcc, 24, (w // 2, h // 2))

while True:

    # 读取视频中的图片
    flag, frame = cap.read()

    # 图片转换为黑白图片(二维数据)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    # 显示图片frame,窗口名字video
    cv2.imshow("video", gray)


    # 保存图片,需要调整图片大小
    gray2 = cv2.resize(gray, dsize=(w // 2, h // 2))
    gray2 = gray2.reshape(h//2, w//2, 1)
    # 显示图片尺寸改变后的图片
    cv2.imshow("video2", gray2)
    # 级联,将多个ndarray数组合并到一起
    np.concatenate([gray2,gray2,gray2], axis=-1)
    # 保存图片
    writer.write(gray2)

    # 当在键盘上输入q就退出循环
    if ord("q") == cv2.waitKey(20):
        break

# 循环结束,释放资源
cv2.destroyAllWindows()
cap.release()
writer.release()

###############################################################################################

import wave

music = wave.open("./01.wav", mode="rb")
data = music.getparams()
print(data)  # _wave_params(nchannels=2, sampwidth=2, framerate=44100, nframes=860923, comptype='NONE', compname='not compressed')

data_nframes = music.readframes(data.nframes)
data_nframes = np.frombuffer(data_nframes, dtype=np.int16)
data_nframes = data_nframes.reshape(data.nframes,2)
print(data_nframes.shape)

data2 = data_nframes[:10*44100]
fp = wave.Wave_write("./music.wav")
fp.setframerate(44100)
fp.setnframes(10*44100)
fp.setnchannels(2)
fp.setsampwidth(2)

fp.writeframes(data2.tobytes())
fp.close()


###############################################################################################
# 合并视频和音频
import subprocess

# cmd = 'ffmpeg -i music.wav -i yousheng.mp4 out.mp4'


