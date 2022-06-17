import socket
import threading
lista_clientes = []

def novo_cliente(id,conexao,endereco):
    lista_clientes.append({'nome':'cliente_'+str(id),'conexao':conexao,'endereco':endereco})
    def thread_cliente():
        print('conexao para ' + str(endereco))
        while True:
            msg = conexao.recv(1024).decode()
            conexao_comparadora = conexao
            if not msg:
                break
            for cliente_conexao in [c['conexao'] for c in lista_clientes]:
                if conexao_comparadora != cliente_conexao:
                    cliente_conexao.send(msg.encode())
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