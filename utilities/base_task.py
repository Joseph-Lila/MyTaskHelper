class BaseTask:

    def __init__(self, name, deadline, description=''):
        """
        Initialize base task object
        :param name: str: name of the task
        :param deadline: datetime.datetime: deadline of the task
        :param description: str: description of the task
        """
        self.name = name
        self.deadline = deadline
        self.description = description
        self.status = None
