import unittest

from parsers.work_parsers.djinni_parser import DjinniParser


class TestRabotaUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(DjinniParser('python').parse())
