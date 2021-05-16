
#from termcolor import colored

try:
    import socket
    from termcolor import colored
    from optparse import OptionParser
    import platform
    import os
    import threading
except ImportError as err:
    print(err)
    module = "".join(str(err).split(' ')[-1:]).strip("\'")
    print("%s IS NOT INSTALLED. USE 'pip install %s' TO INSTALL IT " %
          (module, module))


# def ping(host):
#     print()
#     # use a different option for each platform
#     param = '-n' if platform.system().lower() == 'windows' else '-c'
#     # the command is ping [-option] [number of pkts] [host]
#     command = "ping %s 1 %s" % (param, host)
#     # NOTICE:wehn Destination host unreachable error. Exit code is zero (no error)
#     if str(os.system(command)) == 1:
#         print("""The host is not replaying to ping requset make sure you typed a correct ip address;\
#          otherwise either the host is behind a firewall or is offline.
#          """)
#         exit()


def portscanner(host, port):
    # will return a 0 if no erros
    # ping(host)

    if sock.connect_ex((host, port)):
        print(colored("[-] port %d is closed" % port, "red"))
    else:
        banner = sock.recv(1024)
        print(colored("[+] port %d is open" % port, "green")+"\n"+banner)


def thread_ports(host, ports):
    hostIp = socket.gethostbyname(host)
    if hostIp == host:
        host = ""
    print("[*] Result scan for %s %s:" % (host, hostIp))
    for each_port in ports:
        thread = threading.Thread(
            target=portscanner, args=(host, int(each_port)))
        thread.start()

def options():
    parser = OptionParser(
        "\n[!!] usage: %prog [-H -p -h] [ip] [port,port1] \n[!!] use -h to print help")
    parser.add_option("-H", "--host", dest="host",
                      default="127.0.0.1", type="string",
                      help="specify hostname to run on [127.0.0.1 default] ")
    parser.add_option("-p", "--port", dest="ports", default=80,
                      type="string", help="one or more(seperated by comma) port number to run on [80 default]")

    (options, args) = parser.parse_args()
    parser.usage
    global host
    host = options.host
    global ports
    if host == "127.0.0.1":
        print(parser.usage)
    ports = str(options.ports).split(",")

    thread_ports(host, ports)
if __name__ == "__main__":
    # create an instance of OptionParser
    parser = OptionParser()
    # creating an obj of the socket
    # will use ipv4 address and tcp stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # call the funcs
    options()
    #portscanner()
