
# Labib Kh


# to prompt the user to download unavailable modules
try:
    import parser
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


# ping (to check if hosts are up or down) is unrileable for windows machines. The exit codes for ping are not always clear

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

    # connect to this host and port
    if sock.connect_ex((host, port)):
        print(colored("[-] port %d is closed" % port, "red"))
    else:
        # if connected will print the banner it recived
        banner = sock.recv(1024)
        print(colored("[+] port %d is open" % port, "green")+"\n"+banner)

# use threads to make it faster


def thread_ports(host, ports="", startPort="", endPort=""):
    # translate to ip add if the domain name was provided
    hostIp = socket.gethostbyname(host)
    if hostIp == host:
        host = ""
    print("[*] Result scan for %s %s:" % (host, hostIp))
    # used for range option
    if startPort and endPort:
        print("in start if")
        startPort = int(startPort)
        endPort = int(endPort)
        # inclusive range
        for each_port in range(startPort, endPort+1):
            thread = threading.Thread(
                target=portscanner, args=(host, int(each_port)))
            thread.start()
    # used for other options
    else:
        print("in else")
        for each_port in ports:
            print("checking " + each_port)
            thread = threading.Thread(
                target=portscanner, args=(host, int(each_port)))
            thread.start()


# scan the top common ports
set = None


def scanCommonPorts(option, opt_str, value, parser):
    global set
    set = "set"
    listOfCommonPorts = """1,
    5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,50,53,63,67,68,69,70,71,72,73,73,79,80,88,95,101,102,105,107,109,110,
    111,113,115,117,119,123,137,138,
    139,143,161,162,163,164,174,177,178,179,191,194,199,201,202,204,206,209,210,213,220,245,347,363,369,370,
    372,389,427,434,435,443,444,445,464,468,487,488,496,500,535,538,546,547,554,563,565,587,610,611,612,
    631,636,674,694,749,750,765,767,873,992,993,994,995"""
    commPorts = str(listOfCommonPorts).split(",")

    host = parser.values.host

    thread_ports(host, commPorts)


def options():
    parser = OptionParser(
        "\n[!!] usage: %prog [-H -p -h] [ip] [port,port1] [portStart-portEnd] \n[!!] use -h to print help")
    parser.add_option("-H", "--host", dest="host",
                      default="127.0.0.1", type="string",
                      help="specify hostname to run on [127.0.0.1 default] ")
    parser.add_option("-p", "--port", dest="ports", default=80,
                      type="string", help="one or more(seperated by comma) port number to run on [80 default]")
    parser.add_option("-r", "--rangePort", dest="rangePorts",
                      type="string", help="range of ports (seperated by a dash '-')")
    parser.add_option("-c", "--commonPorts", action="callback", dest="isSet", default=True,


                      callback=scanCommonPorts,   help="scan the top common ports")
    print("here")
    (options, args) = parser.parse_args()
    parser.usage
    host = options.host
    print("list")
    print(parser.option_list)
    if host == "127.0.0.1":
        print(parser.usage)

    if options.ports is not None and not set:
        print("in ,")
        ports = str(options.ports).split(",")
        print(ports)
        thread_ports(host, ports)

    if options.rangePorts is not None:
        print("in r")
        stratPort, endPort = options.rangePorts.split("-")
        print("start port:"+stratPort)
        print("end port" + endPort)
        thread_ports(host, "", stratPort, endPort)


if __name__ == "__main__":
    # create an instance of OptionParser
    parser = OptionParser()
    # creating an obj of the socket
    # will use ipv4 address and tcp stream
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # call options
    options()
    # portscanner()
