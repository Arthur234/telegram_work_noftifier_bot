import datetime
import locale

from parsers.parser import Parser
from constants import HH_URL
from vacancy import Vacancy


class HHParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(HH_URL.format(self.search_query))

        items = soup.findAll('div', {'class': 'vacancy-serp-item'})
        items_premium = soup.findAll('div', {'class': 'vacancy-serp-item  vacancy-serp-item_premium'})

        for item in items + items_premium:
            title = item.find('a', {'class': 'bloko-link HH-LinkModifier'}).get_text()
            link = item.find('a', {'class': 'bloko-link HH-LinkModifier'})['href']
            company = item.find('a', {
                'class': 'bloko-link bloko-link_secondary HH-AnonymousIndexAnalytics-Recommended-Company'
            }).get_text()

            try:
                date = item.find('span', {'class': 'vacancy-serp-item__publication-date'}).get_text()
                date = self._transform_date(date)
            except AttributeError:
                date = datetime.date.today()

            vacancy = Vacancy(title=title, company=company, link=link, date=date)
            self.vacancies.append(vacancy)

        return self.vacancies

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        locale.setlocale(locale.LC_ALL, ('RU', 'UTF8'))

        date = date.replace('\xa0', ' ')
        date = datetime.datetime.strptime(date, '%d %B').date()
        date = date.replace(year=datetime.date.today().year)

        return date


if __name__ == '__main__':
    print(HHParser('python').parse())
