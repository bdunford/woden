import re
import socket
import ipaddress

class Address(object):

    @staticmethod
    def FromHost(host):
        try:
            return socket.gethostbyname(host)
        except:
            return "0.0.0.0"

    @staticmethod
    def ToHosts(ip):
        try:
            host = socket.gethostbyaddr(ip)
            hosts = [host[0]]
            if len(host) > 1:
                hosts += host[1]
            results = list(filter(lambda h: Address.FromHost(h) == ip, hosts))
            return results if len(results) > 0 else None
        except Exception as e:
            return None

    @staticmethod
    def IsRange(value):
        return True if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3}|\*|\d{1,3}/\d{1,2}|\d{1,3}\-\d{1,3})$", value) else False

    @staticmethod
    def IsIP(value):
        return True if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", value) else False

    @staticmethod
    def All(ipOrRange):
        if Address.IsIP(ipOrRange):
            return [ipOrRange]
        if Address.IsRange(ipOrRange):
            if ipOrRange.find("-") > -1:
                p = Parse.WithRegex("^(?P<base>\d{1,3}\.\d{1,3}\.\d{1,3})\.(?P<startIp>\d{1,3})\-(?P<endIp>\d{1,3})$",ipOrRange)
                return list(map(lambda x: "{0}.{1}".format(p.base,x),range(int(p.startIp), int(p.endIp) + 1)))
            if ipOrRange.find("*") > -1:
                ipOrRange = ipOrRange.replace("*","0/24")
            return list(map(lambda x: str(x), list(ipaddress.ip_network(u'%s' % ipOrRange).hosts())))
        return []
