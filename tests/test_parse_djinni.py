import unittest

from parsers.parse_djinni import DjinniParser


class TestRabotaUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(DjinniParser('python').parse())
