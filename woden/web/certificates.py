import ssl
import re
from OpenSSL import crypto
from ..utility import Parse, Lists
ssl._DEFAULT_CIPHERS = 'DEFAULT:!aNULL:!eNULL:!LOW:!EXPORT:!SSLv2'

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
            map(lambda m: m[1], filter(lambda f: len(f) == 2 and f[0] == "CN", self.openSSL.get_subject().get_components())))
        alts = Lists.First(filter(lambda x: x.get_short_name() == 'subjectAltName',map(lambda i: self.openSSL.get_extension(i), range(self.openSSL.get_extension_count()))))
        if alts:
            return list(set(hn + re.sub(r"DNS\:","",alts.__str__()).split(', ')))
        else:
            return hn

    @staticmethod
    def Get(ip, port):
        pem = None
        try:
            pem = ssl.get_server_certificate((ip,int(port)))
        except:
            pem = ssl.get_server_certificate(
                (ip,int(port)),
                ssl_version=ssl.PROTOCOL_TLSv1
            )
        finally:
            if pem:
                return Certificate(pem)
            else:
                return None
