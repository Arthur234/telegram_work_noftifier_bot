from parsers.parser import Parser
from constants import WORKUA_URL
from vacancy import Vacancy


class WorkUaParser(Parser):
    def __init__(self, search_query):
        super().__init__(search_query)

    def parse(self):
        soup = self.get_page_content(WORKUA_URL.format(self.search_query))

        cards = soup.findAll('div', {'class': 'card card-hover card-visited wordwrap job-link'})

        for card in cards:
            title = card.find('h2').find('a').get_text()
            link = 'https://www.work.ua' + card.find('h2').find('a')['href']
            company = card.find('div', {'class': 'add-top-xs'}).find('span').get_text()

            vacancy = Vacancy(title=title, company=company, link=link)
            self.vacancies.append(vacancy)

        return self.vacancies


if __name__ == '__main__':
    vacancies = WorkUaParser().parse()
    print(vacancies)
