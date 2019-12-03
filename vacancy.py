class Vacancy:
    def __init__(self, title: str, company: str, link: str):
        self.title = title
        self.company = company
        # self.date = date
        self.link = link

    def __repr__(self):
        return f'Vacancy(' \
               f'title={self.title}, ' \
               f'company={self.company}, ' \
               f'link={self.link}' \
               f')'


