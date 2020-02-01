from typing import List
from concurrent.futures.thread import ThreadPoolExecutor

from work_vacancy import Vacancy
import parsers.work_parsers as wp


def create_message(vacancies: List[Vacancy]) -> str:
    message = ''
    for vacancy in vacancies:
        message += f'*{vacancy.date}*\n' \
                   f'*{vacancy.company}*: [{vacancy.title}]({vacancy.link})\n\n'
    return message


def start_parser(parser):
    data = parser.parse()
    return data


def get_vacancies(search_query):
    parsers = [parser(search_query) for parser in
               [wp.WorkUaParser, wp.RabotaUaParser, wp.HHParser, wp.DjinniParser]]

    with ThreadPoolExecutor(max_workers=4) as executor:
        data = executor.map(start_parser, parsers)

    vacancies = []
    for nested in data:
        for vacancy in nested:
            vacancies.append(vacancy)
    vacancies.sort(key=lambda x: x.date, reverse=True)

    return vacancies


if __name__ == '__main__':
    print(get_vacancies('Trainee'))
