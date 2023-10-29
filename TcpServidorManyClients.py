#!/usr/bin/python3
import socket
import time
import threading
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    
print("Iniciado")

IP = "192.168.1.114"
NAME = "Servidor"

listTCP = []
file = open('conversa.txt', 'w+')
file.write("")
file.close()

def write(txt):
    f = open('conversa.txt', 'a+')
    f.write(txt+"\n")
    f.close()
    
def updataCall():
    f = open('conversa.txt', 'r')
    content = bytes("a1", "utf8")
    f.close()
    
    
    for i in listTCP:
        i.send(content)

def listenTCP(conexao, cliente):
    listTCP.append(conexao)
    try:
        while True:
            envio = conexao.recv(1024)
            if envio != "":
                write(envio.decode())
                clear()
                updataCall()
    except Exception as exc:
        print(exc)
        conexao.close()
        listTCP.remove(conexao)
        
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVIDOR = (IP, 5000)
tcp.bind(SERVIDOR)
tcp.listen()

while True:
    print("Aguarda conexão do cliente...")
    conexao, cliente = tcp.accept()
    print("O cliente se conectou!")
    t1 = threading.Thread(target=listenTCP, args=(conexao, cliente))
    t1.start()
tcp.close()
