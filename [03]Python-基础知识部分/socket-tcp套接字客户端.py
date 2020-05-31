# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020-05-29 10:57

import socket


def main():

    # 创建套接字 - tcp客户端
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务端信息
    # server_ip = input("请输入服务端IP地址: ")
    # server_port = int(input("请输入服务端PORT端口号: "))

    # 链接服务端
    # tcp_client_socket.connect((server_ip, server_port))
    tcp_client_socket.connect(("192.168.0.100", 8888))

    while True:
        send_data = input("请输入你要发送服务端的信息: ")

        # 当客户端输入"exit"后退出本次与服务端的链接
        if send_data == "exit":
            break

        # 发送数据给服务端
        tcp_client_socket.send(send_data.encode("utf-8"))

        # 接收服务端发送的数据
        recv_data = tcp_client_socket.recv(1024)
        print("服务端的回复信息: %s" % recv_data.decode("utf-8"))

    # 关闭套接字
    tcp_client_socket.close()

if __name__ == '__main__':

    main()