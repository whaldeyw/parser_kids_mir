import csv
from  bs4 import  BeautifulSoup
from  selenium import webdriver
from selenium_stealth import stealth
from time import sleep
import os
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()

options.add_argument("start-maximized")
options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
s = Service(os.path.abspath("chromedriver.exe"))
driver = webdriver.Chrome(options=options, service=s)



def main():
        with open('Детский мир.csv', 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                print('Загружаю данные')

                writer.writerow(
                        (
                                'Категория',
                                'Название товара',
                                'Цена',
                                'Ссылка на товар'
                        )
                )

        for ur in range(1):
                list = [4582, 4592, 45182, 4622, 4628, 4612, 2991, 45181,
                         49671, 44561, 44560, 44562, 50947, 51437, 33491, 11201, 44082, 44181, 1472, 45254, 50940, 51901, 2991, 45181, 49671, 44561, 44560,
                         44562, 50947, 51437, 33491, 11201, 44082, 44181, 1472, 45254, 50940, 51901, 44441,44448, 46410, 86, 88, 44112, 50943, 4,
                         83, 6231, 44182, 49670, 51550, 51938, 50941, 51550, 51398, 2, 44183, 39311, 44066, 51729, 44392, 44627, 44725, 45179, 50944,
                         51160, 51165, 51358, 1152, 5901, 5951, 6471, 46020, 46412, 51369]

                for i in list:
                        url = f"https://www.detmir.ru/search/results/categories-{i}/page/{ur}/?qt=категория&searchType=common&searchMode=refiner"

                        driver.get(url)
                        sleep(2)
                        PageSourse = driver.page_source
                        soup = BeautifulSoup(PageSourse, 'lxml')
                        all = soup.find_all(class_='Iy IC yF')
                        dict = []
                        for i in all:
                                categorian = soup.find(class_='E_4 Fg E_5 Fk Ff').text
                                name = i.find('h3').text
                                price = i.find(class_= 'bgt')
                                if price == None:
                                        price = 'Цена не указана'
                                else:
                                        price = i.find(class_= 'bgt').text

                                href = i.find('a').get('href')

                                print(f'{categorian}\n{name}\n{price}\n{href}')

                                with open('Детский мир.csv', 'a', encoding='utf-8') as file:
                                        writer = csv.writer(file)

                                        writer.writerow(
                                                (
                                                        categorian,
                                                        name,
                                                        price,
                                                        href,
                                                )
                                        )

        for ur in range(3):
                list = [51379, 45180, 44099, 50492, 44050, 45263]

                for i in list:
                        url = f"https://www.detmir.ru/search/results/categories-{i}/page/{ur}/?qt=категория&searchType=common&searchMode=refiner"

                        driver.get(url)
                        sleep(2)
                        PageSourse = driver.page_source
                        soup = BeautifulSoup(PageSourse, 'lxml')
                        all = soup.find_all(class_='Iy IC yF')
                        dict = []
                        for i in all:
                                categorian = soup.find(class_='E_4 Fg E_5 Fk Ff').text
                                name = i.find('h3').text
                                price = i.find(class_= 'bgt')
                                if price == None:
                                        price = 'Цена не указана'
                                else:
                                        price = i.find(class_= 'bgt').text

                                href = i.find('a').get('href')

                                print(f'{categorian}\n{name}\n{price}\n{href}')

                                with open('Детский мир.csv', 'a', encoding='utf-8') as file:
                                        writer = csv.writer(file)

                                        writer.writerow(
                                                (
                                                        categorian,
                                                        name,
                                                        price,
                                                        href,
                                                )
                                        )

        for ur in range(5):
                list1 = [9751, 69, 21581]

                for i in list1:
                        url = f"https://www.detmir.ru/search/results/categories-{i}/page/{ur}/?qt=категория&searchType=common&searchMode=refiner"

                        driver.get(url)
                        sleep(2)
                        PageSourse = driver.page_source
                        soup = BeautifulSoup(PageSourse, 'lxml')
                        all = soup.find_all(class_='Iy IC yF')
                        dict = []
                        for i in all:
                                categorian = soup.find(class_='E_4 Fg E_5 Fk Ff').text
                                name = i.find('h3').text
                                price = i.find(class_= 'bgt')
                                if price == None:
                                        price = 'Цена не указана'
                                else:
                                        price = i.find(class_= 'bgt').text

                                href = i.find('a').get('href')

                                print(f'{categorian}\n{name}\n{price}\n{href}')

                                with open('Детский мир.csv', 'a', encoding='utf-8') as file:
                                        writer = csv.writer(file)

                                        writer.writerow(
                                                (
                                                        categorian,
                                                        name,
                                                        price,
                                                        href,
                                                )
                                        )

        for ur in range(8):
                list = [53]

                for i in list:
                        url = f"https://www.detmir.ru/search/results/categories-{i}/page/{ur}/?qt=категория&searchType=common&searchMode=refiner"

                        driver.get(url)
                        sleep(2)
                        PageSourse = driver.page_source
                        soup = BeautifulSoup(PageSourse, 'lxml')
                        all = soup.find_all(class_='Iy IC yF')
                        dict = []
                        for i in all:
                                categorian = soup.find(class_='E_4 Fg E_5 Fk Ff').text
                                name = i.find('h3').text
                                price = i.find(class_= 'bgt')
                                if price == None:
                                        price = 'Цена не указана'
                                else:
                                        price = i.find(class_= 'bgt').text

                                href = i.find('a').get('href')

                                print(f'{categorian}\n{name}\n{price}\n{href}')

                                with open('Детский мир.csv', 'a', encoding='utf-8') as file:
                                        writer = csv.writer(file)

                                        writer.writerow(
                                                (
                                                        categorian,
                                                        name,
                                                        price,
                                                        href,
                                                )
                                        )

if __name__== '__main__':
        main()