# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020-05-29 10:58


import socket


def main():

    # 创建套接字 - tcp服务端
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息
    tcp_server_socket.bind(("", 8888))

    # 监听: 让默认的套接字由主动变为被动
    tcp_server_socket.listen(128)

    # 循环为多个客户端服务
    while True:
        # 等待客户端链接 - 返回一个元组()
        print("等待新的客户端...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("新的客户端已链接成功...[%s]" % str(client_addr))

        # 为一个客户端服务多次
        while True:
            # 接收客户端发送的请求数据
            recv_data = new_client_socket.recv(1024)
            print("客户端的发送信息: %s" % recv_data.decode("utf-8"))

            # 如果recv解堵塞,那么有两种方式
            # 1.客户端发送过来数据
            # 2.客户端调用close导致了这里解堵塞
            if recv_data:
                # 回复部分数据给客户端
                # new_client_socket.send("success".encode("utf-8"))
                send_data = input("请输入你要回复客户端的信息: ")
                new_client_socket.send(send_data.encode("utf-8"))
            else:
                break

        # 关闭服套接字
        new_client_socket.close()
        print("已经为这个客户端服务完毕...")

    tcp_server_socket.close()


if __name__ == '__main__':

    main()
