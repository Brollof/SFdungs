import re
import json
import urllib.request
from bs4 import BeautifulSoup

DEBUG = False

def parse():
    if DEBUG:
        with open('dungeons.html', 'r', encoding="utf-8") as file:
            html = file.read()
    else:
        with urllib.request.urlopen("https://pl.4m7.de/sammelalbum/dungeons.php") as www:
            html = www.read().decode('utf-8')

    dungeons = re.findall(r'<b>\d+ - (.*?)</b>', html)
    data = [{'dungeon': dung_name, 'monsters': []} for dung_name in dungeons]

    current_dung = 0
    prev_idx = -1

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        idx = int(cols[1].get_text())
        name = cols[2].a.get_text().strip() or 'Sobowtór'
        level = int(cols[3].get_text() or 0)

        if prev_idx > idx:
            current_dung += 1

        monster = {'name': name, 'idx': idx, 'level': level}
        data[current_dung]['monsters'].append(monster)
        prev_idx = idx

    with open('dungeons.json', 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == '__main__':
    parse()