
#from termcolor import colored

try:
    import socket
    from termcolor import colored
except ImportError as err:
    print(err)
    module = "".join(str(err).split(' ')[-1:]).strip("\'")
    print("%s IS NOT INSTALLED. USE 'pip install %s' TO INSTALL IT " %
          (module, module))



# creating an obj of the socket
#will use ipv4 address and tcp stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the host and the port we want to scan
host = input("[*] Enter the host\t")
port = int(input("[*] Enter the port\t"))


def portscanner(port):
    # will return a 0 if no erros
    if sock.connect_ex((host, port)):
        print(colored("[-] port %d is closed" % port, "red"))
    else:
        print(colored("[+] port %d is open" % port, "green"))


portscanner(port)
