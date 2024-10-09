import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

class TodoItem:
    """Represents a single to-do item."""
    def __init__(self, task: str):
        self.task = task
        self.completed = False

    def mark_completed(self):
        self.completed = True
        logger.info(f"Task '{self.task}' marked as completed.")

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{self.task} [{status}]"


class TodoListManager:
    """A simple to-do list manager class to manage tasks."""
    def __init__(self):
        self.tasks: List[TodoItem] = []

    def add_task(self, task: str) -> None:
        """Adds a new task to the list."""
        new_task = TodoItem(task)
        self.tasks.append(new_task)
        logger.info(f"Added task: '{task}'")

    def remove_task(self, task: str) -> bool:
        """Removes a task by its name. Returns True if removed, False if not found."""
        for item in self.tasks:
            if item.task == task:
                self.tasks.remove(item)
                logger.info(f"Removed task: '{task}'")
                return True
        logger.warning(f"Task '{task}' not found.")
        return False

    def list_tasks(self) -> List[str]:
        """Returns a list of all tasks with their status."""
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, task: str) -> bool:
        """Marks a task as completed by its name. Returns True if marked, False if not found."""
        for item in self.tasks:
            if item.task == task:
                item.mark_completed()
                return True
        logger.warning(f"Task '{task}' not found.")
        return False


if _name_ == "_main_":
    manager = TodoListManager()
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    manager.mark_task_completed("Buy groceries")
    print("\n".join(manager.list_tasks()))
    manager.remove_task("Read a book")
    print("\n".join(manager.list_tasks()))