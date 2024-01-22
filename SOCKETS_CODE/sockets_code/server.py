import socket

host = "192.168.197.209"
port = 65535
server_add = (host,port)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as ser:
    print("Creating the server socket")
    ser.bind((host,port))
    print("server socket started")
    
    print("waiting for client")
    ser.listen()

    c,r = ser.accept()
    print("connecting with client")
    print(r)
    print("starting conversation.......")
    while True:
        data = c.recv(1024)
        data = data.decode()
        print("cli: ",data)
