import socket
import threading
from xml.dom.expatbuilder import theDOMImplementation

Port = 5050
Server = socket.gethostbyname(socket.gethostname())

ADDR = (Server, Port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

def handle_client(conn, addr):
    pass

def start():
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread,start()
        print(f'[ACTIVE CONNECTIOMS] {threading.activeCount() - 1}')


print('[starting] server is starting...')
start()