import unittest

from parsers.work_parsers.hh_parser import HHParser


class TestRabotaUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(HHParser().parse())
