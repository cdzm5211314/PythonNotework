# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020-05-29 10:13

import socket


def main():

    # 创建套接字 - udp
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 使用套接字接收数据

    # 绑定本地信息 - 必须绑定自己电脑的ip和port信息
    udp_socket.bind(("", 7878))

    # 接收数据 - 指定字节的数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # recv_data是一个元组数据(接收的数据, (发送方的ip, port))
        # print(recv_data)

        recv_msg = recv_data[0]   # 存储接收的数据
        recv_addr = recv_data[1]  # 存储发送方的地址信息
        print("%s : %s" %(str(recv_addr), recv_msg.decode("utf-8")))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()

