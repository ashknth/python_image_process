# atmclient.py

import socket
import tkinter as tk
from tkinter import messagebox

HOST = 'localhost'
PORT = 8080

class ATMClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Client")

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((HOST, PORT))

        # Username and PIN fields
        self.label_user = tk.Label(root, text="Username")
        self.label_user.pack()

        self.entry_user = tk.Entry(root)
        self.entry_user.pack()

        self.label_pass = tk.Label(root, text="PIN")
        self.label_pass.pack()

        self.entry_pass = tk.Entry(root, show="*")
        self.entry_pass.pack()

        # Login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        # Withdraw and balance buttons
        self.balance_button = tk.Button(root, text="Check Balance", command=self.check_balance, state="disabled")
        self.balance_button.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, state="disabled")
        self.withdraw_button.pack()

    def login(self):
        username = self.entry_user.get()
        pin = self.entry_pass.get()

        # Send login info to the server
        self.server_socket.sendall(username.encode('utf-8'))
        self.server_socket.sendall(pin.encode('utf-8'))

        # Receive login response
        response = self.server_socket.recv(1024).decode('utf-8')

        if response == "Login successful":
            messagebox.showinfo("Login", "Login successful!")
            self.balance_button.config(state="normal")
            self.withdraw_button.config(state="normal")
        else:
            messagebox.showwarning("Login", "Login failed. Please try again.")

    def check_balance(self):
        self.server_socket.sendall("balance".encode('utf-8'))
        balance = self.server_socket.recv(1024).decode('utf-8')
        messagebox.showinfo("Balance", balance)

    def withdraw(self):
        amount = tk.simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
        self.server_socket.sendall(f"withdraw {amount}".encode('utf-8'))
        response = self.server_socket.recv(1024).decode('utf-8')
        messagebox.showinfo("Withdraw", response)

    def close(self):
        self.server_socket.sendall("quit".encode('utf-8'))
        self.server_socket.close()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    atm_client_app = ATMClientApp(root)
    root.protocol("WM_DELETE_WINDOW", atm_client_app.close)
    root.mainloop()
