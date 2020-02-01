from queries.base_query import BaseQuery


class Vacancy(BaseQuery):
    def __init__(self, title, link, date, company):
        super().__init__(title, link, date)
        self.company = company

    def __repr__(self):
        return f'Vacancy(' \
               f'title={self.title}, ' \
               f'link={self.link}' \
               f'date={self.date}, ' \
               f'company={self.company}, ' \
               f')'
