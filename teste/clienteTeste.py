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
        print('Enviando ...')
        sock.sendall(b'message ' )
        
        print('Menssagem enviada ...')
        
    

except:
    print('Você foi desconectado do sevidor.')
    sock.close()