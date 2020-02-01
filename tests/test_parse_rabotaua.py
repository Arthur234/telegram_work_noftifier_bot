import unittest

from parsers.work_parsers.rabotaua_parser import RabotaUaParser


class TestRabotaUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(RabotaUaParser().parse())
