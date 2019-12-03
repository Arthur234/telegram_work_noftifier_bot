import unittest

from parsers.parse_hh import HHParser


class TestRabotaUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(HHParser().parse())
