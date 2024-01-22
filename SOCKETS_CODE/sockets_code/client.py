import socket

host = "192.168.197.66"
port = 12347
server_add = (host,port)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as cli:
    print("client is connected to the server")
    cli.connect(server_add)


    while True:
        msg = input("enter msg: ")

        print("encoding msg")
        msg = msg.encode()

#string has encode whereas hi
# Binary Data has decode

        print("sending msg")
        cli.sendall(msg)
