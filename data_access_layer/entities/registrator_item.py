import datetime


class RegistratorItem:
    def __init__(self, entity_name, quantity, time):
        self.entity_name = entity_name
        self.quantity = quantity
        self.__time = datetime.datetime.now()

    @property
    def time(self):
        return self.__time
    