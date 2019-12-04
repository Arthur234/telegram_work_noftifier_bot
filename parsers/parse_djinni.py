import datetime
import locale

from parsers.parser import Parser
from constants import DJINNI_URL
from vacancy import Vacancy


class DjinniParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(DJINNI_URL.format(self.search_query))

        items = soup.findAll('li', {'class': 'list-jobs__item'})

        for item in items:
            title = item.find('div', {'class': 'list-jobs__title'}).find('a').get_text()
            link = 'https://djinni.co' + item.find('div', {'class': 'list-jobs__title'}).find('a')['href']
            company = item.find('div', {
                'class': 'list-jobs__details'
            }).findAll('a')[1]['href']

            try:
                company = company.split('-at-')[1][:-1]
            except IndexError as e:
                company = company.split('-')[-1][:-1]

            vacancy = Vacancy(title=title, company=company, link=link)
            self.vacancies.append(vacancy)

        return self.vacancies

    def _transform_date(date: str) -> datetime.date:
        locale.setlocale(locale.LC_ALL, ('UK', 'UTF8'))


if __name__ == '__main__':
    print(DjinniParser('python').parse())
