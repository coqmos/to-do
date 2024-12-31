import argparse
import file_manager
import inquirer
from inquirer.themes import GreenPassion


def generate_questions()-> list:
    to_do_items = file_manager.get_list()
    questions = [
            inquirer.Checkbox(
                'to_do',
                message="To Do",
                choices=to_do_items,
                ),
            inquirer.List(
                "choice",
                message="What do you want to do?",
                choices=['Add', 'Edit', 'Mark Done',],
                ),]

    return questions


def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new', help = "Add a new item")
    args = parser.parse_args()
    if None != args.new:
        items = file_manager.add_item(args.new)
        file_manager.save(items)

if __name__ == "__main__":
    handle_arguments()

    answers = inquirer.prompt(generate_questions(), theme=GreenPassion())
    assert answers is not None
    
    if 'Mark Done' == answers['choice']:
        items = file_manager.delete_items(answers['to_do'])
        file_manager.save(items)
        print("Items Removed")
    if 'Add' == answers['choice']:
        question = [
            inquirer.Text(
                'add_item',
                message="What would you like to add?",
            )
        ]
        answer = inquirer.prompt(question)
        assert answer is not None

        items = file_manager.add_item(answer['add_item'])
        file_manager.save(items)
        print("Item Added")
    if 'Edit' == answers['choice']:
        selected_item = answers['to_do'][0]
        assert selected_item is not None

        question = [
            inquirer.Text(
                'edit_item',
                message="Edit item",
                default=selected_item
            )
        ]
        answer = inquirer.prompt(question)
        assert answer is not None

        items = file_manager.merge_item(answer['edit_item'], selected_item)
        file_manager.save(items)
        print("Updated")
