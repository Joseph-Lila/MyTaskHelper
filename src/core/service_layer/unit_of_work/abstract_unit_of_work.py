""" Module core.service_layer.unit_of_work.abstract_unit_of_work """
import abc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from core import config
from core.adapters.repository.common_task_repository import \
    CommonTaskRepository
from core.adapters.repository.registrator_item_repository import \
    RegistratorItemRepository
from core.adapters.repository.registrator_repository import \
    RegistratorRepository
from core.adapters.repository.special_task_repository import \
    SpecialTaskRepository
from core.domain.models.base_task import BaseTask


class AbstractUnitOfWork(abc.ABC):
    """ Abstract unit of work class."""
    def __init__(self):
        self.session = None
        self.common_tasks: CommonTaskRepository = None
        self.special_tasks: SpecialTaskRepository = None
        self.registrators: RegistratorRepository = None
        self.registrator_items: RegistratorItemRepository = None

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_sqlite_uri(),
    )
)
