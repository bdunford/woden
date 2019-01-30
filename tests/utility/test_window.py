import unittest

class TestWindow(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.utility import Window
        w = Window(80)
        w.write(["AAA","AAA","AAA"])
        w.write(["BBB","BBB","BBB"])
        w.write(["CCC","CCC","CCC"])
        w.close()       
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestWindow)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
