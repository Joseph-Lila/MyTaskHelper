""" Module core.domain.models.base_task """
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class BaseTask:
    """ Dataclass representing a base task"""
    item_id: int = field(init=False)
    title: str
    deadline: datetime
    period: Optional[int]
    description: str
    status: str
