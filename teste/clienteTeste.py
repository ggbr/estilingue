import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



host  = ''

port =  3322
print('connecting to  port ' , port)
sock.connect((host, port))

try:
    while True:
        message = str(input())
        message = message
        print('Enviando ...')
        sock.send(message.encode('ascii'))
        print('Menssagem enviada ...')
        

except:
    print('Você foi desconectado do sevidor.')
    sock.close()