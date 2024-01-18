import sqlite3
import requests
from bs4 import BeautifulSoup as bs

def create_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS test1(
                      id INTEGER PRIMARY KEY,
                      name VARCHAR(50) NOT NULL,
                      url VARCHAR(100) NOT NULL);""")
    connection.commit()
    connection.close()

def insert_initial_data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO test1(name, url) VALUES
                      ('Курс валют', 'https://bank.gov.ua/ua/markets/exchangerates/'),
                      ('Прогноз погоди', 'https://meteofor.com.ua/ru/weather-kyiv-4944/'),
                      ('Цікаві факти про Леонардо Да Вінчі', 'https://faktypro.com.ua/page/20-czikavikh-faktiv-pro-leonardo-da-vinchi');""")
    connection.commit()
    connection.close()

def get_data_from_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("""SELECT name FROM test1""")
    data = cursor.fetchall()

    connection.close()
    return data

def display_currency_exchange():
    URL = 'https://bank.gov.ua/ua/markets/exchangerates/'
    r = requests.get(URL)
    html = bs(r.text, "html.parser")

    currency_values = html.find_all('td')
    for value in currency_values:
        print(value.text)
    print('Перше значення - Код цифровий, друге - Код літерний, третє - Кількість одиниць валюти, четверте - Назва валюти, пяте - Офіційний курс')

def display_weather_forecast():
    URL = 'https://meteopost.com/city/29313/ua/'
    r = requests.get(URL)
    html = bs(r.text, "html.parser")

    temperature_values1 = html.find_all('b')
    temperature_values = html.find_all('span', class_='t')
    for value in temperature_values:
        print(value.text)
    for value1 in temperature_values1:
        print(value1.text)


def display_interesting_facts():
    URL = 'https://tsikavi-fakty.com.ua/tsikavi-fakty-pro-leonardo-da-vinchi/'
    r = requests.get(URL)
    html = bs(r.text, "html.parser")

    facts = html.find_all('li')
    for fact in facts:
        print(fact.text)

if __name__ == "__main__":
    create_database()
    insert_initial_data()

    data = get_data_from_database()
    print(data)

    what = input('Що ви хочете подивитися з вище сказаних тем?')

    if what == 'Курс валют':
        display_currency_exchange()
    elif what == 'Прогноз погоди':
        display_weather_forecast()
    elif what == 'Цікаві факти про Леонардо Да Вінчі':
        display_interesting_facts()
    else:
        print('Напишіть назву коректно')
