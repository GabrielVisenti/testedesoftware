from __future__ import annotations
from typing import Dict, Tuple
from itertools import count

from .models import Task, TaskStatus

class TaskService:
    def __init__(self) -> None:
        self._store: Dict[int, Task] = {}
        self._seq = count(start=1)

    def add_task(self, name: str, description: str | None = None) -> Task:
        if name is None or not name.strip():
            raise ValueError("Nome da tarefa não pode ser vazio.")
        tid = next(self._seq)
        t = Task(id=tid, name=name.strip(), description=(description or "").strip(), status=TaskStatus.TODO)
        self._store[tid] = t
        return t

    def mark_as_done(self, task_id: int) -> Task:
        t = self._get_required(task_id)
        t.status = TaskStatus.DONE
        return t

    def mark_in_progress(self, task_id: int) -> Task:
        t = self._get_required(task_id)
        t.status = TaskStatus.IN_PROGRESS
        return t

    def edit_task(self, task_id: int, new_name: str, new_description: str | None = None) -> Task:
        t = self._get_required(task_id)
        if new_name is None or not new_name.strip():
            raise ValueError("Nome da tarefa não pode ser vazio.")
        t.name = new_name.strip()
        t.description = (new_description or "").strip()
        return t

    def delete_task(self, task_id: int) -> None:
        self._get_required(task_id)  # valida existência
        del self._store[task_id]

    def list_tasks(self) -> Tuple[Task, ...]:
        # Retorna tupla para evitar mutações externas
        return tuple(self._store.values())

    # ---- helpers ----
    def _get_required(self, task_id: int) -> Task:
        t = self._store.get(task_id)
        if t is None:
            raise ValueError(f"Tarefa não encontrada: id={task_id}")
        return t
