import json
import os

JSON_FILE = "file_store.json"


def save_to_disk(data):
    """
    Save data to disk
    """
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
    except Exception as e:
        raise e


def open_json_file():
    """
    Open and return data in a json file.
        - If no data exists, return an empty dict and create a new json file.
    """

    if os.path.isfile(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            raise e

    data = {}
    save_to_disk(data)

    return data


def add_new_task(object):
    """
    Add new Task/obj to the Json file
    """

    # Splits the object into a dict
    object_dict = {
        "description": object.description,
        "created": str(object.created_on),
        "updated": object.updated_on,
        "status": object.status,
    }
    # Opens the file and then adds a new dict item
    data = open_json_file()
    data[object.id] = object_dict

    # Saves the file
    save_to_disk(data)
