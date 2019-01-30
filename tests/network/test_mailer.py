import unittest
import getpass

class TestMailer(unittest.TestCase):

    def test_pass(self):
        import woden 
        from woden.network import Mailer
        sender = "john@localhost.com"
        recipients=["john@yahoo.com"]
        content = "<html><h1>TEST</h1></html>"
        subject = "10 am meeting"
        attachment = __file__ 
        err = Mailer.Send(sender, recipients, subject, content, True, attachment, False, 1)
        if err: 
            print("Mailer: {0}".format(err))
        
        self.assertTrue(True)

        relay={
            "host" : "127.0.0.1",
            "port" : 25,
            "ssl" : False
        }
        err = Mailer.Send(sender, recipients, subject, content, True, attachment, relay, 1)
        if err: 
            print("Mailer: {0}".format(err))
        self.assertTrue(True)
            
suite = unittest.TestLoader().loadTestsFromTestCase(TestMailer)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
