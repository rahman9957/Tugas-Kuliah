import socket
from datetime import datetime

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))
serverSocket.listen(1)

print("====================================")
print("SERVER SIAP DIJALANKAN")
print("Tanggal :", datetime.now().strftime("%d-%m-%Y"))
print("====================================")

conn, addr = serverSocket.accept()
print("Terhubung dengan:", addr[0])

client_name = conn.recv(1024).decode()
server_name = input("Masukkan nama Server: ")
conn.send(server_name.encode())

print(f"{client_name} telah bergabung pada {datetime.now().strftime('%H:%M:%S')}")
print("------------------------------------")

while True:
    pesan = conn.recv(1024).decode()
    waktu_terima = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu_terima}] {client_name}: {pesan}")

    balasan = input("Balas ke client: ")
    waktu_kirim = datetime.now().strftime("%H:%M:%S")
    conn.send(f"[{waktu_kirim}] {server_name}: {balasan}".encode())

conn.close()
