from kivy.factory import Factory
from controllers.main_container import MainContainer
from controllers.my_screen_manager import MyScreenManager
from controllers.personal_office_screen import PersonalOfficeScreen
from controllers.main_screen import MainScreen


Factory.register(cls=MainContainer, classname="MainContainer")
Factory.register(cls=MyScreenManager, classname="MyScreenManager")
Factory.register(cls=PersonalOfficeScreen, classname="PersonalOfficeScreen")
Factory.register(cls=MainScreen, classname="MainScreen")
