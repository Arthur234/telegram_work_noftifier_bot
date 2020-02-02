import datetime

from parsers.parser import Parser
from constants import FLRU_URL
from queries.project import Project


class FlRuParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(FLRU_URL.format(self.search_query))

        items = soup.findAll('div', {'class': 'search-lenta-item c'})
        for item in items:
            title = item.find('h3').find('a').get_text()
            link = 'https://www.fl.ru' + item.find('h3').find('a')['href']
            offers_count = item.find('span', {'class': 'search-answer'}).find('a').get_text().split(' ')[0]
            date = self._transform_date(item.find('ul', {'class': 'search-meta'}).findAll('li')[-1].get_text())

            self.projects.append(Project(
                title=title, link=link, offers_count=offers_count, date=date))
        return self.projects

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        number, definition = date.split(' ')[:2]
        if definition[0].isdigit():
            date = datetime.datetime.strptime(number, '%d.%m.%Y').date()
        else:
            date = datetime.datetime.today().date()
        return date


if __name__ == '__main__':
    print(FlRuParser('js').parse())