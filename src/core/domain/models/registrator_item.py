""" Module core.domain.models.registrator_item """
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class RegistratorItem:
    """ Dataclass representing registrator item """
    item_id: int = field(init=False)
    registrator_id: int = field(init=False)
    what: str
    how_much: float
    when: datetime
