import socket
import threading


def conex_cliente(cliente,menssagem):
    def thread_cliente():
        cliente.send(menssagem.encode('utf-8'))
        while True:
            msg = cliente.recv(1024).decode('utf-8')
            if not msg:
                break
            else:    
                print(msg)    
    return threading.Thread(target=thread_cliente, args=())


def cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('192.168.0.102',8090))
    nome = input('Digite seu nome')
    nome = '@' + nome + ":"
    while True:
        msg = input('-> ')
        msg = nome + msg
        conex = conex_cliente(cliente,msg)
        conex.start()

    cliente.close()

if __name__ == '__main__':\
    cliente()
    






