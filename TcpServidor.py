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

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVIDOR = (IP, 5000)
tcp.bind(SERVIDOR)
tcp.listen()

def listenTCP(conexao, cliente):
    try:
        while True:
            envio = conexao.recv(1024)
            if envio != "":
                print(envio.decode())
    except Exception as exc:
        print(exc)
        conexao.close()
        
clear()
print("Aguarda conexão do cliente...")
conexao, cliente = tcp.accept()
print("O cliente se conectou!")
t1 = threading.Thread(target=listenTCP, args=(conexao, cliente))
t1.start()
while True:
    conexao.send(bytes(NAME+": "+input(), "utf8"))
    clear()
tcp.close()
