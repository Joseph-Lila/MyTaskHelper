import datetime

from kivymd.uix.screen import MDScreen

from models.common_task_list_item import CommonTaskListItem


class CommonTasksListScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks = []
        for i in range(5):
            self.tasks.append(
                CommonTaskListItem(
                    name=str(i), deadline=datetime.datetime.fromisoformat("2022-11-20 10:00:00"),
                    period=None, separator_name=None, separator_quantity=None))

    def on_kv_post(self, base_widget):
        for item in self.tasks:
            self.common_tasks_list.add_widget(item)
