import socket

print("Welcome to World Wide Web")
stop = "Y"
while(stop != "N"):
    ip_address_server = input(str("Enter IP Address Server: "))
    port = int(input(str("Enter Port : ")))
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_client.connect((ip_address_server, port))
    print("Connect ...")
   
    my_ip_address = sock_client.getsockname()[0]
    print("IP Address Saya : %s" %(my_ip_address))
    enter = '\r\n'.encode()
    request_line = 'GET /index.html HTTP/1.1'.encode()
    host = 'Host: '+str(my_ip_address)+':'+str(port)
    host = host.encode()
    user_agent = 'User-Agent: WorldWideWeb'.encode()
    accept = 'Accept: text/html'.encode()
    entity_header = b''.join([host, enter, user_agent, enter, accept])
    request = b''.join([request_line, enter, entity_header, enter])
    sock_client.send(request)
    response = sock_client.recv(1024)
    print(response.decode())
    
    sock_client.close()
    print("Close...\n")
    stop = input(str("Do you want to continue?(Y/N)"))
