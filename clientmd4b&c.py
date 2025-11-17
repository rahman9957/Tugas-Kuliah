import socket
import threading
from datetime import datetime

username = input("Masukkan username: ")
client = socket.socket()
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        print(client.recv(1024).decode('ascii'))

def write():
    while True:
        teks = input(">> ")
        jam = datetime.now().strftime("%H:%M:%S")
        pesan = f"{teks} (dikirim pada {jam})"
        client.send(pesan.encode('ascii'))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
