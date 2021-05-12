
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


def options():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-H", "--host", dest="host",
                      default="127.0.0.1", type="string",
                      help="specify hostname to run on [127.0.0.1 default] ")
    parser.add_option("-p", "--port", dest="port", default=80,
                      type="int", help="port number to run on [80 default]")

    (options, args) = parser.parse_args()

    global host
    host = options.host
    global port
    port = options.port


if __name__ == "__main__":
    # create an instance of OptionParser
    parser = OptionParser()
    # creating an obj of the socket
    # will use ipv4 address and tcp stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # call the funcs
    options()
    portscanner()
