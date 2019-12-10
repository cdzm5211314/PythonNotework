# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 13:50

import numpy as np
import wave

# 安装: pip install wave
# wave 读取wav格式的音乐文件

# 读取音频数据
# wave01 = wave.open('./01.wav')
# wave02 = wave.open('./02.wav')
# print(wave01)  # <wave.Wave_read object at 0x000000000212D390>
# print(wave02)  # <wave.Wave_read object at 0x0000000003C17780>

# 获取参数
# p1 = wave01.getparams()
# p2 = wave02.getparams()
# print(p1)  # _wave_params(nchannels=2, sampwidth=2, framerate=22050, nframes=64000, comptype='NONE', compname='not compressed')
# print(p2)  # _wave_params(nchannels=1, sampwidth=2, framerate=22050, nframes=62465, comptype='NONE', compname='not compressed')

# 获取数据,只能调用(读取)一次
# data01 = wave01.readframes(nframes=64000)  # data01为bytes类型数据
# data02 = wave02.readframes(nframes=62465)  # data02为bytes类型数据

# 把bytes类型数据转换为numpy类型数据
# nd01 = np.frombuffer(data01,dtype=np.int16)
# nd02 = np.frombuffer(data02,dtype=np.int16)
# print(nd01, nd01.shape)
# print(nd02, nd02.shape)


# 还原为歌类型
# wav01= nd01.reshape(64000,2)
# wav02= nd02.reshape(62465,1)
# print(wav01.shape)  # (64000, 2)
# print(wav02.shape)  # (62465, 1)

# 音频切片操作
# pre01 = wav01[:22050*2]  # 前2秒音频数据
# print(pre01.shape)

# # 写入音频数据
# f = wave.Wave_write("./03.wav")
# # 设置属性
# f.setframerate(22050)  # 帧数
# f.setnchannels(2)  # 通道数
# f.setsampwidth(2)
# f.setnframes(2*22050)  # 2秒数据,1秒22050
# # 写数据
# f.writeframes(pre01.tobytes())
# f.close()

# # 写入音频数据 - 倒转
# f2 = wave.Wave_write("./03倒转.wav")
# # 设置属性
# f2.setframerate(22050)  # 帧数(1秒多少帧)
# f2.setnframes(2*22050)  # 2秒数据,1秒22050
# f2.setnchannels(2)  # 通道数
# f2.setsampwidth(2)
# # 写数据,将音乐倒着播放
# f2.writeframes(pre01[::-1].tobytes())
# f2.close()


###############################################################################################
# 合成音频文件
f1 = wave.open('./01.wav', mode="rb")
f2 = wave.open('./02.wav', mode="rb")

p1 = f1.getparams()
p2 = f2.getparams()
print(p1)
print(p2)

# 只能读取一次
data01 = f1.readframes(nframes=860923)  # data01为bytes类型数据
data02 = f2.readframes(nframes=287083)  # data02为bytes类型数据

# 把bytes类型数据转换为numpy类型数据
nd01 = np.frombuffer(data01,dtype=np.int16)
nd02 = np.frombuffer(data02,dtype=np.int16)

# 还原为歌类型
wav01= nd01.reshape(860923,2)
wav02= nd02.reshape(287083,2)


# 获取音频文件的时长: 秒 -> 分
# print(860923/44100)  # 19秒
# print(860923/44100//60)
# print(860923/22050)  # 39秒
# print(287083/22050//60)

# 音频切片
pre01 = wav01[:44100*8]
pre02 = wav02[:22050*5]
print(pre01.shape, pre02.shape)

# 将两段(ndarray)音频合二为一
music_np = np.concatenate([pre01,pre02])
print(music_np.shape)

f = wave.open("./music.wav", mode="wb")
f.setnchannels(2)
f.setsampwidth(2)
f.setframerate(44100)
f.setnframes(463050)

f.writeframes(music_np)
f.close()

f1.close()
f2.close()