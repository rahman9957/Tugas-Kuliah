import socket
import threading
from datetime import datetime

userName = input("Masukkan username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print("Terjadi kesalahan koneksi!")
            client.close()
            break

def write():
    while True:
        jam = datetime.now().strftime("%H:%M:%S")
        pesan = input('>> ')
        message = f"{userName} ({jam}): {pesan}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
