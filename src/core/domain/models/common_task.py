""" Module core.adapters.repository.registrator_repository """
from dataclasses import field
from datetime import datetime
from typing import Optional

from core.domain.models.base_task import BaseTask
from core.domain.models.status import Status


class CommonTask(BaseTask):
    """ Common task class """
    WORKING_HOURS_PER_DAY = 16
    LAST_WORKING_HOUR = 21

    def __init__(self, eta: int, partition_title: Optional[str], partition_count: Optional[int],
                 partition_progress: Optional[int]):
        super().__init__()
        self.eta: int = eta
        self.partition_title: Optional[str] = partition_title
        self.partition_count: Optional[int] = partition_count
        self.partition_progress: Optional[int] = partition_progress

    @staticmethod
    def get_by_id(common_tasks, task_id: int):
        """ Get a common task by id """
        results = [task for task in common_tasks if task.item_id == task_id]
        return results[0] if len(results) > 0 else None

    @staticmethod
    def get_remainder_hours(common_task) -> int:
        """ Returns hours before the deadline """
        return (common_task.deadline - datetime.now()).day * CommonTask.WORKING_HOURS_PER_DAY + \
               CommonTask.LAST_WORKING_HOUR - datetime.now().hour - common_task.eta

    @staticmethod
    def distribute_statuses(common_tasks) -> None:
        """ Method to distribute statuses """
        remainders = {}
        for task in common_tasks:
            remainders[task.id] = CommonTask.get_remainder_hours(task)
        remainders = dict(sorted(remainders.items(), key=lambda x: x.value))
        amount = 0
        for key, value in remainders.items():
            for status in sorted(Status.STATUSES_WITH_MARKS):
                estimation = Status.get_hours_before_start_working_on_task(status)
                if value - amount <= estimation:
                    task = CommonTask.get_by_id(common_tasks, key)
                    if task:
                        task.status = status
                    amount += value
