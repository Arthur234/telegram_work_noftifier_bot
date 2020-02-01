from queries.base_query import BaseQuery


class Project(BaseQuery):
    def __init__(self, title, link, date, offers_count):
        super().__init__(title, link, date)
        self.offers_count = offers_count

    def __repr__(self):
        return f'Project(' \
               f'title={self.title}, ' \
               f'link={self.link}' \
               f'date={self.date}, ' \
               f'offers_count={self.offers_count}, ' \
               f')'