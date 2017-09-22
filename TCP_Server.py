import socket
import threading

# vars
BIND_IP = "0.0.0.0"
BIND_PORT = 9999

# create server socket object from socket class
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind server socket object with IP(public host) & PORT
server.bind((BIND_IP, BIND_PORT))

# server socket object listens up to 5 connect requests
server.listen(5)

# display bound IP & PORT
print("[*] Listening on %s:%d" % (BIND_IP, BIND_PORT))

# this is our client-handling thread
def handle_client(client_socket):
   
   # print out what the client sends
   request = client_socket.recv(1024)
   
   print("[*] Received: %s" % request)
   
   # send back a packet
   client_socket.send("ACK!")
   
   # close client_socket object connection
   client_socket.close()

# main()
While True:
  client, addr = server.accept()
  print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
  
  # spin up our client thread to handle incoming data
  client_handler = threading.Thread(target=handle_client, args=(client,))
  client_handler.start()
