import sys
import time
import socket
socket.socket

f = open('scanner.txt', 'w+')
start_time = time.time()
t2 = 0
t1 = 0


def scan(host, port):
    try:
        #print("scanning: " + str(host) + " on port: " + str(port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
                print(str(port) + ' (' + str(service) + ')' + " was open")
                f.write(str(port) + ' (' + str(service) + ')' + ' was open \n')
                s.close()

            except Exception as e:
                print(str(port) + ' (NA)' + " was open")
                f.write(str(port) + ' (NA)' + ' was open \n')
                s.close()

    except KeyboardInterrupt:
        s.sock.close()
        sys.exit(1)


if(len(sys.argv) == 2):
    try:
        for i in reversed(range(1, 65536)):
            t1 = time.time()
            scan(str(sys.argv[1]), i)
            t2 = time.time()
    except KeyboardInterrupt:
        sys.exit(1)
else:
    sys.exit(1)

end_time = time.time()
total = end_time - start_time
t_total = t2 - t1

f.write('time elapsed = ' + str(total) + 's \n')
f.write('time per scan = ' + str(t_total) + 's \n')
