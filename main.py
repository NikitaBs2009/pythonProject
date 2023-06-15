import os
import requests
from itertools import count
from math import ceil
from dotenv import load_dotenv
from terminaltables import AsciiTable


TITLE_SJ = 'superjob_Moscow'
TITLE_HH = 'headhunter_Moscow'
def get_language_hh_vacancies(language):
    sum_salary = 0
    vacancies_processed = 0
    for page_number in count(0, 1):
        params = {
            'specialization': '1.221',
            'area': '1',
            'period': '30',
            'per_page': '100',
            'page': page_number,
            'text': language
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        response.raise_for_status()
        formated_response = response.json()
        for vacancy in formated_response['items']:
            if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
                sum_salary += predict_salary(
                    vacancy['salary']['from'],
                    vacancy['salary']['to']
                )
                vacancies_processed += 1
        if page_number >= formated_response['pages'] - 1:
            break
    language_vacancies = {
        'vacancies_found': formated_response['found'],
        'vacancies_processed': vacancies_processed,
        'average_salary': int(sum_salary / vacancies_processed)
    }
    return language_vacancies


def get_language_sj_vacancies(language, token, vacancy_count_per_page):
    headers = {'X-Api-App-Id': token}
    sum_salary = 0
    vacancies_processed = 0
    for page_number in count(0, 1):
        params = {
            'town': 'Moscow',
            'catalogues': '48',  # id of programmer specialization
            'keyword': language,
            'count': vacancy_count_per_page,
            'page': page_number
        }
        response = requests.get(
            'https://api.superjob.ru/2.0/vacancies/',
            headers=headers,
            params=params
        )
        response.raise_for_status()
        formated_response = response.json()
        for vacancy in formated_response['objects']:
            if vacancy['currency'] == 'rub':
                if vacancy['payment_from'] or vacancy['payment_to']:
                    sum_salary += predict_salary(
                        vacancy['payment_from'],
                        vacancy['payment_to']
                    )
                    vacancies_processed += 1
        vacancy_page_count = ceil(
            formated_response['total'] / vacancy_count_per_page
        )
        if page_number == vacancy_page_count - 1:
            break
    language_vacancies = {
        'vacancies_found': formated_response['total'],
        'vacancies_processed': vacancies_processed,
        'average_salary': int(sum_salary / vacancies_processed)
    }
    return language_vacancies


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_to:
        return salary_to * 0.8
    elif salary_from:
        return salary_from * 1.2

    
def make_table(languages_params, title):
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    ]
    for language, vacancy in languages_params.items():
        table_data.append([language, vacancy['vacancies_found'], vacancy['vacancies_processed'], vacancy['average_salary']])
    table = AsciiTable(table_data, title)
    return table.table


if __name__ == "__main__":
    load_dotenv()
    sj_key = os.getenv('SECRET_KEY_SJ')
    languages = ['Python', 'Java', 'Javascript', 'CSS', 'C++', 'Ruby', 'PHP', 'C#']
    languages_params_sj = {}
    languages_params_hh = {}
    vacancy_count_per_page = 50
    for language in languages:
        languages_params_hh[language] = get_language_hh_vacancies(language)
    for language in languages:
        languages_params_sj[language] = get_language_sj_vacancies(language, sj_key, vacancy_count_per_page)


print (make_table(TITLE_SJ, languages_params_sj))
print (make_table(TITLE_HH, languages_params_hh))
