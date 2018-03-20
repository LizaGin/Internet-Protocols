import socket
import struct
import time

#time.windows.com localhost
def gettime_ntp(addr='localhost'):
    TIME1970 = 2208988800
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(6)
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode(), (addr, 123))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= TIME1970
        return time.ctime(t), t


if __name__ == '__main__':
    try:
        print(gettime_ntp())
    except socket.timeout:
        print('Server unreachable')
