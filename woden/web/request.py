import requests
import ssl
from requests.adapters import HTTPAdapter
from requests.auth import HTTPDigestAuth
from requests.packages.urllib3.poolmanager import PoolManager
requests.packages.urllib3.disable_warnings()
from requests_ntlm import HttpNtlmAuth

class Request(object):

    defaults = {"verify" : False}

    @staticmethod
    def Get(url, params=None, **kwargs):
        return Request.Raw('get', url, params=params, **kwargs)

    @staticmethod
    def Options(url, **kwargs):
        return Request.Raw('options', url, **kwargs)

    @staticmethod
    def Head(url, **kwargs):
        return Request.Raw('head', url, **kwargs)

    @staticmethod
    def Post(url, data=None, json=None, **kwargs):
        return Request.Raw('post', url, data=data, json=json, **kwargs)

    @staticmethod
    def Put(url, data=None, **kwargs):
        return Request.Raw('put', url, data=data, **kwargs)

    @staticmethod
    def Patch(url, data=None, **kwargs):
        return Request.Raw('patch', url,  data=data, **kwargs)

    @staticmethod
    def Delete(url, **kwargs):
        return Request.Raw('delete', url, **kwargs)

    @staticmethod
    def Raw(method, url, **kwargs):

        session = requests.Session()

        for k,v in Request.defaults.iteritems():
            kwargs.setdefault(k,v)

        if method in ('head','options') :
            kwargs.setdefault('allow_redirects', True)

        try:
            return session.request(method,url,**kwargs)
        except Exception, ex:
            if type(ex).__name__ == "SSLError":
                session.mount('https://', SSLAdapter(ssl.PROTOCOL_TLSv1))
                return session.request(method,url,**kwargs)
            else:
                raise ex

    @staticmethod
    def NTLM(username, password):
        return HttpNtlmAuth(username, password)

    @staticmethod
    def Digest(username, password):
        return HTTPDigestAuth(username,password)


class SSLAdapter(HTTPAdapter):
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version

        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=self.ssl_version)
