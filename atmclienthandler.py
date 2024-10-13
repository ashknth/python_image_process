# atmclienthandler.py

import socket

class ClientHandler:
    def __init__(self, client_socket, bank):
        self.client_socket = client_socket
        self.bank = bank
        self.username = None

    def handle_client(self):
        try:
            # Handle login
            self.username = self.client_socket.recv(1024).decode('utf-8')
            pin = self.client_socket.recv(1024).decode('utf-8')

            if self.bank.verify_user(self.username, pin):
                self.client_socket.sendall("Login successful".encode('utf-8'))
                self.client_operations()
            else:
                self.client_socket.sendall("Login failed".encode('utf-8'))
        finally:
            self.client_socket.close()

    def client_operations(self):
        while True:
            # Receive command (e.g., "balance" or "withdraw <amount>")
            command = self.client_socket.recv(1024).decode('utf-8')

            if command == "balance":
                balance = self.bank.get_balance(self.username)
                self.client_socket.sendall(f"Your balance is ${balance}".encode('utf-8'))
            
            elif command.startswith("withdraw"):
                amount = int(command.split()[1])
                if self.bank.withdraw(self.username, amount):
                    self.client_socket.sendall(f"Withdrawal of ${amount} successful.".encode('utf-8'))
                else:
                    self.client_socket.sendall("Insufficient funds".encode('utf-8'))

            elif command == "quit":
                self.client_socket.sendall("Goodbye!".encode('utf-8'))
                break
