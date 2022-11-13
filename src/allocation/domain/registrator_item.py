from datetime import datetime
from dataclasses import dataclass, field


@dataclass(frozen=True)
class RegistratorItem:
    id: int = field(init=False)
    registrator_id: int = field(init=False)
    what: str
    how_much: float
    when: datetime
