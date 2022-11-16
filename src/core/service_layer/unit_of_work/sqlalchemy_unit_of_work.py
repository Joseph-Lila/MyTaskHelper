"""Module core.service_layer.unit_of_work.sqlalchemy_unit_of_work """
from core.adapters.repository.common_task_repository import \
    CommonTaskRepository
from core.adapters.repository.registrator_item_repository import \
    RegistratorItemRepository
from core.adapters.repository.registrator_repository import \
    RegistratorRepository
from core.adapters.repository.special_task_repository import \
    SpecialTaskRepository
from core.service_layer.unit_of_work.abstract_unit_of_work import (
    DEFAULT_SESSION_FACTORY, AbstractUnitOfWork)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    """ SqlAlchemyUnitOfWork implementation for unit of work pattern """
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.common_tasks = CommonTaskRepository(self.session)
        self.special_tasks = SpecialTaskRepository(self.session)
        self.registrators = RegistratorRepository(self.session)
        self.registrator_items = RegistratorItemRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(self, *args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
