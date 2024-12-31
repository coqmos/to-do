from typing import Final

FILE_PATH: Final[str] = 'to-do-list.txt'

def add_item(item)-> list:
    items = get_list()
    items.append(item)
    return items

def get_list()-> list:
    with open(FILE_PATH, 'r') as file:
        lines = file.readlines()

        lines = [line.strip() for line in lines]

    return lines

def delete_items(items: list)-> list:
    return [item for item in get_list() if item not in items]

def save(items: list):
    with open(FILE_PATH, 'w') as file:
        for item in items:
            file.write("%s\n" % item)
