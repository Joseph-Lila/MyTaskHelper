""" Module layers.adapters.repository.registrator_repository """
from dataclasses import dataclass
from typing import Optional, List
from allocation.domain.models.base_task import BaseTask
from allocation.domain.models.status import Status


class CommonTask(BaseTask):
    def __init__(self, eta: int, partition_title: Optional[str], partition_count: Optional[int],
                 partition_progress: Optional[int]):
        self.eta: int = eta
        self.partition_title: Optional[str] = partition_title
        self.partition_count: Optional[int] = partition_count
        self.partition_progress: Optional[int] = partition_progress

    @staticmethod
    def get_by_id(common_tasks: List[CommonTask], task_id: int):
        results = [task for task in common_tasks if task.id == task_id]
        return results[0] if len(results) > 0 else None

    @staticmethod
    def distribute_statuses(common_tasks: List[CommonTask]) -> None:
        remainders = {}
        for task in common_tasks:
            remainders[task.id] = get_remainder_hours(task)
            remainders.sort(key=lambda x: x.value)
        amount = 0
        for key, value in remainders.items():
            for status in sorted(Status.STATUSES_WITH_ESTIMATION):
                estimation = Status.get_status_estimation(status)
                if value - amount <= estimation:
                    task: CommonTask = CommonTask.get_by_id(common_tasks, key)
                    if task:
                        task.status = status
                    amount += value
