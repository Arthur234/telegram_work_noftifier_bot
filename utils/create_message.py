from typing import List
from vacancy import Vacancy


def create_message(vacancies: List[Vacancy]) -> str:
    message = ''

    for vacancy in vacancies:
        message += f'*{vacancy.date}*\n' \
                   f'*{vacancy.company}*: [{vacancy.title}]({vacancy.link})\n\n' \

    return message
