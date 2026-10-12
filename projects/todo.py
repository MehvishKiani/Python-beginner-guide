"""Mini Projects — todo.py

Part of Python Beginner Guide: https://github.com/MehvishKiani/Python-beginner-guide
"""
import json
from pathlib import Path

FILE = Path("todo.json")


def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []


def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2))


def add_task(tasks, title):
    tasks.append({"id": len(tasks) + 1, "title": title, "done": False})
    save_tasks(tasks)


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
    save_tasks(tasks)


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    for t in tasks:
        print(f"[{'✔' if t['done'] else ' '}] {t['id']}. {t['title']}")
    done = sum(t["done"] for t in tasks)
    print(f"Progress: {done}/{len(tasks)} completed")


if __name__ == "__main__":
    tasks = load_tasks()
    add_task(tasks, "Revise Python loops")
    add_task(tasks, "Practice OOP exercises")
    add_task(tasks, "Build a mini project")
    complete_task(tasks, 1)
    show_tasks(tasks)
    print("Saved to", FILE, "→ reloaded tasks:", len(load_tasks()))
