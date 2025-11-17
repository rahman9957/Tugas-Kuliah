import socket
import threading
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()

clients = []
names = []

def broadcast(message):
    for c in clients:
        c.send(message)

def handle(client):
    while True:
        try:
            data = client.recv(1024).decode('ascii')
            idx = clients.index(client)
            nama = names[idx]

            waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            final = f"[{waktu}] {nama}: {data}"
            broadcast(final.encode('ascii'))

        except:
            break

def receive():
    while True:
        c, _ = server.accept()
        c.send("NICK".encode('ascii'))
        nama = c.recv(1024).decode('ascii')
        names.append(nama)
        clients.append(c)

        threading.Thread(target=handle, args=(c,)).start()

receive()
