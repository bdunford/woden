import ssl
import re
import socket
from OpenSSL import crypto
from ..utility import Parse, Lists
ssl._DEFAULT_CIPHERS = 'DEFAULT:!aNULL:!eNULL:!LOW:!EXPORT:!SSLv2'



#TODO rewrite using https://pypi.org/project/pem/
class Certificate(object):

    def __init__(self, pemCert):
        self.pem = pemCert
        self.openSSL = crypto.load_certificate(crypto.FILETYPE_PEM, pemCert)
        sc = self.openSSL.get_subject()
        ir = self.openSSL.get_issuer()

        self.country = sc.countryName
        self.state = sc.stateOrProvinceName
        self.locality = sc.localityName
        self.org = sc.organizationName
        self.orgUnit = sc.organizationalUnitName
        self.commonName = sc.commonName
        self.email = sc.emailAddress
        self.issuer = {
            "country" : ir.countryName, 
            "name" : ir.commonName, 
            "company" : ir.organizationName
        }
        self.bits = self.openSSL.get_pubkey().bits()
        self.expired = self.openSSL.has_expired()
        self.issued = self.openSSL.get_notBefore()
        self.expires = self.openSSL.get_notAfter()

    def hosts(self):
        hn = list(
            map(lambda m: m[1], filter(lambda f: len(f) == 2 and f[0] == b"CN", self.openSSL.get_subject().get_components())))
        alts = Lists.First(list(filter(lambda x: x.get_short_name() == b'subjectAltName',map(lambda i: self.openSSL.get_extension(i), range(self.openSSL.get_extension_count())))))
        if alts:
            return list(set(hn + re.sub(r"DNS\:","",alts.__str__()).split(', ')))
        else:
            return hn

    @staticmethod
    def Get(ip, port):
        pem = None
        try:
            address = (ip,int(port))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            x = ssl.wrap_socket(sock)
            x.connect(address)
            x.do_handshake()
            pem = ssl.get_server_certificate(address)
            x.close()
            return Certificate(pem)
        except:
            return None
        
