import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("127.0.0.1", 12345))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Send data to the client
    client_socket.send(b"Hello, client! This is the server.")

    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received from client: {data.decode('utf-8')}")

    # Close the client socket
    client_socket.close()
