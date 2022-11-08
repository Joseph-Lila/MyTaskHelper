class TasksStore:
    ACCEPTED_STATUSES = ['horror', 'critical', 'hard', 'middle', 'light', 'freeze']

    def __init__(self, tasks):
        self.tasks = tasks

    def set_statuses(self):
        pass
