import json
import os
import re
import requests
from datetime import date
from bs4 import BeautifulSoup as bs

BASE_URL_CURRENCIES = 'https://coinmarketcap.com/currencies/'


def to_snake_case(name):
    """
    Método para convertir los nombres de los campos del html a snake case.
    """
    name = name.replace('/', '_')
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


def get_currency_info(currency):
    """
    Método que scrappea la página /currencies/<currency> y devuelve un json con la información
    sumado a un campo updated_at con la fecha de actualización.
    Se usa los mismos nombres que aparecen en el HTML solo que cambiados a snake case.
    """
    url = f'{BASE_URL_CURRENCIES}/{currency}'
    res = requests.get(url)
    if res.status_code != 200:
        return {}
    raw = bs(res.text, 'html.parser')
    table = raw.findAll('table')
    table_1 = table[0]
    table_2 = table[len(table) - 1]

    results = {}
    for key, value in table_1('tr'):
        results.update({
            to_snake_case((key.text).replace(' ', '')): value.text
        })

    for key, value in table_2('tr'):
        results.update({
            to_snake_case((key.text).replace(' ', '')): value.text
        })
    results.update({
        'updated_at': str(date.today())
    })
    save_data(currency, results)
    return results


def save_data(currency, data):
    """
    Método para guardar la data scrappeada en un archivo tipo json (currencies.json)
    """
    if not os.path.exists('currencies.json'):
        file = open('currencies.json', 'x')
        file.close()
    file = open('currencies.json', 'r')
    file_size = os.stat('currencies.json').st_size
    if file_size == 0:
        json_object = {}
    else:
        json_object = json.load(file)
    file.close()

    json_object[currency] = {
        'data': data
    }

    file = open('currencies.json', 'w')
    json.dump(json_object, file, ensure_ascii=False, indent=4)
    file.close()


def get_all_currencies():
    file = open('currencies.json', 'r')
    json_data = json.load(file)
    return json_data
