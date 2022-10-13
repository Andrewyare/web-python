from datetime import datetime
from http import client
import socket
import time
import threading

print_lock = threading.Lock()

max_size = 1024
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
server.bind(('127.0.0.1', 12345))
server.listen()
print('working...')
def threaded(client_socket):
    while True:
        data = client_socket.recv(max_size).decode('utf-8')
        client_socket.send(data.encode('utf-8'))
        if data == "End":
            client_socket.close()
            exit()
        else:
            print("Message recieved: ", datetime.now())
            time.sleep(5)
            print(data, datetime.now())
while True:	
    client_socket, address = server.accept()
    print_lock.acquire()
    print('connect')
    client_socket.send('connect'.encode('utf-8'))
    thread = threading.Thread(target=threaded, args=[client_socket])
    thread.start()
