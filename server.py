import socket
import sys
import _thread

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
				res = 'you did: ' + response
				connect.send(res.encode())
	connect.close()

if __name__ == '__main__':
	print ('server started')
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 8080
	server.bind((host, port))

	server.listen(5)

	while True:
		connect, address = server.accept()
		print('New Connection', address)
		
		#send hello
		msg = 'hi'
		connect.send(msg.encode())
		
		_thread.start_new_thread(handler,(connect, address))
	server.close()

