import sys
import argparse

from task_class import Task
from json_handler import add_new_task, save_to_disk
from task_manager import (
    list_all_tasks,
    list_specific_tasks,
    delete_task,
    update_task,
    update_progress,
)


def add():
    """
    Adds the current Task
    """
    # Uses sys.argv to grab the last input in the console and set it to description
    description = sys.argv[-1]
    # add, save to disk, all done
    new_task = Task(description)
    add_new_task(new_task)


def update():
    """
    Updates the current task based on ID, with the new description
    """
    # Uses sys.argv to grab the last input in the console and set it to description
    description = sys.argv[-1]
    # Id is the 2nd last keyword
    id = sys.argv[-2]
    update_task(id, description)


def delete():
    # ID num
    last_arg = sys.argv[-1]
    delete_task(last_arg)


def view_conditions():
    last_arg = sys.argv[-1].strip("--")

    if last_arg == "view":
        list_all_tasks()
    else:
        list_specific_tasks(last_arg)


def progress():
    description = sys.argv[-1].strip("--")
    id = sys.argv[-2]
    update_progress(id, description)


def clear():
    # Saving an empty dict, to reset the Json file
    save_to_disk({})


def main(args):
    match (args.command):
        case "view":
            view_conditions()
        case "add":
            add()
        case "update":
            update()
        case "progress":
            progress()
        case "delete":
            delete()
        case "clear":
            clear()


def args_parser():
    """
    Args parser to create the following keywords:
        - add ("description")
        - view (--done, --incomplete, --current)
        - update ("ID") (--done, --incomplete, --current)
        - progress (--done, --incomplete, --current)
        - delete ("ID")
        - clear
    """

    # Create parser
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    # Add
    add_task = sub.add_parser("add", help="Add new task")
    add_task.add_argument("description", type=str, help="Task description string")

    # Update
    update = sub.add_parser("update", help="Update a task")
    update.add_argument("id", type=str, help="Change task using id")
    update.add_argument("description", type=str, help="New Task description string")

    # Delete
    delete = sub.add_parser("delete", help="Update a task")
    delete.add_argument("id", type=str, help="Delete provided task using id")

    # Delete
    clear = sub.add_parser("clear", help="Update a task")

    # Progress
    progress = sub.add_parser("progress", help="Change the progress of a task")
    progress.add_argument("id", type=str, help="Change progress using id")
    mutual_progress = progress.add_mutually_exclusive_group(required=True)
    mutual_progress.add_argument("--done", action="store_true")
    mutual_progress.add_argument("--incomplete", action="store_true")
    mutual_progress.add_argument("--current", action="store_true")

    # View
    view_task = sub.add_parser("view", help="view current tasks")
    mutual = view_task.add_mutually_exclusive_group(required=False)
    mutual.add_argument("--done", action="store_true")
    mutual.add_argument("--incomplete", action="store_true")
    mutual.add_argument("--current", action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    args = args_parser()

    main(args)
