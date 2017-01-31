import unittest
import os

import sox.tools


def relpath(f):
    return os.path.join(os.path.dirname(__file__), f)


INPUT_FILE = relpath('data/input.wav')
OUTPUT_FILE = relpath('data/output.wav')


class TestTools(unittest.TestCase):

    def test_trim(self):
        self.assertEqual(sox.tools.trim(INPUT_FILE, OUTPUT_FILE, 0, 1.5))
