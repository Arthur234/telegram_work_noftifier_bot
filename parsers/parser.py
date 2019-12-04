import datetime
from typing import Dict

import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, search_query):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}
        self.search_query = search_query
        self.vacancies = []

    def get_page_content(self, url: str):
        page = requests.get(url, headers=self.headers)
        return BeautifulSoup(page.content, 'html.parser')

    def get_page_content_not_verified(self, url: str):
        page = requests.get(url, verify=False, headers=self.headers)
        return BeautifulSoup(page.content, 'html.parser')

    def parse(self):
        pass

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        pass

