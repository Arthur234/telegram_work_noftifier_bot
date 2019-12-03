import unittest

from utils.create_message import create_message
from vacancy import Vacancy


class TestMessage(unittest.TestCase):
    def test_message_creation(self):
        vacancy = Vacancy('title', 'company', 'link')
        my_message = f' Название вакансии: {vacancy.title} \n Компания: {vacancy.company} \n Ссылка: {vacancy.link}\n\n'

        self.assertEqual(create_message([vacancy]), my_message)
