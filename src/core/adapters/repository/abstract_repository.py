""" Module core.adapters.repository.abstract_repository """
import abc
from typing import List, Optional

from core.domain.models.base_task import BaseTask


class AbstractRepository(abc.ABC):
    """ Abstract repository implementation """
    @abc.abstractmethod
    def add(self, item: BaseTask):
        """
        Method to add an item to the repository
        :param item: BaseTask
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, item_id: int) -> Optional[BaseTask]:
        """
        Method to get an item using the given id
        :param item_id: int
        :return: BaseTask
        """
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[BaseTask]:
        """
        Method to get all items in the repository
        :return: List[BaseTask]
        """
        raise NotImplementedError
