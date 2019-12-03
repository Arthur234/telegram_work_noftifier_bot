from parsers.parser import Parser
from constants import HH_URL
from vacancy import Vacancy


class HHParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(HH_URL.format(self.search_query))

        items = soup.findAll('div', {'class': 'vacancy-serp-item'})

        for item in items:
            title = item.find('a', {'class': 'bloko-link HH-LinkModifier'}).get_text()
            link = item.find('a', {'class': 'bloko-link HH-LinkModifier'})['href']
            company = item.find('a', {
                'class': 'bloko-link bloko-link_secondary HH-AnonymousIndexAnalytics-Recommended-Company'
            }).get_text()

            vacancy = Vacancy(title=title, company=company, link=link)
            self.vacancies.append(vacancy)

        return self.vacancies


if __name__ == '__main__':
    print(HHParser().parse())
