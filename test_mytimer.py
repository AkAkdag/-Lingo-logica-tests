import unittest
import time
from mytimer import Timer

class TimerTests(unittest.TestCase):
    def test_start(self):
        timer = Timer()
        timer.start()
        self.assertIsNotNone(timer.start_time)

    def test_reset(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        timer.reset()
        self.assertIsNone(timer.start_time)
        self.assertEqual(timer.get_verstreken_time(), 0)

    def test_get_verstreken_time(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        verstreken_time = timer.get_verstreken_time()
        self.assertGreater(verstreken_time, 0)

    def test_get_verstreken_time_without_start(self):
        timer = Timer()
        verstreken_time = timer.get_verstreken_time()
        self.assertEqual(verstreken_time, 0)

    def test_reken_score(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        score = timer.reken_score(5)
        self.assertGreater(score, 0)

if __name__ == '__main__':
    unittest.main()
