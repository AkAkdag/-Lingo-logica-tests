import unittest
import time
from mytimer import Timer

class TimerTests(unittest.TestCase):
    
    # Start functie testen
    def test_start(self):
        timer = Timer()
        timer.start()
        self.assertIsNotNone(timer.start_time)

    # Reset functie testen
    def test_reset(self):
        timer = Timer()
        timer.start()
        time.sleep(1)
        timer.reset()
        self.assertIsNone(timer.start_time)
        self.assertEqual(timer.get_verstreken_time(), 0)

    # Functie verstreken tijd testen
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

if __name__ == '__main__':
    unittest.main()
