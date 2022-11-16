""" Module core.domain.models.status """
from typing import Optional


class Status:
    """ Status class """
    DONE = 'done'
    HORROR = 'horror'
    CRITICAL = 'critical'
    HARD = 'hard'
    MIDDLE = 'middle'
    LIGHT = 'light'
    DELETED = 'deleted'
    FROZEN = 'frozen'
    UNKNOWN = 'unknown'

    STATUSES_WITH_MARKS = [
        CRITICAL,
        HARD,
        MIDDLE,
        LIGHT,
    ]

    BEFORE_START_WORKING_ON_TASK = {
        DONE: None,
        HORROR: None,
        CRITICAL: 0,
        HARD: 20,
        MIDDLE: 50,
        LIGHT: 100,
        DELETED: None,
        FROZEN: None,
        UNKNOWN: None,
    }

    @staticmethod
    def check_status_assumes_time_to_work(status):
        """ Checks if the status assumes time to work on it. """
        return status in Status.STATUSES_WITH_MARKS

    @classmethod
    def get_hours_before_start_working_on_task(cls, status: str) -> int:
        """ Method to get hours before start working on task. """
        if not Status.check_status_assumes_time_to_work(status):
            raise KeyError('Wrong status value!')
        eta: Optional[int] = cls.BEFORE_START_WORKING_ON_TASK[status]
        if eta is None:
            raise ValueError(f"The status `{status}` cannot be estimated!")
        return eta
