import unittest
from parsers.parse_workua import WorkUaParser


class TestWorkUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(WorkUaParser().parse())
