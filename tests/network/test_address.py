import unittest

class TestAddress(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.network import Address
        self.assertEquals(254,len(Address.All("192.168.1.*")))
        self.assertEquals(65534,len(Address.All("192.168.0.0/16")))

suite = unittest.TestLoader().loadTestsFromTestCase(TestAddress)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
