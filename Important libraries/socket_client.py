import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 12345))

# Send data to the server
client_socket.send(b"Hello, server! This is the harir.")

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

# Close the client socket
client_socket.close()
