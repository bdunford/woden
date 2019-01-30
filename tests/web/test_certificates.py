import unittest

class TestCertificate(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.web import Certificate
        c = Certificate.Get("yahoo.com",443)
        self.assertTrue(isinstance(c,Certificate))
        self.assertIn("www.yahoo.com", c.hosts())
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestCertificate)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
