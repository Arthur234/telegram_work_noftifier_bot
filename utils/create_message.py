from typing import List
from vacancy import Vacancy


def create_message(vacancies: List[Vacancy]) -> str:
    message = ''

    for vacancy in vacancies:
        message += f'*Название вакансии*: {vacancy.title} \n*Компания*: {vacancy.company} \n*Ссылка*: {vacancy.link}\n\n'

    return message
