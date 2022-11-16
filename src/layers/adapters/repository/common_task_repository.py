""" Module layers.adapters.repository.common_task_repository """
from typing import List, Optional

from allocation.adapters.repository.abstract_repository import \
    AbstractRepository
from allocation.domain.models.common_task import CommonTask


class CommonTaskRepository(AbstractRepository):
    """ Repository for common tasks. """
    def __init__(self, session):
        self.session = session

    def add(self, item: CommonTask) -> None:
        self.session.add(item)

    def get_by_id(self, item_id: int) -> Optional[CommonTask]:
        return self.session.query(CommonTask).filter_by(id=item_id).one()

    def list(self) -> List[CommonTask]:
        return self.session.query(CommonTask).all()
