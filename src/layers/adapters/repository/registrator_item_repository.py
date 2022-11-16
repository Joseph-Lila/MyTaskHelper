""" Module layers.adapters.repository.registrator_item_repository """
from allocation.adapters.repository.abstract_repository import \
    AbstractRepository
from allocation.domain.models.registrator_item import RegistratorItem


class RegistratorItemRepository(AbstractRepository):
    """ Repository for registrator items. """
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(item)

    def get_by_id(self, item_id):
        return self.session.query(RegistratorItem).filter_by(id=item_id).one()

    def list(self):
        return self.session.query(RegistratorItem).all()
