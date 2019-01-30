import unittest

class TestWriter(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.utility import Writer
        f = "./testdata/test.txt"
        Writer.Replace(f,"A"*500)
        Writer.Append(f,"B"*500)
        self.assertTrue(True)


suite = unittest.TestLoader().loadTestsFromTestCase(TestWriter)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
