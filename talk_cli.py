import sys
from multiprocessing import Process
from socket import *


def do_chat(name,sock,ADDR):

    while True:
        try:
            m = input("%s:\n"%name)
        except KeyboardInterrupt:
            m = 'quit'

        if m=='quit':
            sock.sendto(name.encode(), ADDR)
            sys.exit("您已退出登录")

        msg = 's %s %s' % (name, m)

        sock.sendto(msg.encode(), ADDR)


def do_recv(sock,name):

    while True:
        msg, addr = sock.recvfrom(1024)

        print(msg.decode(),"\n%s:"%name,end='')


def cliserver():
    sock = socket(AF_INET, SOCK_DGRAM)

    ADDR=('127.0.0.1',8888)

    while True:

        name=input("请输入姓名：")
        msg='l '+name

        sock.sendto(msg.encode(),ADDR)

        data01,addr=sock.recvfrom(1024)

        if data01==b'ok':
            print('您已进入聊天室')
            break

        else:

            print(data01.decode())


    p=Process(target=do_recv,args=(sock,name))
    p.daemon=True

    p.start()

    do_chat(name, sock, ADDR)







if __name__ == '__main__':

    cliserver()

