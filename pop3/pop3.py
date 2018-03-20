import socket
import sys
import argparse
import ssl


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str, help='Mail server host')
    parser.add_argument('port', type=int, help='Mail server port', default=110)
    parser.add_argument("login", type=str, help="User login")
    parser.add_argument("password", type=str, help="User password.")
    args = parser.parse_args()

    if args.port < 0 and args.port > 65535:
        print('Incorrect port. Default will be used [110].')
        args.port = 110
    return args

