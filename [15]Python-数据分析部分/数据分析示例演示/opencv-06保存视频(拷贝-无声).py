# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-27 18:45

import cv2

"""
# OpenCV提供的格式是未经过压缩的，目前支持的格式如下：
CV_FOURCC('P', 'I', 'M', '1') = MPEG-1 codec
CV_FOURCC('M', 'J', 'P', 'G') = motion-jpeg codec
CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec 
CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec 
CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec 
CV_FOURCC('U', '2', '6', '3') = H263 codec 
CV_FOURCC('I', '2', '6', '3') = H263I codec 
CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec

# 视频格式包括: 
# I420(适合处理大文件) -> .avi;
# PIMI -> .avi;
# MJPG -> .avi & .mp4
# THEO -> .ogv;
# FLV1(flash video, 流媒体视频) -> .flv
"""


# 加载视频
cap = cv2.VideoCapture("./05.mp4")

# 获取视频的宽度与高度
w = int(cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)) + 1
h = int(cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)) + 1


# 参数一: 保存视频的地址
# 参数二: 视频编码格式
# 参数三: 视频采样频率(一秒多少帧)
# 参数四: 视频尺寸
writer = cv2.VideoWriter("./copy.avi",cv2.VideoWriter_fourcc('M', 'P', '4', '2'),24,(w,h))
# writer = cv2.VideoWriter("./copy.flv",cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),24,(w,h))

# mp4格式
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# writer = cv2.VideoWriter("./copy.mp4",fourcc,24,(w,h))


while True:

    # 读取视频中的图片
    flag, frame = cap.read()

    # 显示图片frame,窗口名字video
    cv2.imshow("video",frame)

    # 保存图片
    writer.write(frame)

    # 当在键盘上输入q就退出循环
    if ord("q") == cv2.waitKey(30):
        break

# 循环结束,释放资源
cv2.destroyAllWindows()
cap.release()

writer.release()

