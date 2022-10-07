from socket import *
IP = ''
PORT = 50000
BUFFLEN = 512
listenSocket = socket(AF_INET,SOCK_STREAM)
listenSocket.bind((IP,PORT))

listenSocket.listen(8)
print(f'客户端启动成功，在｛port｝端口等待客户端连接...')

dataSocket,addr = listenSocket.accept()
print(f'接受一个客户端', addr)
while True:
	recved = dataSocket.recv(BUFFLEN)
	if not recved:
		break
	info = recved.decode()
	print(f'收到对方信息：{info}')
	dataSocket.send(f'服务端收到信息：{info}'.encode())

dataSocket.close()
listenSocket.close()