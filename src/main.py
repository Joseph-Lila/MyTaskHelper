from kivy.factory import Factory
from kivymd.app import MDApp


class MyTaskHelper(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.material_style = 'M3'
        return Factory.MainContainer()


if __name__ == '__main__':
    MyTaskHelper().run()
