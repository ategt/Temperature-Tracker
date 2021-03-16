import unittest

from tabata_timer import TabataTimer
from time import sleep

class TestTabataTimer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.timer.stop()

    def test_start_many_timers(self):
        self.timer = TabataTimer()

        self.timer.start()

        with self.assertRaises(Exception):
            self.timer.start()

        self.timer.stop()
        self.timer.start()

        with self.assertRaises(Exception):
            self.timer.start()

    def test_getPid(self):
        self.timer = TabataTimer()

        self.timer.getPid()
        self.timer.start()
        self.timer.getPid()

    def test_stop_without_start(self):
        self.timer = TabataTimer()

        self.timer.stop()

if __name__ == '__main__':
    unittest.main()