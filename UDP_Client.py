import socket

# constants
TARGET_HOST = "127.0.0.1"
TARGET_PORT = 80

# create client socket object from socket class
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data (fuzz) to target_host on target_port
client.sendto("AAABBBCCC",(TARGET_HOST, TARGET_PORT))

# receive some data
data, addr = client.recvfrom(4096)

# display received data
print(data)
