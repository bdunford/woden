import unittest

class TestGeneric(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.utility import Generic
        g = Generic(id=1,name="test")
        self.assertEqual(g.id,1)
        self.assertEqual(g.name,"test")

suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneric)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
