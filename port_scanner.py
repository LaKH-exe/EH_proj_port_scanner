import socket
# creating an obj of the socket
#will use ipv4 address and tcp stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the host and the port we want to scan
host = "192.168.1.113"
port = 443


def portscanner(port):
    # will return a 0 if no erros
    if sock.connect_ex((host, port)):
        print("port %d is closed" % port)
    else:
        print("port %d is open" % port)


portscanner(port)
