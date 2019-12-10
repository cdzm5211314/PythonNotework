# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 15:28


import numpy as np
import pydub
# RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
# warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)

# pydub依赖ffmpeg
# ffmpeg下载并配置环境变量: https://github.com/FFmpeg/FFmpeg/releases
# 安装: pip install pydub
# pydub不仅仅可以读取mp3类型文件,wav等其他格式文件的音频文件都可以加载

# .mp3: 压缩格式音乐文件

pb = pydub.AudioSegment.from_mp3("./火的噼啪声.mp3")
print(type(pb))  # pydub.audio_segment.AudioSegment
# 可以直接操作该对象,进行切片和分贝控制

# 获取音频通道数
print(pb.channels)
# 获取音频时长
print(pb.duration_seconds)

# 对音频进行切片操作(毫秒)
pb1 = pb[:1000*5]
print(pb1.duration_seconds)

# 分贝增加(减少)10分贝
pb1 = pb1 + 10
# pb1 = pb1 - 10
print(pb1.duration_seconds)


pb2 = pydub.AudioSegment.from_mp3("./火焰喷射声.mp3")
print(pb2.duration_seconds)
pb3 = pb2[5*1000:10*1000]
print(pb3.duration_seconds)

# 两段音频合而为一
music = pb1 + pb3

# 保存合成的音频
pydub.AudioSegment.export(music,'./合成.mp3')





