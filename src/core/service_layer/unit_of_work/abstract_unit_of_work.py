""" Module core.service_layer.unit_of_work.abstract_unit_of_work """
import abc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import config


class AbstractUnitOfWork(abc.ABC):
    """ Abstract unit of work class."""
    def __init__(self):
        self.session = None
        self.common_tasks = None
        self.special_tasks = None
        self.registrators = None
        self.registrator_items = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        """ Method to commit the current session"""
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        """ Method to roll back the current session"""
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_sqlite_uri(),
    )
)
