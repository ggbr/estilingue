from escuta import Escuta

from threading import Thread
import _thread

listaPortas = [(3311),(3322),(3333)]

listaEscua = []



def controle():
    pass


def tredingEscuta(porta):
    escuta = Escuta(porta)
    escuta.run()
    listaEscua.append(escuta)

for porta in listaPortas:
    print(porta)
    t = _thread.start_new_thread(tredingEscuta, (porta, )  )
    listaEscua.append(t)
    #t.start()

while 1:
   pass