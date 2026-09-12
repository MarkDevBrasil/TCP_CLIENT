# client tcp by mark
import socket
import os
# Variaveis de escolhar

def client():
    ip = input("Digite o IP: ")
    porta = int(input("Digite a porta para se conectar: "))
    # Sockets
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    try:
        client.connect((ip, porta))
        client.send(b"computador hackeado pelo mark")

        while True:
            pacotes = client.recv(1024).decode()
            if not pacotes:
                break
            print(pacotes)
    except:
        print("Ocorreu um erro, tente novamente.")


client()
