import re
import subprocess
import platform
from ..utility import Parse, Lists

class Ping(object):

    def __init__(self, results):
        head = None
        packets = []
        tail = None
        for r in results:
            head = Parse.WithRegex("PING\s(?P<host>[^\s]+)\s\((?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})\).*",r) if not head else head
            tail = Parse.WithRegex("(?P<transmitted>\d+)\s.*transmitted.*(?P<received>\d+)\s.*received.*(?P<lost>[\d\.]+\%)\spacket\sloss.*",r) if not tail else tail
            packet = Parse.WithRegex(".*bytes\sfrom\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}).*ttl\=(?P<ttl>\d+).*time\=(?P<time>[\d\.]+)",r)
            if packet:
                packets.append(packet)

        self.up = True if tail and int(tail.received) > 0 else False
        self.ip = head.ip if head else None
        self.host = head.host if head else None
        self.ttl = Lists.First(packets).ttl if len(packets) > 0 else None
        self.time = Lists.First(packets).time if len(packets) > 0 else None
        self.transmitted = int(tail.transmitted) if tail else 0
        self.received = int(tail.received) if tail else 0
        self.lost = tail.lost if tail else None
        self.raw = results

    @staticmethod
    def Run(ipOrHost, count=1, options=None):
        timeout = 2 if platform.system() == 'Linux' else 2000
        options = options if options else ["-c {0}".format(count),"-W {0}".format(timeout)]
        cmd = ["ping"] + options + [ipOrHost]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        r = list(map(lambda x: x.rstrip(), iter(p.stdout.readline, b'')))
        return Ping(r)
