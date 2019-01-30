class Lists(object):

    @staticmethod
    def First(items):
        if items:
            return list(items)[0] if len(items) > 0 else None
        else:
            return None

    
