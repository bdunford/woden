class Header(object):
    browsers = {
        "IE9" : {"user-agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"},
        "IE10" : {"user-agent" : "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)"},
        "IE11" : {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"},
        "Safari" : {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5"},
        "Chrome" : {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
        "FireFox" : {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"},
        "Chrome-osx" : {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"},
        "FireFox-osx" : {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:33.0) Gecko/20100101 Firefox/33.0"},
        "iOS" : {"user-agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 10_10_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4"},
        "Android" : {"user-agent" : "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"}
    }

    default = {
        "user-agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "accept" : "*/*",
        "accept-encoding" : "gzip, deflate",
        "accept-language" :"en-US,en;q=0.8"
    }

    @classmethod
    def Get(self,name):
        h = self.default
        if name in self.browsers:
            h["user-agent"] = self.browsers[name]["user-agent"]

        return h


    @classmethod
    def Browsers(self):
        for k in self.browsers:
            yield k
