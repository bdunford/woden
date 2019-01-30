import socket
import ssl

class Port():

    def __init__(self, ip, port, timeout=1, ssl_wrap=False):
        self._address = (ip,int(port))
        self._error = None

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        if ssl_wrap:
            self._socket = ssl.wrap_socket(sock)
        else:
            self._socket = sock


    @property
    def error(self):
        return self._error

    @property
    def socket(self):
        return self._socket

    @property
    def localport(self):
        return self._socket.getsockname()[1]

    def connect(self):
        try:
            self._socket.connect(self._address);
            return True
        except socket.error, e:
            self.error = e
            return False

    def disconnect(self):
        self._socket.close()

    def send(self, data, lt='\r\n'):
        if lt:
            data += lt
        self._socket.send(data)
        return self.read()

    def read(self, chunk=1024):
        data = ""
        try:
            while True:
                part = self._socket.recv(chunk)
                if part:
                    data += part
                if len(part) < chunk:
                    break
        except:
            pass
        finally:
            return data.rstrip() if len(data) > 0 else None

    @classmethod
    def Sniff(self, ip, port, banner=True):
        p = Port(ip,port,1)
        if p.connect():
            result = p.read() if banner else True
            p.disconnect()
            return result if result else True
        else:
            p = None
            return False

    @classmethod
    def Connect(self, ip, port, timeout=1, ssl_wrap=False):
        p = Port(ip,port,timeout,ssl_wrap)
        if p.connect():
            return p
        else:
            return None
