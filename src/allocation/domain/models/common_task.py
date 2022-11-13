from dataclasses import dataclass
from typing import Optional
from allocation.domain.models.base_task import BaseTask


@dataclass
class CommonTask(BaseTask):
    partition_title: Optional[str] = None
    partition_count: Optional[int] = None
    partition_progress: Optional[int] = None
