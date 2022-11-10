# coding:utf-8
'''import socket
import os

def sendF(s):
	
	str1 = s.recv(1024)
	filename = str1.decode('utf-8')
	print('I want to send the file %s!' % filename)
	if os.path.exists(filename):
		print('I have %s, begin to download!' % filename)
		s.send(b'yes')
		s.recv(1024)
		size = 1024
		with open(filename,'rb') as f:
			while True:
				data = f.read(size)
				s.send(data)
				if len(data)<size:
					break
		print('The downloaded file is %s.' % filename)
	else:
		print('Sorry, I have no %s' % filename)
		s.send(b'no')
	s.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))


while 1:
	sendF(s)'''


import socket
import os


def sendfile(sock):
	str1 = sock.recv(1024)
	filename = str1.decode('utf-8')
	print('the sever request my file: %s' , filename)
	if os.path.exists(filename):
		print('I have %s ,begin to download!' % filename)
		sock.send(b'yes')
		sock.recv(1024)
		size = 1024
		with open(filename, 'rb') as f:
			while True:
				data = f.read(size)
				sock.send(data)
				if len(data) < size:
					break
		print('%s is download sucessfully!' % filename)
	else:
		print('Sorry ,I have bo %s' % filename)
		sock.send(b'no')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9000))
while True:		
	sendfile(sock)
sock.close()