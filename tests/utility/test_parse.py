import unittest

class TestParse(unittest.TestCase):

    def test_pass(self):
        import woden
        from woden.utility import Parse
        
        o = Parse.WithRegex("(?P<numbers>\d+)\:(?P<letters>[A-Z]+)","123:ABC")
        self.assertEqual(o.numbers,"123")
        self.assertEqual(o.letters,"ABC")
        
        lines = list(Parse.File(__file__,"class\s(?P<name>[A-Za-z]+).*"))
        self.assertEqual(len(lines),1)
        self.assertEqual(lines[0].name,"TestParse")


        
            

suite = unittest.TestLoader().loadTestsFromTestCase(TestParse)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
