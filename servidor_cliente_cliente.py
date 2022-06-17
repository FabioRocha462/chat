import socket
import threading

from cliente import cliente
lista_clientes = []

def novo_cliente(id,conexao,endereco):
    lista_clientes.append({'nome':'cliente_'+str(id),'conexao':conexao,'endereco':endereco})
    def thread_cliente():
        print('conexao para ' + str(endereco))
        while True:
            msg = conexao.recv(1024).decode()

            if not msg:
                break
            cliente_destino = msg.split('/')
            nome = cliente_destino[0]
            print(nome)
            menssagem = cliente_destino[1]
            client = next((c for c in lista_clientes if c['nome'] == nome),None)
            client['conexao'].send(menssagem.encode())
        conexao.close()
    return threading.Thread(target=thread_cliente, args=())






def servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.0.102',8090))
    id = 0
    while True:
        server.listen(1000)
        print("ESPERANDO CONEXÕES")
        conexao,endereco = server.accept()
        print(conexao,endereco)
        cliente_thread = novo_cliente(id,conexao,endereco)
        cliente_thread.start()
        id +=1
if __name__ == '__main__':\
    servidor()