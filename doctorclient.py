import socket

def main():
    host = 'localhost'
    port = 8080
    
    # Get the patient's name
    patient_name = input("Please enter your name: ")

    # Connect to the doctor server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Send the patient name to the server
        s.sendall(patient_name.encode('utf-8'))
        
        while True:
            # Read input from the patient
            patient_input = input("You: ")
            
            # Send input to the server
            s.sendall(patient_input.encode('utf-8'))
            
            # Receive and print the doctor's reply
            data = s.recv(1024)
            print(f"Doctor: {data.decode('utf-8')}")
            
            if patient_input.lower() in ['quit', 'exit']:
                break

if __name__ == "__main__":
    main()
