import socket
import threading
from datetime import datetime

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            tanggal = datetime.now().strftime("%d-%m-%Y")

            pesan = f"[{tanggal}] {msg}"
            broadcast(pesan.encode('ascii'))

        except:
            break

def receive():
    while True:
        client, _ = server.accept()
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        threading.Thread(target=handle, args=(client,)).start()

receive()
