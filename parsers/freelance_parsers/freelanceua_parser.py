import datetime

from queries.project import Project
from parsers.parser import Parser
from constants import FREELANCEUA_URL


class FreelanceUaParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(FREELANCEUA_URL.format(self.search_query))
        items = soup.findAll('li', {'class': 'media'})

        for item in items:
            title = item.find('a').get_text()
            link = item.find('a')['href']

            date = self._transform_date(item.find('i', {'class': 'fa fa-clock-o'}).\
                find_parent('li').get_text().strip())

            offers_count = int(
                item.find('ul').find('span').get_text().split(' ')[0])

            self.projects.append(Project(
                title=title, link=link, offers_count=offers_count, date=date))
        return self.projects

    @staticmethod
    def _transform_date(date: str) -> datetime.date:
        # days_before = 1 if date.startswith('вч') else \
        #         int(date.split(' ')[0]) if date.startswith('дня') \
        #         else 30 * int(date.split(' ')[0])
        days_before = 0

        try:
            number, definition = date.split(' ')[:2]
        except ValueError:
            definition = date

        if definition.startswith('вчера'):
            days_before = 1
        elif definition.startswith('дн'):
            days_before = int(number)
        elif definition.startswith('мес'):
            days_before = int(number) * 30

        return datetime.date.today() - datetime.timedelta(days=days_before)


if __name__ == '__main__':
    FreelanceUaParser('python').parse()