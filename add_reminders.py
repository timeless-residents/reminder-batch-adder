"""
This module provides functions to interact with the Apple Reminders app using AppleScript.

Functions:
    add_to_reminders: Adds a list of tasks to a specific reminder list in the Reminders app.
"""
from applescript import tell

def add_to_reminders(reminder_list_name, reminder_list):
    """
    Adds a list of reminders to the specified reminder list in the Apple Reminders app.

    Args:
        reminder_list_name (Any): The name of the reminder list to add tasks to.
        reminder_list (Any): A list of reminder tasks to be added.

    Returns:
        None
    """
    for reminder in reminder_list:
        script = f'''
        tell application "Reminders"
            set myList to list "{reminder_list_name}"
            make new reminder at end of myList with properties {{name:"{reminder}"}}
        end tell
        '''
        tell.app("Reminders", script)

if __name__ == "__main__":
    LIST_NAME = "Day One"  # リスト名
    with open("reminders.txt", "r", encoding="utf-8") as file:
        reminders = [line.strip() for line in file]
    add_to_reminders(LIST_NAME, reminders)
