import operator
from concurrent.futures.thread import ThreadPoolExecutor

from parsers.parse_workua import WorkUaParser
from parsers.parse_rabotaua import RabotaUaParser
from parsers.parse_hh import HHParser
from parsers.parse_djinni import DjinniParser


def start_parser(parser):
    data = parser.parse()
    return data


def get_vacancies(search_query):
    parsers = [WorkUaParser, RabotaUaParser, HHParser, DjinniParser]
    parsers = [parser(search_query) for parser in parsers]

    with ThreadPoolExecutor(max_workers=4) as executor:
        data = executor.map(start_parser, parsers)

    vacancies = []
    for nested in data:
        for vacancy in nested:
            vacancies.append(vacancy)

    vacancies.sort(key=lambda x: x.date, reverse=True)

    print(vacancies)
    return vacancies


if __name__ == '__main__':
    print(get_vacancies('Trainee'))
