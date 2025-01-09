# import socket
# HOST = '127.0.0.1' # Localhost – Server’s IP address
# PORT = 10675 # Non-privileged port – Server’s port number
# # Create a socket and bind it to an address
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT)) # Bind to host and port
#     s.listen() # Listen for incoming connections
#     print("Server is listening...")
#     conn, addr = s.accept() # Accept a client connection
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024) # Receive data from the client
#             if not data:
#                 break
#             conn.sendall(data) # Echo the received data back to the client

import socket
import threading
# Counter to assign unique IDs to clients
client_counter = 1
client_mapping = {} # Maps address to client IDs
# Function to handle communication with a single client
def handle_client(conn, addr):
    global client_counter
    client_id = client_mapping.get(addr, f"Client{client_counter}")
    if addr not in client_mapping:
        client_mapping[addr] = client_id
        client_counter += 1
        print(f"{client_id} connected.")
  
    with conn:
        while True:
            try:
                # Receive message from client
                message = conn.recv(1024).decode('utf-8')
                if not message or message.lower() == "exit":
                    print(f"{client_id} disconnected.")
                    break
                print(f"{client_id}: {message}")
                # Send response to client
                response = input(f"You (to {client_id}): ")
                conn.send(response.encode('utf-8'))
                if response.lower() == "exit":
                    print(f"{client_id} disconnected.")
                    break
            except Exception as e:
                print(f"Error with {client_id}: {e}")
                break

# Main server function
# Create a TCP server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server Console:\nWaiting for connections...")
    while True:
        conn, addr = server_socket.accept()
        # Create a new thread to handle the client
        threading.Thread(target=handle_client, args=(conn, addr)).start()