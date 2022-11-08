from utilities.status import Status


class BaseTask:

    def __init__(self, name, deadline, period, description=''):
        """
        Initialize base task object
        :param name: str: name of the task
        :param deadline: datetime.datetime: deadline of the task
        :param description: str: description of the task
        """
        self.name = name
        self.deadline = deadline
        self.description = description
        self.period = period
        self.__status = None

    @property
    def status(self):
        return self.__status

    def mark_as_done(self):
        self.__status = Status.DONE

    def delete_task(self):
        self.__status = Status.DELETED

    def freeze_task(self):
        self.__status = Status.FROZEN

    def undo_freeze_task(self):
        self.__status = Status.UNKNOWN
