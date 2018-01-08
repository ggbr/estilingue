# Echo server program
import socket
import StringIO
import httplib
import urllib2
import requests

buff = StringIO.StringIO(2048)  
HOST = ''                 # Symbolic name meaning the local host
PORT = 8182              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)
while True:
	conn, addr = s.accept()
	print 'Connected by', addr

	data = conn.recv(2048)

	print data

	conn.close()


