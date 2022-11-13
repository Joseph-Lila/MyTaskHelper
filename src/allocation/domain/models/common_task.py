from dataclasses import dataclass
from typing import Optional, List
from allocation.domain.models.base_task import BaseTask


@dataclass
class CommonTask(BaseTask):
    eta: int
    partition_title: Optional[str] = None
    partition_count: Optional[int] = None
    partition_progress: Optional[int] = None


def distribute_statuses(common_tasks: List[CommonTask]):
    pass
