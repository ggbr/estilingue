from socket import *
from threading import Thread

class Escuta:
    def __init__(self):
        self._clientes = []
        self._host = ''
        self._port = 1313
        self._trds = []


    def clientHandler(self,c, addr):

        print(addr, "is Connected")
        try:
            while True:
                data = c.recv(1024)
                data = str(data[:-1])
                if (data == b'ls'):
                    print('comoando aceito')
                else:
                    print(data, ' Não encontrado')
        except:
            print("Error. Data not sent to all clients.")

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