from concurrent.futures.thread import ThreadPoolExecutor

from parsers.parse_workua import WorkUaParser
from parsers.parse_rabotaua import RabotaUaParser
from parsers.parse_hh import HHParser
from parsers.parse_djinni import DjinniParser


def start_parser(parser):
    data = parser.parse()
    return data


def get_vacancies(search_query):
    parsers = [WorkUaParser, HHParser, DjinniParser, RabotaUaParser]
    parsers = [parser(search_query) for parser in parsers]

    with ThreadPoolExecutor(max_workers=4) as executor:
        data = executor.map(start_parser, parsers)

    vacancies = []
    for nested in data:
        for vacancy in nested:
            vacancies.append(vacancy)

    return vacancies


if __name__ == '__main__':
    get_vacancies()
