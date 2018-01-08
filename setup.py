import sys

from escuta import Escuta

from threading import Thread
import _thread

listaPortas = [2211,2222,2233]

listaEscua = []



def controle(comando):


    if(comando == 'versao'):
        print('0.0.1')
    elif(comando == 'portas'):
        print(listaPortas)
    elif(comando == 'start'):
        for porta in listaPortas:
            print(porta)
            t = _thread.start_new_thread(tredingEscuta, (porta,))
            listaEscua.append(t)
            # t.start()

    else:
        print('Comendo não encontrado')


def tredingEscuta(porta):
    escuta = Escuta(porta)
    escuta.run()
    listaEscua.append(escuta)


#logo marota
print("""

   7==#.              (((C    
    %#@7             C=#73    
     =C7=7         .=¦=¦@A    
      7(=7=.      .(¦==J3     
      J.(=7($    7(¦==3C      
      C  7=7=($.J(¦=C#        
     C    C(===¦¦¦=#%         
     ¦     7(====@73          
    J       =¦=C==C3          
    5       .(#===J           
   ‘        .@¦(==3.          
   C        $J((==$           
   J         7(===%           
  ,=       ÐÐ=((==A           
  ,=$#   ÐW5ÐC(===%.          
   =35®®MW5Ð %(=¦7J           
     #®®MM              



""")

print("Controle de portas")
while 1:
    comando = str(input())
    controle(comando)