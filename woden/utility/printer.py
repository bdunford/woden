
class Printer(object):
    @staticmethod
    def HR():
        print("--------------------------------------------------------------------------------")

    @staticmethod
    def Print(mixed):
        if mixed:
            if isinstance(mixed, (list,tuple)):
                for r in mixed:
                    print(r)
                return

            if isinstance(mixed,dict):
                for k in reversed(mixed.keys()):
                    if isinstance(mixed[k], (list, tuple)):
                        print("%s: " % k)
                        for v in mixed[k]:
                            print(v)
                    else:
                        print("{0}: {1}".format(k, mixed[k]))
                return
            print(mixed)

    @staticmethod
    def PrintWebResponse(r, content=True):
        Printer.HR()
        Printer.Print({"stats" : r.status_code})
        Printer.Print({"url" : r.url})
        Printer.Print("-----------Headers------------")
        Printer.Print(dict(r.headers))
        if content:
            Printer.Print("-----------Content------------")
            print(r.text)
        Printer.HR()
