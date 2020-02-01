import datetime

from parsers.parser import Parser
from config import RABOTAUA_URL
from vacancy import Vacancy


class RabotaUaParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content_not_verified(RABOTAUA_URL.format(self.search_query))
        items = soup.findAll('article', {'class': 'f-vacancylist-vacancyblock'})

        for item in items:
            title = item.find('a', {'class': 'f-visited-enable ga_listing'}).get_text().strip()
            link = 'https://rabota.ua' + item.find('a', {'class': 'f-visited-enable ga_listing'})['href'].strip()
            company = item.find('a', {
                'class': 'f-text-dark-bluegray f-visited-enable'
            }).get_text().strip()

            try:
                date = item.find('p', {'class': 'f-vacancylist-agotime f-text-light-gray fd-craftsmen'}).get_text()
                date = self._transform_date(date)
            except AttributeError:
                date = datetime.date.today()

            vacancy = Vacancy(title=title, link=link, company=company, date=date)
            self.vacancies.append(vacancy)

        return self.vacancies

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        days_before = 0
        hours_before = 0

        number, definition = date.split('\xa0')[:2]
        number = int(number)

        if definition.startswith('час'):
            hours_before = number
        elif definition.startswith('д'):
            days_before = number
        elif definition.startswith('н'):
            days_before = number * 7

        return datetime.date.today() - datetime.timedelta(days=days_before, hours=hours_before)


if __name__ == '__main__':
    vacancies = RabotaUaParser('Python').parse()
    print(vacancies)
