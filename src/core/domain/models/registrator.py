""" Module core.domain.models.registrator """
from dataclasses import dataclass, field

from core.domain.models.registrator_item import RegistratorItem


@dataclass
class Registrator:
    """ Class core registrator """
    item_id: int = field(init=False)
    title: str
    description: str = ""
    items: list[RegistratorItem] = field(default_factory=list)
