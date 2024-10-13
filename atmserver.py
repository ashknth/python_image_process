# atmserver.py

import socket
import threading
from atmclienthandler import ClientHandler
from bank import Bank

HOST = 'localhost'
PORT = 8080

def main():
    bank = Bank()  # Bank instance shared among client handlers

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"ATM Server started on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        
        # Create a new thread for each client
        client_handler = ClientHandler(client_socket, bank)
        client_thread = threading.Thread(target=client_handler.handle_client)
        client_thread.start()

if __name__ == "__main__":
    main()
