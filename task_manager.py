from json_handler import open_json_file, save_to_disk
import datetime


def current_date_time() -> str:
    """
    Returns date and time, formatted.
    """
    # Used more than once, just returning time/date in a pretty format.
    return str(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))


def display(id: str, values: str) -> None:
    """
    Display the current task using provided data
    """
    print(f"\nID: {id}")
    print("----------")
    print(f"Task: {values["description"]}")
    print(f"Status: {values["status"]}")
    print(f"Created on: {values["created"]}")
    if values["updated"]:
        print(f"Updated: {values["updated"]}")


def list_specific_tasks(task_type: str) -> None:
    """
    Lists all tasks of a specific type
    """
    data = open_json_file()
    for key, val in data.items():
        if val["status"] == task_type:
            display(key, val)


def list_all_tasks() -> None:
    """
    Lists all tasks
    """
    data = open_json_file()
    for key, val in data.items():
        display(key, val)


def delete_task(id: str) -> None:
    """
    Removes a Task and re-saves file
    """
    data = open_json_file()
    for key in data.keys():
        if key == id:
            del data[key]
            save_to_disk(data)
            break
    else:
        print(f"no key found: {id}")


def update_task(id: str, descripton: str) -> None:
    """
    Updates a current task
    """
    data = open_json_file()
    if id in data.keys():
        dict_id = data[id]
        dict_id["description"] = descripton
        dict_id["updated"] = current_date_time()
        save_to_disk(data)
    else:
        # With a small error raised
        raise KeyError(f"No Task with the key {id} could be found")


def update_progress(id: str, new_cond: str) -> None:
    """
    Updates the progress of a Task
    """
    data = open_json_file()

    if id in data.keys():
        dict_id = data[id]
        # Update the progress
        dict_id["status"] = new_cond
        # Then update the time it was last-updated
        dict_id["updated"] = current_date_time()
        save_to_disk(data)
    else:
        # With a small error raised
        raise KeyError(f"No Task with the key {id} could be found")
