import socket
import sys

client = socket.socket()

if len(sys.argv) < 1:
	print ('format: client.py [hostname] [port]')
else:
	host = sys.argv[1]
	port = 8080
	if sys.argv[2]:
		port = sys.argv[2]

	client.connect((host, int(port)))

	#recv hello msg
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