from kivy.uix.screenmanager import FallOutTransition
from kivymd.uix.screenmanager import MDScreenManager


class MyScreenManager(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transition = FallOutTransition()
