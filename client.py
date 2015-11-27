import socket
import sys
import config

client = socket.socket()

if len(sys.argv) < 2:
	print ('format: client.py [address] [port]')
else:
	host = sys.argv[1]
	port = config.port
	if len(sys.argv) == 3:
		port = sys.argv[2]

	print ("Connecting to server: ", host, ":", port)
	client.connect((host, int(port)))

	#recv hello msg
	print(client.recv(1024).decode())

	while True:
		command = input("Input Command: ")

		if(command):
			client.send(command.encode())	
			if(command == 'exit'):
				break;
			else:
				print(client.recv(1024).decode())
		
	client.close()	
	print('goodbye')