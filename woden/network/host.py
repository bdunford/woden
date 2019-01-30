import re
import subprocess
import platform
from ..utility import Parse, Lists

class Host(object):

    @staticmethod
    def Run(ipOrHost, options=None):
        options = options if options else []
        cmd = ["host"] + options + [ipOrHost]
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        r = list(map(lambda x: x.rstrip(), iter(p.stdout.readline, b'')))
        return r

    @staticmethod
    def Resolve(host):
        r = Host._parse(Host.Run(host),".*\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", "ip")
        return Lists.First(r) if r else None

    @staticmethod
    def Reverse(ip):
        return Host._get_hostnames(Host.Run(ip))

    @staticmethod
    def MailServers(domain):
        return Host._get_hostnames(Host.Run(domain, ["-t","mx"]))
    @staticmethod
    def NameServers(domain):
        return Host._get_hostnames(Host.Run(domain, ["-t", "ns"]))

    @staticmethod
    def ZoneTransfer(domain, nameServer):
        r = Host.Run(nameServer, ["-l", domain])
        return Host._parse(r,"^(?P<host>[^\s]+)\s.*\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ["ip","host"])

    @staticmethod
    def _get_hostnames(records):
        return Host._parse(records,"^.*\s(?P<host>[^\s]+)\.$","host")

    @staticmethod
    def _parse(records, expr, cg):
        results = []
        for r in records:
            o = Parse.WithRegex(expr, r)
            if o:
                try:
                    if isinstance(cg,list):
                        vals = {}
                        for f in cg:
                            vals[f] = getattr(o,f)
                        results.append(vals)
                    else:
                        results.append(getattr(o,cg))
                except:
                    pass
        return results if len(results) > 0 else None
