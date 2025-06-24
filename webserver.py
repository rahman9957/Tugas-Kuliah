import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
print('Mendengarkan pada host & port : http://%s:%s'%(SERVER_HOST, SERVER_PORT))
print('Tekan ctrl+C untuk keluar')

while True: 
    client_connection, client_address = server_socket.accept() 
    request = client_connection.recv(1024).decode() 
    print(request)
    response_line = 'HTTP/1.1 200 OK'.encode()
    entity_header = 'Content-Type: text/html'.encode()
    file = open('index.html', 'r')
    body = file.read().encode()
    file.close()
    enter = '\r\n'.encode() 
    response = b''.join([response_line, enter, entity_header, enter, enter, body])
    client_connection.send(response)
    client_connection.close() 
server_socket.close() 