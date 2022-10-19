from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

from socket import *

app = QApplication([])
IP = '127.0.0.1'
SERVER_PORT = 50000
BUFFLEN = 1024

dataSocket = socket(AF_INET, SOCK_STREAM)

dataSocket.connect((IP, SERVER_PORT))



def handleCalc():
    

     while True:
         toSend = textEdit.toPlainText()
         if toSend == 'exit':
             break

         dataSocket.send(toSend.encode())

         recved = dataSocket.recv(BUFFLEN)

         if not recved:
             break
         textEdit.appendPlainText(recved.decode())
    
    # dataSocket.close()




window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('服务器')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入内容")
textEdit.move(10,25)
textEdit.resize(300,350)


button = QPushButton('显示', window)
button.move(380,80)
window.show()


button.clicked.connect(handleCalc)


app.exec_()