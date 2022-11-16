""" Module core.adapters.repository.registrator_repository """
from typing import List, Optional

from core.adapters.repository.abstract_repository import AbstractRepository
from core.domain.models.registrator import Registrator


class RegistratorRepository(AbstractRepository):
    """ Repository for registrators. """
    def __init__(self, session):
        self.session = session

    def add(self, item: Registrator) -> None:
        self.session.add(item)

    def get_by_id(self, item_id: int) -> Optional[Registrator]:
        return self.session.query(Registrator).filter_by(id=item_id).one()

    def list(self) -> List[Registrator]:
        return self.session.query(Registrator).all()
