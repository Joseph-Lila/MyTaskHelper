from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget

from utilities.common_task import CommonTask


class CommonTaskListItem(CommonTask, ThreeLineAvatarListItem):
    def __init__(self, name, deadline, period, separator_name, separator_quantity, **kwargs):
        super().__init__(name, deadline, period, separator_name, separator_quantity, **kwargs)
        image_left_widget = ImageLeftWidget(source="assets/images/eight.jpg")
        self.add_widget(image_left_widget)

    @property
    def name(self):
        return self.text

    @name.setter
    def name(self, value):
        self.text = value
        self.name = value

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value):
        self.status = value
        self.secondary_text = value

    @property
    def deadline(self):
        return self.deadline

    @deadline.setter
    def deadline(self, value):
        self.deadline = value
        self.tertiary_text = value

