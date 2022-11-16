from dataclasses import dataclass, field

from allocation.domain.models.registrator_item import RegistratorItem


@dataclass
class Registrator:
    id: int = field(init=False)
    title: str
    description: str = ""
    items: list[RegistratorItem] = field(default_factory=list)
