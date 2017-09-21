#import socket
from socket import *

TARGET_HOST = 'www.google.com'
TARGET_PORT = 80

# create client socket object from socket class
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket(AF_INET, SOCK_STREAM)


# connect the client socket object to target host & port
client.connect((TARGET_HOST, TARGET_PORT))

# send some data (fuzz) to target host
client.send('GET / HTTP/1.1\r\nHost:' + TARGET_HOST + '\r\n\r\n')

# retrieve data from client object
response = client.recv(4096)

# display retrieved data
print(response)
