#!usr/bin/python3
import socket

print('Iniciado')

 # ouvirá em todas as interfaces
S_IP = '192.168.1.111'

# porta que irá receber
S_PORTA = 5000

# AF_INET = ex: IVP4 | SOCK_STREAM = ex: TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVIDOR = (S_IP, S_PORTA)
tcp.connect(SERVIDOR)

while 1: 
    print('Mande a sua mensagem')
    msg = input()
    tcp.send(bytes(msg, 'utf8'))
        
tcp.close()

