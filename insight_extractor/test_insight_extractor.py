#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for insight_extractor

"""

import os
import shutil
import unittest
import pandas as pd
from insight_extractor.pipeline import extract_insights
from . import capture


class TestCensusLn(unittest.TestCase):

    def setUp(self):
        sentences = [
    'According to the most recent statistics, more than a million people a year are arrested for simple drug possession in the United States -- and more than half a million of those arrests are for marijuana possession.',
    'One study found that for cancer patients considering experimental chemotherapy, trust in their physician was one of the most important reasons they enrolled in a clinical trial -- on par with the belief that the treatment would be effective.',
    'Senate leaders were working to agree on a dual track to try the departing president at the same time it considered the agenda of the incoming one, an exercise never tried before.',
]
        self = sentences

    def tearDown(self):
        pass

    def test_insight_extractor(self):
        predictions = extract_insights(sentences)
        self.assertTrue(all(predictions == [0.28326818, 0.3710433, 0.9886193]))

if __name__ == '__main__':
    unittest.main()
