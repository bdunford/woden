import unittest

class TestLists(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.utility import Lists
        a = Lists.First([1,2,3,4,5,6,7,8])
        self.assertEqual(a,1)







suite = unittest.TestLoader().loadTestsFromTestCase(TestLists)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
