import os
import json
import argparse
import dung_parser

# def compare_dungs_by_monster_level(d1, d2):

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("levels", help="Dungeons list", nargs="+")
    args = parser.parse_args()
    levels = args.levels

    if not os.path.exists('dungeons.json'):
        print('Parsing website...')
        dung_parser.parse()

    with open('dungeons.json', 'r') as file:
        data = json.load(file)

    current_monsters = []
    for i in range(len(levels)):
        if levels[i].isdigit():
            idx = int(levels[i])
            dung_name = data[i]['dungeon']
            monsters = data[i]['monsters']
            for monster in monsters:
                if monster['idx'] == idx:
                    monster['dungeon'] = dung_name
                    current_monsters.append(monster)
    if not current_monsters:
        print('Brak stworów :(')
        return

    current_monsters = sorted(current_monsters, key=lambda m: m['level'])

    max_dung_name = len(max(current_monsters, key=lambda m: len(m['dungeon']))['dungeon'])
    max_monster_name = len(max(current_monsters, key=lambda m: len(m['name']))['name'])

    formatter = '| {0:^10} | {1:^{2}} | {3:^{4}} | {5:^11} |'
    header = formatter.format('Poz. lochu', 'Loch', max_dung_name, 'Stwór', max_monster_name, 'Poz. stwora')
    print('-' * len(header))
    print(header)
    print('-' * len(header))
    for monster in current_monsters:
        print(formatter.format(monster['idx'], monster['dungeon'], max_dung_name, monster['name'], max_monster_name, monster['level']))
    print('-' * len(header))

if __name__ == '__main__':
    main()