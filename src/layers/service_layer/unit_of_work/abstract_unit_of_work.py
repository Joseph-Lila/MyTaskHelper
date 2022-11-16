import abc
from src.layers.domain.models.base_task import BaseTask
from src.layers.adapters.repository.common_task_repository import CommonTaskRepository
from src.layers.adapters.repository.special_task_repository import SpecialTaskRepository
from src.layers.adapters.repository.registrator_repository import RegistratorRepository
from src.layers.adapters.repository.registrator_item_repository import RegistratorItemRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from src.layers import config


class AbstractUnitOfWork(abc.ABC):
    common_tasks: CommonTaskRepository
    special_tasks: SpecialTaskRepository
    registrators: RegistratorRepository
    registrator_items: RegistratorItemRepository

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
