import unittest

class TestPrinter(unittest.TestCase):

    def test_pass(self):
        import requests
        import woden
        from woden.utility import Printer
        Printer.Print(["test","printer"])
        Printer.PrintWebResponse(requests.get("https://www.google.com"),False)
        self.assertEqual(1,1)


suite = unittest.TestLoader().loadTestsFromTestCase(TestPrinter)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
