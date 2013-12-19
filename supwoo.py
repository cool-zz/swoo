import os
import requests
import json
import time, re
import random
import multiprocessing
import subprocess
import socks
import socket
import sys

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock


def test_proxy(_proxy):
    i = _proxy.split(":")
    error = False
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, i[0], int(i[1]))
    socket.socket = socks.socksocket
    socket.create_connection = create_connection
    import urllib2
    try:
        response = urllib2.urlopen('http://boards.420chan.org/wooo/').read()
        if "You're banned from 420chan!" in response:
            print("BANNED :(")
            error = True
    except:
        error = True
    if error:
        proxy_txt = open("proxies.txt", "r").readlines()
        new_proxy = [p.rstrip('\r\n') for p in proxy_txt if p != _proxy]
        new_proxy_txt = open("proxies.txt", "w")
        for i in new_proxy:
            new_proxy_txt.write(i+'\n')
    return error


def get_last_page():
    base_url = "http://api.420chan.org/wooo/threads.json"
    json = requests.get(base_url).json()
    _threads = []
    pg = json[13]
    for t in pg['threads']:
        _threads.append(str(t['no']))
    return _threads


def main(_proxy):
    threads = get_last_page()
    _thread = random.choice(threads)
    _thread = _thread.rstrip('\r\n')
    print(_proxy)
    banned = test_proxy(_proxy)
    if banned:
        sys.exit(1)
    _proxy = _proxy.replace("\n", "")
    base_url = "http://boards.420chan.org/"
    page = "{0}wooo/res/{1}.php".format(base_url, _thread)
    try:
        line = 'casperjs --proxy={0} ruin.js "{1}"'.format(_proxy, page)
        os.system(line)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    jobs = []
    proxy_txt = open("proxies.txt", "r").readlines()
    for i in proxy_txt:
        p = multiprocessing.Process(target=main, args=(i,))
        jobs.append(p)
        p.start()











