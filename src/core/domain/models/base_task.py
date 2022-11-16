""" Module core.domain.models.base_task """
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class BaseTask:
    """ Dataclass representing a base task"""
    item_id: int = field(init=False)
    title: str
    deadline: datetime
    period: int
    description: str
    status: str
