import socket
import threading

# Handle the client request in a new thread
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            
            # Echo the message back to the client
            response = f"Server received: {message}"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        print(f"Connection closed for {client_address}")
        client_socket.close()

def start_server(host='127.0.0.1', port=12345):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        
        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()


