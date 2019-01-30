import unittest
import sys

class TestOptions(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.system import Options
        target = "192.168.1.*"
        olg_argv = sys.argv

        sys.argv +=  ["-t",target]
        o = Options.Get([Options.target()])
        self.assertEqual(o.target,target)







suite = unittest.TestLoader().loadTestsFromTestCase(TestOptions)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
