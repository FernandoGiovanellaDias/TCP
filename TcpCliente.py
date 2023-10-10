#!/usr/bin/python3
import socket
print('Iniciado')

# ouvirá em todas as interfaces
C_IP = ''

# porta que irá receber
C_PORTA = 5000

# AF_INET = ex: IVP4 | SOCK_STREAM = ex: TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Recebe o IP e PORTA do cliente
CLIENTE = (C_IP, C_PORTA)
tcp.bind(CLIENTE)
tcp.listen()

print('Aguarda conexão do cliente ')
# Recebe o IP e PORTA do cliente
conexao, cliente = tcp.accept()

print('O cliente se conectou!')
while True:
    envio = conexao.recv(1024)
    
    if envio != '':
        print("Recebeu a mesagem: " + envio.decode())
    
   
    
conexao.close()
