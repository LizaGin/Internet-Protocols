import argparse
import re
import subprocess
import sys
from urllib.request import urlopen
import socket

ip_r = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
whois_r = re.compile(r'whois:\s+(.+)')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', type=str, help='')
    args = parser.parse_args()
    return args


def get_resp(sock):
    resp = []
    while 1:
        try:
            data = sock.recv(65535)
            if data:
                resp.append(data)
            else:
                break
        except socket.timeout:
            break
        except (ConnectionError, OSError) as e:
            print(str(e))
    return b''.join(resp).decode(errors='ignore')


def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        print(str(e))
        sys.exit()


def trace_to(domain):
    ip = domain_to_ip(domain)
    trace = subprocess.check_output('tracert ' + ip, shell=True, stderr=subprocess.STDOUT).decode('cp866').split('\n')
    addresses = []
    for line in trace:
        try:
            if re.search(ip_r, line):
                addresses.append(re.search(ip_r, line).group(0))
        except Exception as e:
            print(str(e))
    return addresses


def get_whois(ip):
    with urlopen('https://www.iana.org/whois?q=' + ip) as page:
        try:
            return re.search(whois_r, page.read().decode()).group(1).rstrip()
        except Exception:
            pass


def get_data(whois, ip):
    sock = socket.socket()
    sock.settimeout(2)
    sock.connect((whois, 43))
    info = ip + '\r\n'
    sock.send(info.encode())
    data = get_resp(sock)
    return data


def get_country(data):
    country_r = re.compile(r'country:\s+(\w+)', re.IGNORECASE)
    if re.search(country_r, data):
        country = re.search(country_r, data).group(1)
    else:
        country = '*'
    return country


def get_origin(data):
    origin_r = re.compile(r'origin:\s+(.+)', re.IGNORECASE)
    if re.search(origin_r, data):
        origin = re.search(origin_r, data).group(1)
    else:
        origin = '*'
    return origin


def get_descr(data):
    descr_r = re.compile(r'descr:\s+(.+)', re.IGNORECASE)
    if re.search(descr_r, data):
        descr = re.search(descr_r, data).group(1)
    else:
        descr = '*'
    return descr


def main():
    args = parse_args()
    domain = args.domain
    addresses = trace_to(domain)
    print(addresses)
    i = 0
    for ip in addresses[1:]:
        i += 1
        whois = get_whois(ip)
        if whois:
            data = get_data(whois, ip)
            as_number = get_origin(data)
            country = get_country(data)
            provider = get_descr(data)
            print('№: {0} IP: {1} AS: {2} Country: {3} Provider: {4}'.format(i, ip, as_number, country, provider))
        else:
            print('№: {0} IP: {1} AS: * Country: * Provider: *'.format(i, ip))


if __name__ == '__main__':
    main()
