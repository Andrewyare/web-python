import socket
from datetime import datetime
import threading
import time

server_address = ('127.0.0.1', 200)
max_size = 1024
print('Starting the client at', datetime.now())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345))

def write():
    while True:
        message = input("Write:")
        client.send(message.encode("utf-8"))

def receive():
    while True:
        data = client.recv(max_size)
        if data.decode('utf-8') == "End":
            print("Connection closed...") 
            time.sleep(5)
            exit()
         
data = client.recv(1024)
print(data.decode('utf-8'))
message = input("Enter message:")        
client.send(message.encode('utf-8'))
    
write_thread = threading.Thread(target = write)
write_thread.start()

recv_thread = threading.Thread(target = receive)
recv_thread.start()
