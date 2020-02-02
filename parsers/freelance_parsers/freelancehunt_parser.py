import datetime
import locale

from parsers.parser import Parser
from constants import FREELANCHUNT_URL
from queries.project import Project


class FreelanceHuntParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(FREELANCHUNT_URL.format(self.search_query))

        items = soup.findAll('tr')
        for item in items:
            title = item.find('td', {'class': 'left'}).find('a').get_text()
            link = item.find('td', {'class': 'left'}).find('a')['href']
            day = item.find('div', {'class': 'with-tooltip calendar'}).find('h2').get_text()
            month = item.find('div', {'class': 'with-tooltip calendar'}).find('h5').get_text()
            offers_count = item.find('td', {'class': 'text-center hidden-xs'}).find('a').get_text()

            date = self._transform_date(f'{day} {month}')

            self.projects.append(Project(
                title=title, link=link, offers_count=offers_count, date=date))
        return self.projects

    @staticmethod
    def _transform_date(date) -> datetime.date:
        locale.setlocale(locale.LC_ALL, ('RU', 'UTF8'))

        date = datetime.datetime.strptime(date, '%d %b').date()
        return date.replace(year=datetime.date.today().year)


if __name__ == '__main__':
    FreelanceHuntParser('python').parse()
