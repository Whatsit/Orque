import socket
import sys
from threading import Thread

def handler(connect, player):
	while True:
		#recv client command
		response = connect.recv(1024).decode()
		
		if(response):
			if not response:
				break;
			else:
				print ("Player ", player, " : ",response)
				if(response == 'exit'):
					print ("Player ", player, 'has rage quit')
					break;
				else:
					#process commands
					res = 'you did: ' + response
					connect.send(res.encode())
	connect.close()
	
if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("format: python server.py [port]")
		print("using default port")

	port = 8080
	if len(sys.argv) == 2:
		port = sys.argv[1]
	host = socket.gethostname()
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host, int(port)))

	print ('server started on port: ', port)
	server.listen(5)

	playerCount = 0
	while True:
		connect, address = server.accept()
		print('New Connection', address)
		print(address, "is Player ", playerCount)
		
		#send hello
		msg = 'welcome to orque'
		connect.send(msg.encode())
		
		thread = Thread(target=handler, args=(connect, playerCount))
		thread.start()
		
		playerCount += 1
	server.close()

