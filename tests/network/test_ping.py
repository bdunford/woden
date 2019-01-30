import unittest

class TestPing(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.network import Ping
        x = Ping.Run("8.8.8.8")
        self.assertTrue(x.up)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPing)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
