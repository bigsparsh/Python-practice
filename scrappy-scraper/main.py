import time
import requests
import selectorlib
import datetime
import pandas as pd

URL = 'https://programmer100.pythonanywhere.com/'


def scrape_n_extract():
    html_content = requests.get(URL).text
    extracted_content = selectorlib.Extractor.from_yaml_file('extract_info.yaml').extract(html_content)['home']
    return extracted_content


def update_log():
    timestamp = datetime.datetime.now()
    with open('temperature_log.txt', 'a') as log:
        log.write(f'{timestamp},{scrape_n_extract()}\n')


def read_log():
    return pd.read_csv('temperature_log.txt')


if __name__ == '__main__':
    while True:
        update_log()
        time.sleep(3)
