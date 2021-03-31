import json

import requests
from bs4 import BeautifulSoup


def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(r.text)
    with open('index.html', encoding='utf-8') as f:
        src = f.read()

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('table', class_='table')
    tr = table.find_all('tr')

    td_list = []
    for td in tr:
        td_item = td.find('a', class_='mt_a')
        if td_item == None:
            td_count = None
        else:
            td_count = td_item.find_parent('td').find_next('td')

        if td_item != None and td_count != None:
            td_list.append({'country': td_item.text, 'count': td_count.text})
    print(td_list)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(td_list, f, indent=4, ensure_ascii=False)


def analize():
    with open('data.json', encoding='utf-8') as f:
        src = json.load(f)

    return src


def main():
    # parse('https://www.worldometers.info/coronavirus/')
    return analize()


# if __name__ == '__main__':
#     main()
