# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020-05-28 11:50


import socket


def main():

    # 创建套接字 - udp
    # 注: 套接字可以同时收发数据
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息 - 必须绑定自己电脑的ip和port信息
    udp_socket.bind(("", 7788))

    # 使用套接字发送数据
    # udp_socket.sendto("data".encode("utf-8"), ("addrip", port))

    # 发送数据
    # udp_socket.sendto("haha".encode("utf-8"), ("192.168.0.100", 7878))

    while True:
        send_data = input("请输入你要发送的信息: ")
        if send_data == "exit":
            break
        # 发送数据
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.100", 7878))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':

    main()
