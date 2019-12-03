import datetime

from parsers.parser import Parser
from constants import WORKUA_URL
from vacancy import Vacancy


class WorkUaParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(WORKUA_URL.format(self.search_query))

        cards = soup.findAll('div', {'class': 'card card-hover card-visited wordwrap job-link'})
        hot_cards = soup.findAll('div', {'class': 'card card-hover card-visited wordwrap job-link js-hot-block'})

        for card in cards + hot_cards:
            title = card.find('h2').find('a').get_text()
            link = 'https://www.work.ua' + card.find('h2').find('a')['href']
            company = card.find('div', {'class': 'add-top-xs'}).find('span').get_text()

            try:
                date = card.find('span', {'class': 'text-muted small'}).get_text()
                date = self._transform_date(date)
            except AttributeError:
                date = datetime.date.today()

            vacancy = Vacancy(title=title, company=company, link=link, date=date)
            self.vacancies.append(vacancy)

        return self.vacancies

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        days_before = 0
        hours_before = 0

        if date.startswith('Вчера'):
            days_before = 1
        else:
            number, definition = date.split('\xa0')[:2]
            number = int(number)

            if definition.startswith('дня'):
                days_before = number
            elif definition.startswith('нед'):
                days_before = number * 7
            elif definition.startswith('ч'):
                hours_before = number

        return datetime.date.today() - datetime.timedelta(days=days_before, hours=hours_before)


if __name__ == '__main__':
    vacancies = WorkUaParser('Менеджер').parse()
    print(vacancies)
