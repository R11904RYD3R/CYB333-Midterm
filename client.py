import socket

HOST = "127.0.0.1"
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        client.sendall(b"Hello from client!")

        response = client.recv(1024)

        print("Server replied:", response.decode())

except Exception as error:
    print("Client error:", error)