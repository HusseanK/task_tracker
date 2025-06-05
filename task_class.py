import hashlib
from random import randrange

from task_manager import current_date_time
from json_handler import open_json_file


class Task:

    def __init__(self, description):
        self.description = description
        self.created_on = current_date_time()
        self.updated_on = None
        self.status = "incomplete"
        self.id = self.create_id()
        self.display_task()

    def create_id(self):
        # creates an ID using sha256 from hashlib, adds a little randomness to ensure different id
        sha = (self.description + (str(randrange(-100, 100)))).encode("ascii")
        id = hashlib.sha256(sha).hexdigest()[:4]
        data = open_json_file()

        # small recursion if the key is in-use. Very unlikely but safeguard
        if id in data.keys():
            return self.create_id()

        return id

    def display_task(self):
        # On creation display
        print(f"\nID: {self.id}")
        print("----------")
        print(f"Task: {self.description}")
        print(f"Status: {self.status}")
        print(f"Created on: {self.created_on}")
