import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 8080)
server_socket.bind(server_address)

server_socket.listen(1)
print("Echo server is running...")

while True:
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")
        
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received: {data}")
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
