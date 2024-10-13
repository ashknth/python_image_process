import socket

def get_time_from_server(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))  # This is where ConnectionRefusedError might occur
            s.sendall(b"What's the time?")
            data = s.recv(1024)
            return data.decode('utf-8')
    except ConnectionRefusedError:
        # Handle the exception when the server is not available
        print(f"Error: Unable to connect to the server at {host}:{port}. Connection was refused.")
        return None

def main():
    host = 'localhost'
    port = 8080
    time_from_server = get_time_from_server(host, port)
    
    if time_from_server:
        print(f"Time from server: {time_from_server}")
    else:
        print("Failed to retrieve the time from the server.")

if __name__ == "__main__":
    main()
