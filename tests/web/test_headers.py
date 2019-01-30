import unittest

class TestHeader(unittest.TestCase):
    
    def test_pass(self):
        import woden
        from woden.web import Header
        h = Header.Get("IE") 
        self.assertIn("user-agent",h)
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestHeader)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
