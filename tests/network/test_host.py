import unittest

class TestHost(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.network import Host
        x = Host.Reverse("8.8.8.8")
        self.assertIn("google-public-dns-a.google.com",x)

suite = unittest.TestLoader().loadTestsFromTestCase(TestHost)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
