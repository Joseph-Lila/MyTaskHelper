""" Module layers.adapters.repository.special_task_repository """
from typing import List, Optional

from allocation.adapters.repository.abstract_repository import \
    AbstractRepository
from allocation.domain.models.special_task import SpecialTask


class SpecialTaskRepository(AbstractRepository):
    """ Repository for special tasks. """
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(item)

    def get_by_id(self, item_id):
        return self.session.query(SpecialTask).filter_by(id=item_id).one()

    def list(self):
        return self.session.query(SpecialTask).all()
