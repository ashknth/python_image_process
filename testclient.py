import socket
import threading
from doctor import Doctor

def handle_client(client_socket):
    """Handles the conversation with a single patient."""
    try:
        # Receive the patient's name
        patient_name = client_socket.recv(1024).decode('utf-8')
        
        # Load the Doctor object for this patient, or create a new one
        doctor = Doctor.load_history(patient_name)
        print(f"Handling patient: {patient_name}")

        while True:
            # Receive input from the patient
            patient_input = client_socket.recv(1024).decode('utf-8')

            # If the patient wants to quit, break the loop
            if patient_input.lower() in ['quit', 'exit']:
                break

            # Generate a reply using the Doctor object
            reply = doctor.generate_reply(patient_input)

            # Send the reply to the patient
            client_socket.sendall(reply.encode('utf-8'))

        # Save the patient's history when they disconnect
        doctor.save_history()

    finally:
        client_socket.close()

def main():
    host = 'localhost'
    port = 8080

    # Start the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    main()
