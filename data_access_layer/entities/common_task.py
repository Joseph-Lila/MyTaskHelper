from utilities.base_task import BaseTask


class CommonTask(BaseTask):
    def __init__(self, name, deadline, period, separator_name, separator_quantity, **kwargs):
        super().__init__(name, deadline, period)
        self.separator_name = separator_name
        self.separator_quantity = separator_quantity
        self.__separator_progress = 0

    @property
    def separator_progress(self):
        return self.__separator_progress

    def increment_separator_progress(self):
        self.__separator_progress += 1

    def decrement_separator_progress(self):
        self.__separator_progress -= 1
    