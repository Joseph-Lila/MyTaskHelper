from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget

from utilities.common_task import CommonTask


class CommonTaskListItem(ThreeLineAvatarListItem):
    def __init__(self, name, deadline, period, separator_name, separator_quantity, **kwargs):
        super().__init__(**kwargs)
        self.text_color = [1, 0, 0, 1]
        self.theme_text_color = 'Custom'
        self.name = name
        self.status = "UNKNOWN"
        self.deadline = str(deadline)
        self.period = period
        self.separator_name = separator_name
        self.separator_quantity = separator_quantity
        image_left_widget = ImageLeftWidget(source="assets/images/eight.jpg")
        self.add_widget(image_left_widget)

    @property
    def name(self):
        return self.text

    @name.setter
    def name(self, value):
        self.text = value
        self._name = value

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value):
        self.__status = value
        self.secondary_text = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
        self.tertiary_text = value

