import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 44344

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

# Response = ClientSocket.recv(1024)
# while True:
#     Input = input('Say Something: ')
#     ClientSocket.send(str.encode(Input))
#     Response = ClientSocket.recv(1024)
#     print(Response.decode('utf-8'))

# ClientSocket.send(bytes([1]))
# ClientSocket.send(bytes([1]))
# ClientSocket.send(str.encode("1"))
# ClientSocket.send(str.encode("1"))

size = ClientSocket.recv(4)
print(size)
msg = ClientSocket.recv(int(size.decode('utf-8')))
print(msg)


ClientSocket.close()