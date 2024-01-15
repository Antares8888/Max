import requests
from bs4 import BeautifulSoup as bs

URL = 'https://privatbank.ua/rates-archive'
r = requests.get(URL)

html = bs(r.text, "html.parser")

num1 = html.find_all('div', class_='sale')
num2 = html.find_all('div', class_='purchase')

for i in num1:
    print(i.text)

print('Три верхніх числа над цим текстом це курс продажу, перше - Євро, друге - Долар США, третє - Польський злотий')

for i in num2:
    print(i.text)

print('Три верхніх числа над цим текстом це курс купівлі, перше - Євро, друге - Долар США, третє - Польський злотий')

def calc():
    try:
        num3 = float(input('Виберіть у яку валюту будете переводити, у курс продаж чи купівлі, напишіть одне з чисел про які я вам казав'))
        num4 = float(input('Вкажіть скільки гривнь ви переводите'))

        if num3 == 42.8 or num3 == 38.8 or num3 == 9.9 or num3 == 41.8 or num3 == 38.2 or num3 == 9.5:
            print(num4 / num3)
        else:
            print("Невірне значення для курсу. Спробуйте ще раз.")
    except ValueError:
        print("Невірний формат числа. Спробуйте ще раз.")

calc()
