import unittest
import time

class Marker(object):
    def __init__(self):
        self.results = []
    

marker = Marker()

def do_work(sleep_time, data):
    time.sleep(sleep_time)
    return data     

def report_work(data):
    marker.results.append(data)

class TestThreader(unittest.TestCase):
    
    def test_pass(self):
        import woden
        from woden.system import Threader

        threads = 100
        sleep_time = 5

        t = Threader(threads,report_work)
        for i in range(0,threads):
            t.add((do_work,{"sleep_time":sleep_time,"data":i}))
        st = time.time()    
        t.start()
        rt = int(time.time() - st)

        self.assertEqual(len(marker.results),threads)
        self.assertLessEqual(rt,sleep_time)






suite = unittest.TestLoader().loadTestsFromTestCase(TestThreader)
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
