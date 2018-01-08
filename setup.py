from escuta import Escuta

from threading import Thread


listaPortas = [3311,3322,3333]

listaEscua = []



def tredingEscuta(port):

    print('Iniciando porta  ' , port)
        
    escuta = Escuta(porta)
    escuta.run()
        
    listaEscua.append(escuta)

for porta in listaPortas:
    t = Thread(target=tredingEscuta,  args=(porta) )
    listaEscua.append(t)
    t.start()