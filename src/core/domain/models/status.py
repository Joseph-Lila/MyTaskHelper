from typing import Optional


class Status:
    DONE = 'done'
    HORROR = 'horror'
    CRITICAL = 'critical'
    HARD = 'hard'
    MIDDLE = 'middle'
    LIGHT = 'light'
    DELETED = 'deleted'
    FROZEN = 'frozen'
    UNKNOWN = 'unknown'

    STATUSES_WITH_ESTIMATION = [
        CRITICAL,
        HARD,
        MIDDLE,
        LIGHT,
    ]

    STATUS_ESTIMATE = {
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

    @classmethod
    def get_status_estimation(cls, status: str) -> int:
        if status not in cls.STATUS_ESTIMATE:
            raise KeyError('Wrong status value!')
        eta: Optional[int] = cls.STATUS_ESTIMATE[status]
        if eta is None:
            raise ValueError(f"The status `{status}` cannot be estimated!")
        return eta
