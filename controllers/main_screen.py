import threading
import time

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    def do_loading(self, *args):
        self.dialog = MDDialog(
            text='Hi',
            on_dismiss=lambda x: True,
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_press=lambda x: self.dialog_close()
                ),
            ]
        )
        self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)