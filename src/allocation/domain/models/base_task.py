from dataclasses import dataclass, field
from datetime import datetime
from allocation.domain.status import Status


@dataclass
class BaseTask:
    id: int = field(init=False)
    title: str
    deadline: datetime
    period: int
    description: str = ""
    status: str = Status.UNKNOWN
