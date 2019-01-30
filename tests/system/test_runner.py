import unittest

class TestRunner(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.system import Runner
        
        o = Runner.Run("python",["--version"])
        self.assertTrue(len(o.results) > 0)
        self.assertIn("python", o.results[0].lower())
        

suite = unittest.TestLoader().loadTestsFromTestCase(TestRunner)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
