import socket
import _thread
import sys

def handler(connect, address):
	while True:
		#recv client command
		response = connect.recv(1024).decode()
		print (address, " : ",response)
		if not response:
			break;
		else:
			if(response == 'exit'):
				print (address, 'has rage quit')
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

	while True:
		connect, address = server.accept()
		print('New Connection', address)
		
		#send hello
		msg = 'welcome to orque'
		connect.send(msg.encode())
		
		_thread.start_new_thread(handler,(connect, address))
	server.close()

