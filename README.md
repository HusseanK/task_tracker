Small project based on : https://roadmap.sh/projects/task-tracker

Everything is run through the CLI using commands via argparse.

The tasks are displayed in a simplified format:

    ID: 3bcd
    ----------
    Task: Description of the task
    Status: incomplete/current/done
    Created on: 06:15PM on June 05, 2025
    Updated: 06:20PM on June 05, 2025

Command List:

    python main.py add "description"
        - The ADD keyword creates and stores a new "task" in a json file.
        - A positional argument for a description is needed and is simply a "Task Description"

    python main.py view (--done, --incomplete, --current)
        - the VIEW keyword is used to view all current tasks, with optional methods to view either Done, Incomplete, or Current tasks

    python main.py update "id" "description"
        - the UPDATE keyword updates a current task using its ID
        - A positional argument for a description is needed and is simply a "Task Description"
        (Note, each new task will be displayed on-creation with the ID visible)

    python main.py progress "id" (--incomplete, --current, --done)
        - the PROGRESS keyword updates a current tasks progress using its ID
        - A positional argument for status type is needed and is either --incomplete, --current, --done

    pythhon main.py delete "id"
        - the DELETE keyword simply removes a targeted ID from the task list

    python main.py clear
        - the CLEAR keyword clears the entire task list, starting back from scratch.
