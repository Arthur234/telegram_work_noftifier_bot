import unittest
from parsers.work_parsers.workua_parser import WorkUaParser


class TestWorkUaParser(unittest.TestCase):
    def test_parsing(self):
        self.assertIsNotNone(WorkUaParser().parse())
