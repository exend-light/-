from socket import *
from multiprocessing import Process

sock=socket(AF_INET,SOCK_DGRAM)
ADDR=('127.0.0.1',8888)
sock.bind(ADDR)

user={}

def do_login(tem,addr):
    if tem[1] in user:

        sock.sendto('\n昵称已被占用'.encode(), addr)
        return

    else:

        sock.sendto(b'ok', addr)

        if len(user)!=0:

            for i in user:
                msg="\n%s进入聊天室" % tem[1]

                sock.sendto(msg.encode(), user[i])

    user[tem[1]]=addr

def do_send(tem,addr):

    for i in user:

        if i!=tem[1]:

            sock.sendto(tem[2].encode(), user[i])


def do_exict(data01):

    del user[data01.decode()]

    for i in user:

        mag=data01+'已退出'.encode()

        sock.sendto(mag, user[i])


def do_admin():
    while True:
        text = input("请输入：")
        msg='s %s 管理员：\n%s'%('管理员',text)

        sock.sendto(msg.encode(),ADDR)


def serve():

    while True:
        data01,addr=sock.recvfrom(1024)

        tem=data01.decode().split(' ',2)

        if tem[0]=='l':

            do_login(tem,addr)

        elif tem[0]=='s':
            do_send(tem,addr)

        else :
            do_exict(data01)


def main():

    p=Process(target=serve)
    p.start()

    do_admin()

    p.join()







if __name__ == '__main__':

    main()




