from parsers.parser import Parser
from constants import RABOTAUA_URL
from vacancy import Vacancy


class RabotaUaParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(RABOTAUA_URL.format(self.search_query))

        items = soup.findAll('article', {'class': 'f-vacancylist-vacancyblock'})

        for item in items:
            title = item.find('a', {'class': 'f-visited-enable ga_listing'}).get_text().strip()
            link = 'https://rabota.ua' + item.find('a', {'class': 'f-visited-enable ga_listing'})['href'].strip()
            company = item.find('a', {
                'class': 'f-text-dark-bluegray f-visited-enable'
            }).get_text().strip()

            vacancy = Vacancy(title=title, link=link, company=company)
            self.vacancies.append(vacancy)

        return self.vacancies


if __name__ == '__main__':
    vacancies = RabotaUaParser().parse()
    print(vacancies)
