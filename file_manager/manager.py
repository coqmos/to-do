import json
from typing import Final

FILE_PATH: Final[str] = 'to-do-list.json'

def add_item(item):
    items = get_list()
    items.append({
            "item" : item,
            "status": 0
    })
    with open(FILE_PATH, 'w') as outfile:
        json.dump(items, outfile)


def get_list()-> list:
    with open(FILE_PATH, 'r') as json_item:
        return json.load(json_item)
