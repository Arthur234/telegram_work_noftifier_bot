import datetime
from typing import Dict

import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, search_query):
        self.search_query = search_query
        self.vacancies = []

    def get_page_content(self, url: str):
        page = requests.get(url, verify=False)
        return BeautifulSoup(page.content, 'html.parser')

    def parse(self):
        pass

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        pass

