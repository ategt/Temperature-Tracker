import unittest

from possible import SegmentationDetector

import re
import os

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

    def test_validateSegmentor(self):
        TEMPERATURE_DATA_FILE_REGEX = re.compile(r"temp\-(?:\d+)\-(?:\d+)\-(?:\d+)\.txt")

        for file in os.listdir("data"):
            if TEMPERATURE_DATA_FILE_REGEX.match(file):
                path = os.path.join("data", file)

                detector = SegmentationDetector(path, 25000)

                inflection_segments = detector.getSegmentInflections(30)

                self.assertTrue(len(inflection_segments) >= 18, f"Minimum Acceptable Segments - {path}")
                self.assertTrue(len(inflection_segments) <= 30, f"Maximum Acceptable Segments - {path}")

if __name__ == '__main__':
    unittest.main()