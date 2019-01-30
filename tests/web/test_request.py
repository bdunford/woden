import unittest

class TestRequest(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.web import Request
        r = Request.Get("https://www.google.com/")
        self.assertEqual(r.status_code,200)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRequest)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
