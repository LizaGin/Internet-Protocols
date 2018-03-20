import socket
import Packet
import time
import random
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('delay', type=int, help='"The number of falsification seconds. Default is 0"', nargs='?', default=0)
    args = parser.parse_args()
    return args


def run():
    args = parse_args()
    delay = args.delay
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.bind(('localhost', 123))
        except OSError as e:
            sys.exit(str(e))
        while 1:
            data, address = sock.recvfrom(65535)
            time_now = time.time()
            req = Packet.Packet()
            req.unpack(data)
            resp = Packet.Packet(req.version_number, 4, 1, req.poll,
                                 req.time_to_sntp_format(time.time() - random.randint(2, 5) / 5),
                                 req.time_to_sntp_format(time_now - delay),
                                 req.time_to_sntp_format(time.time() - delay))
            #sock.sendto(resp.pack(), address)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        sys.exit()
