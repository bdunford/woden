import re
import sys

class Parse(object):

    class Regex():
        LmNtlm = "(?P<user>.*)\:(?P<group>\d+)\:(?P<LM>[a-zA-z0-9]+)\:(?P<NTLM>[a-zA-z0-9]+)\:{3}"

    @staticmethod
    def WithRegex(expr, value):
        x = re.compile(expr)
        
        if sys.version_info[0] >= 3 and type(value) == bytes:
            value = value.decode()

        m = x.match(value)
        
        if m:
            o = Parse()
            if m.groupdict():
                for k, v in m.groupdict().items():
                    setattr(o, k, v)
            return o
        else:
            return None

    @staticmethod
    def File(filename, capture=None, delimeter=None):
        with open(filename) as f:
            for r in f:
                if capture:
                    v = Parse.WithRegex(capture,r)
                    if v:
                        yield v
                elif delimeter:
                    yield r.split(delimeter)
                else:
                    yield r.rstrip()
