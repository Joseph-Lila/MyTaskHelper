from datetime import datetime, timedelta

import pytest

from core.domain.models.common_task import CommonTask
from core.domain.models.status import Status


def test_get_by_id():
    task1 = CommonTask(
        item_id=1, title="Task 1", deadline=datetime(2022, 1, 1, 0, 0, 0), period=None,
        description="Task 1 description", status=Status.UNKNOWN, eta=4,
        partition_title="Глава", partition_count=15, partition_progress=3)
    task2 = CommonTask(
        item_id=2, title="Task 2", deadline=datetime(2022, 1, 1, 0, 0, 0), period=None,
        description="Task 2 description", status=Status.UNKNOWN, eta=4,
        partition_title="Глава", partition_count=15, partition_progress=3)
    tasks = [task1, task2]
    print(tasks)
    assert CommonTask.get_by_id(tasks, 1) == task1
