import socket
import threading
import time

shutdown_flag = threading.Event()

def handle_client(client_socket):
    """Handles communication with a connected client."""
    with client_socket:
        current_time = time.ctime(time.time())  # Get the current server time
        client_socket.sendall(current_time.encode('utf-8'))

def start_server(host, port):
    """Starts the time server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse the socket address
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while not shutdown_flag.is_set():  # Check if the shutdown flag is set
            try:
                server_socket.settimeout(1)  # Set a timeout to allow periodic checking of the shutdown flag
                client_socket, addr = server_socket.accept()
                print(f"Accepted connection from {addr}")
                handle_client(client_socket)
            except socket.timeout:
                continue  # No connections, loop back and check the shutdown flag

def shutdown_server():
    """Waits for the Enter key to be pressed and then signals the server to shut down."""
    input("Press Enter to shut down the server...\n")
    shutdown_flag.set()  # Set the shutdown flag to stop the server

def main():
    host = 'localhost'
    port = 8080

    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server, args=(host, port))
    server_thread.start()

    # Wait for the user to press Enter to shut down the server
    shutdown_server()

    # Wait for the server thread to finish before exiting the program
    server_thread.join()
    print("Server has shut down.")

if __name__ == "__main__":
    main()
