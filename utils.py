from datetime import time
from typing import List
from concurrent.futures.thread import ThreadPoolExecutor

from queries.project import Project
from queries.vacancy import Vacancy


def create_work_message(vacancies: List[Vacancy]) -> str:
    message = ''
    for vacancy in vacancies:
        message += f'*{vacancy.date}*\n' \
                   f'*{vacancy.company}*: [{vacancy.title}]({vacancy.link})\n\n'
    return message


def create_freelance_message(projects: List[Project]) -> str:
    message = ''
    for project in projects:
        message += f'*{project.date}*\n' \
                   f'[{project.title}]({project.link})\n' \
                   f'*{project.offers_count} Предложений*\n\n'
    return message


def start_parser(parser):
    data = parser.parse()
    return data


def get_queried_data(search_query, parsers):
    parsers = [parser(search_query) for parser in parsers]

    with ThreadPoolExecutor(max_workers=4) as executor:
        data = executor.map(start_parser, parsers)

    vacancies = []
    for nested in data:
        for vacancy in nested:
            vacancies.append(vacancy)
    vacancies.sort(key=lambda x: x.date, reverse=True)

    return vacancies


if __name__ == '__main__':
    pass
    # print(get_vacancies('Trainee'))
