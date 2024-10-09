import pytest
from ToDo.main import TodoListManager

def test_add_task():
    manager = TodoListManager()
    manager.add_task("Go for a walk")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].task == "Go for a walk"
    assert not manager.tasks[0].completed

def test_remove_task():
    manager = TodoListManager()
    manager.add_task("Go for a walk")
    assert manager.remove_task("Go for a walk") == True
    assert len(manager.tasks) == 0
    assert manager.remove_task("Go for a walk") == False

def test_mark_task_completed():
    manager = TodoListManager()
    manager.add_task("Go for a walk")
    assert manager.mark_task_completed("Go for a walk") == True
    assert manager.tasks[0].completed
    assert manager.mark_task_completed("Nonexistent task") == False

def test_list_tasks():
    manager = TodoListManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.mark_task_completed("Task 1")
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0] == "Task 1 [✔]"
    assert tasks[1] == "Task 2 [✘]"