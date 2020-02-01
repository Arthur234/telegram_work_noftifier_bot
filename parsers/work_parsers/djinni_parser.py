import datetime
import locale

from parsers.parser import Parser
from constants import DJINNI_URL
from work_vacancy import Vacancy


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

            date = item.find('div', {'class': 'inbox-date pull-right'}).get_text().strip()
            date = self._transform_date(date)

            vacancy = Vacancy(title=title, company=company, link=link, date=date)
            self.vacancies.append(vacancy)

        return self.vacancies

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        locale.setlocale(locale.LC_ALL, ('UK', 'UTF8'))
        date = date.replace('\xa0', ' ')

        before_days = 0

        if date.startswith('вчора'):
            before_days = 1
        elif date[0].isdigit():
            pass

        return datetime.date.today() - datetime.timedelta(days=before_days)


if __name__ == '__main__':
    print(DjinniParser('product manager').parse())
