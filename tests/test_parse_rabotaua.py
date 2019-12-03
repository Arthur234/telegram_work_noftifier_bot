import unittest

from parsers.parse_rabotaua import RabotaUaParser


class TestRabotaUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(RabotaUaParser().parse())
