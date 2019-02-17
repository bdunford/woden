import unittest

class TestPort(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.network import Port
        p = Port.Connect("google.com",80)
        x = p.send("GET / HTTP/1.1\n\n")
        self.assertIn("HTTP/1.1 200 OK",x)
        p.disconnect()



suite = unittest.TestLoader().loadTestsFromTestCase(TestPort)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
