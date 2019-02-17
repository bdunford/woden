import re
import subprocess
import string
import sys
from threading import Timer
from ..utility import Parse

class Runner(object):

    def __init__(self,results):
        self.results = results


    def get(self, expr, first=True):
        results = filter(lambda f: f, map(lambda m: Parse.WithRegex(expr,m), self.results))
        return results if not first else lists.first(results)

    @staticmethod
    def Run(program, options, timeout=None):
        cmd = [program] + options
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        timer = Timer(timeout, lambda p: p.terminate(), [p]) if timeout else None

        if timer:
            timer.start()

        
        r = None 
        if sys.version_info[0] < 3:
            r = map(
                    lambda x: x.rstrip().replace("\t","     "), 
                    iter(p.stdout.readline, b'')
                )
        else: 
            r = map(
                    lambda x: x.decode().rstrip().replace("\t","     "), 
                    iter(p.stdout.readline, b'')
                )

            


        


        if timer:
            timer.cancel()

        return Runner(list(r))
