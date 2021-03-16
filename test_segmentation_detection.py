import unittest

from possible import SegmentationDetector

class TestSegmentationDetection(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_segmenter(self):
        detector = SegmentationDetector("data/temp-2021-03-16.txt")

        inflection_segments = detector.getSegmentInflections(30)

        self.assertTrue(len(inflection_segments) >= 18, "Minimum Acceptable Segments")
        self.assertTrue(len(inflection_segments) <= 30, "Maximum Acceptable Segments")

if __name__ == '__main__':
    unittest.main()