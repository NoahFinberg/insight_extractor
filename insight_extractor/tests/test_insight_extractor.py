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


class TestInsightExtractor(unittest.TestCase):

    def setUp(self):
        self.sentences = [
    'According to the most recent statistics, more than a million people a year are arrested for simple drug possession in the United States -- and more than half a million of those arrests are for marijuana possession.',
    'One study found that for cancer patients considering experimental chemotherapy, trust in their physician was one of the most important reasons they enrolled in a clinical trial -- on par with the belief that the treatment would be effective.',
    'Senate leaders were working to agree on a dual track to try the departing president at the same time it considered the agenda of the incoming one, an exercise never tried before.',
]

    def tearDown(self):
        pass

    def test_insight_extractor(self):
        probs_insight = extract_insights(self.sentences)
        ref = [0.7167318, 0.6289567, 0.01138071]
        self.assertTrue(probs_insight, ref)

if __name__ == '__main__':
    unittest.main()

