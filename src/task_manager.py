"""Core task management logic for the SPM Task Manager application."""

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable


@dataclass
class Task:
    title: str
    status: str = "To Do"
    due_date: date | None = None
    notes: str = ""
    tags: list[str] = field(default_factory=list)


class TaskBoard:
    allowed_statuses = ("To Do", "In Progress", "Done")

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str, *, due_date: date | None = None, notes: str = "") -> Task:
        task = Task(title=title, due_date=due_date, notes=notes)
        self._tasks.append(task)
        return task

    def move_task(self, title: str, status: str) -> Task:
        if status not in self.allowed_statuses:
            raise ValueError(f"Unsupported status: {status}")

        task = self.find_task(title)
        task.status = status
        return task

    def find_task(self, title: str) -> Task:
        for task in self._tasks:
            if task.title == title:
                return task
        raise LookupError(f"Task not found: {title}")

    def list_tasks(self, status: str | None = None) -> Iterable[Task]:
        if status is None:
            return tuple(self._tasks)
        return tuple(task for task in self._tasks if task.status == status)
