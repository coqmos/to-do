import argparse
import file_manager
import inquirer

def generate_questions()-> list:
    to_do_items = format_list(file_manager.get_list())
    questions = [
            inquirer.Checkbox(
                'to_do',
                message="To Do",
                choices=to_do_items,
                ),
            inquirer.List(
                "choice",
                message="What do you want to do?",
                choices=['Add', 'Delete', 'Edit', 'Mark Done',],
                ),]

    return questions


def format_list(items:list) -> list:
    formatted_items = []
    for i in items:
        text = i['item']
        if i['status'] == 1:
            text =' ' + text
        formatted_items.append(text)
    return formatted_items


def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new', help = "Add a new item")
    args = parser.parse_args()
    if None != args.new:
        file_manager.add_item(args.new)

def handle_delete(items: list):
    print('Lets delete')

if __name__ == "__main__":
    handle_arguments()
    answers = inquirer.prompt(generate_questions())
    assert answers is not None
    if 'Delete' == answers['choice']:
        print(answers['choice'])

