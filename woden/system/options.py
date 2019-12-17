import re
import os
from optparse import OptionParser
from ..network.address import Address


#accepts usage as string example, options as list of dictionary, args and command line args
#validates args prints help and error if invalid then returns false else returs options object
class Options(object):

    @staticmethod
    def Get(options):
        valid = True

        # ADD Flag support parser.add_option("-v", action="store_true", dest="verbose")
        p = OptionParser()
        exflags = []
        exparms = []
        for o in options:
            h = (o["help"] + " default: %s" % o["default"]) if o["default"] else o["help"]
            if o["type"].lower() in ["flag","bool"]:
                exflags.append(o["arg"])
                p.add_option(o["arg"],"--%s" % o["dest"], action="store_true" if not o["default"] else "store_false", dest=o["dest"], help=h, default=o["default"])
            else:
                exparms.append("{0} [{1}]".format(o["arg"],o["dest"]))
                p.add_option(o["arg"],"--%s" % o["dest"], action="store", type=o["type"], dest=o["dest"], help=h, default=o["default"])

        p.set_usage("%prog {0} {1}".format(" ".join(exflags)," ".join(exparms)))
        (x,a) = p.parse_args()

        for o in options:
            v = x.ensure_value(o["dest"], None)
            if "required" in o and o["required"] and not v:
                valid = False
                p.error(o["required"])
            if v and "validate" in o and o["validate"] and not o["validate"](v):
                valid = False
                p.error(o["dest"] + " is invalid")

        x.parser = p
        return x if valid else False

    @staticmethod
    def target(required="A Valid IP address or range is required", default=None):
        return {"arg" : '-t',
                "dest" : "target",
                "type" : "string",
                "help" : "Ip Address or Range accepts wildcard (.*) and CIDR",
                "required" : required,
                "validate" : Address.IsRange,
                "default" : default
                }

    @staticmethod
    def host(required="A Valid Host IP address is required", default=None):
        return {"arg" : '-x',
                "dest" : "host",
                "type" : "string",
                "help" : "Host IP address",
                "required" : required,
                "validate" : Address.IsIP,
                "default" : default
                }

    @staticmethod
    def dictionary(required="An input Dictionary file is required",default=None):
        return {"arg" : '-d',
                "dest" : "dictionary",
                "type" : "string",
                "help" : "dictionary file to use as an input source",
                "required" : required,
                "validate" : os.path.exists,
                "default" : default
                }

    @staticmethod
    def port(required="A port number is required",default=None):
        return {"arg" : '-p',
                "dest" : "port",
                "type" : "int",
                "help" : "TCP or UDP port number to use",
                "required" : required,
                "validate" : None,
                "default" : default
                }

    @staticmethod
    def inputList(required="An input List is required",default=None):
        return {"arg" : '-i',
                "dest" : "inputList",
                "type" : "string",
                "help" : "File to use as an input source",
                "required" : required,
                "validate" : os.path.exists,
                "default" : default
                }
    @staticmethod
    def inputList(required=False,default="1-65535"):
        return {
            "arg" : '-p',
            "dest" : "ports",
            "type" : "string",
            "help" : "Port number(s) to use 443 or 22,443,80 or 1-1000",
            "required" : False,
            "validate" : None,
            "default" : default
        }

