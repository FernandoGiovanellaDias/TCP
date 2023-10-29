#!/usr/bin/python3
import socket
import time
import threading

print("Iniciado")

IP = "192.168.1.114"
NAME = "Cliente"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENTE = (IP, 5000)

tcp.connect(CLIENTE)

def listenTCP(tcp):
    try:
        while True:
            envio = tcp.recv(1024)
            if envio != "":
                print(envio.decode())
    except Exception as exc:
        print(exc)


t1 = threading.Thread(target=listenTCP, args=(tcp,))
t1.start()

while True:
    msg = input()
    tcp.send(bytes(NAME+": "+msg, "utf8"))
    
tcp.close()





