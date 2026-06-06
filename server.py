import socket

HOST = "127.0.0.1"
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print("Server is listening for connections...")

        conn, addr = server.accept()

        with conn:
            print(f"Client connected from {addr}")

            data = conn.recv(1024)

            print("Client says:", data.decode())

            conn.sendall(b"Hello from server!")

except Exception as error:
    print("Server error:", error)