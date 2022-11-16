""" Module core.adapters.repository.registrator_item_repository """
from typing import List, Optional

from core.adapters.repository.abstract_repository import AbstractRepository
from core.domain.models.registrator_item import RegistratorItem


class RegistratorItemRepository(AbstractRepository):
    """ Repository for registrator items. """
    def __init__(self, session):
        self.session = session

    def add(self, item: RegistratorItem) -> None:
        self.session.add(item)

    def get_by_id(self, item_id: int) -> Optional[RegistratorItem]:
        return self.session.query(RegistratorItem).filter_by(id=item_id).one()

    def list(self) -> List[RegistratorItem]:
        return self.session.query(RegistratorItem).all()
