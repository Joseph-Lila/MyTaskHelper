from utilities.status import Status


class BaseTask:

    def __init__(self, name, deadline, period, description=''):
        """
        Initialize base task object
        :param name: str: name of the task
        :param deadline: datetime.datetime: deadline of the task
        :param description: str: description of the task
        """
        self._name = name
        self._deadline = deadline
        self._description = description
        self._period = period
        self.my_status = None

    def mark_as_done(self):
        self.my_status = Status.DONE

    def delete_task(self):
        self.my_status = Status.DELETED

    def freeze_task(self):
        self.my_status = Status.FROZEN

    def undo_freeze_task(self):
        self.__status = Status.UNKNOWN
