# This code is under the MAX license
# PyTelChat Chat Server 1.0
# YOU MUST CHANGE THE PORT NUMBER WHENEVER YOU END THE SERVER! ON LINE 34!
import socket
import threading

def handle_client(client_socket, client_address):
    print(f'Accepted connection from {client_address}')
 
response = "{client_address} joined the chat!"
 send_message(response)
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            # Process the received message
            process_message(data.strip())

def process_message(message):
    print(f'Received: {message}')
    if message.lower() == 'info':
        response = "PyTelChat Chat Server 1.0 - github.com/MaxBiz100/PyTelChat"
        send_message(response)
         # Add more conditions and responses as needed
    
  
def send_message(message):
    for client in clients:
        client.send(f'Message recvd: {message}\n'.encode('utf-8'))

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('0.0.0.0', 5212)  # Listen on all available interfaces

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print('Server is running and listening for incoming connections...')

# Maintain a list of connected clients
clients = []

try:
    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        # Create a thread to handle client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

        # Send a welcome message to the client
        welcome_message = "Welcome to the chat!"
        client_socket.send(welcome_message.encode('utf-8'))

except KeyboardInterrupt:
    print('Server error 1. Server terminated.')

finally:
    # Close all client connections
    for client in clients:
        client.close()

    # Close the server socket
    server_socket.close()
