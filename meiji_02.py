import socket
import json


def receive_payload(port):
	# Create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(serversocket)

	# Get the local machine name
    host = socket.gethostname()
    print(host)

	# Reserve a port for the socket
    serversocket.bind((host, port))

	# Set the maximum number of incoming connections
    serversocket.listen(5)

    while True:
		# Wait for a connection
        clientsocket, addr = serversocket.accept()

		# Receive the payload from the AWS Lambda function
        payload = clientsocket.recv(1024)

		# Convert the payload from bytes to a JSON object
        payload = json.loads(payload.decode("utf-8"))

		# Save the payload to a file
        with open("payload.json", "w") as file:
            json.dump(payload, file)

		# Close the socket connection
        clientsocket.close()


# Start the server to receive the payload
receive_payload(12345)
