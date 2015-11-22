import socket
import sys

client = socket.socket()
host = socket.gethostname()
port = 8080

client.connect((host, port))

#recv hello
print(client.recv(1024).decode())

while True:
	command = input("Input Command: ")

	client.send(command.encode())	
	if(command == 'exit'):
		break;
	else:
		print(client.recv(1024).decode())
	
client.close()	
print('goodbye')