from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

@dataclass(eq=True, frozen=False)
class Task:
    id: Optional[int] = field(default=None, compare=True)
    name: str = field(default="")
    description: str = field(default="")
    status: TaskStatus = field(default=TaskStatus.TODO)

    def __post_init__(self):
        if self.status is None:
            self.status = TaskStatus.TODO
