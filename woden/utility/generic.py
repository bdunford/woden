import json
class Generic(object):

    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return json.dumps(self.__dict__,indent=4)

    def __repr__(self):
        return self.__str__()
