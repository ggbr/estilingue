from socket import *
from threading import Thread

class Escuta:
    def __init__(self,port):
        self._clientes = []
        self._host = ''
        self._port = port
        self._trds = []


    def clientHandler(self,c, addr):

        print(self._port , "se conectou")
        try:
            while True:
                print('Escutando...', addr)
                data = c.recv(1024)
                if not data: break
                print(data)
        except:
            print("Clinte se desconectou  da porta: ", self._port)
            c.close()

    def run(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self._host, self._port))
        s.listen(5)

        print("Server is running on " + str(self._port))

        # Thread(target=clientHandler).start()
        # Thread(target=clientHandler).start()
        # Thread(target=clientHandler).start()


        for i in range(5):
            c, addr = s.accept()
            self._clientes.append(addr)
            t = Thread(target=self.clientHandler, args=(c, addr))
            self._trds.append(t)
            t.start()

        for t in self._trds:
            t.join()

        s.close()