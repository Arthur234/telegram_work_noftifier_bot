class Vacancy:
    def __init__(self, title: str, company: str, link: str, date=None):
        self.title = title
        self.company = company
        self.date = date
        self.link = link
        self.provider = None

    def __repr__(self):
        return f'Vacancy(' \
               f'title={self.title}, ' \
               f'company={self.company}, ' \
               f'date={self.date}, ' \
               f'link={self.link}' \
               f')'


