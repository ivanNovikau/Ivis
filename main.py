import kivy
import kivy.uix.button as kb
from kivy.app import App
from kivy.base import runTouchApp, stopTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.splitter import Splitter
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

from kivy.uix.boxlayout import BoxLayout


import ArbitraryData as AD


# replace with your current kivy version !
kivy.require('1.11.1')


class StartMenu(BoxLayout):
    app = None
    work_module = None

    def __init__(self, current_app, **kwargs):
        super(StartMenu, self).__init__(**kwargs)
        self.work_module = AD.ArbitraryData()
        self.app = current_app

    def new_project(self):
        print(self.work_module.module_name)
        print(self.app.name_app)

        # for child in self.children:

    def quit(self):
        stopTouchApp()
        # self.app.stop()
        # App.get_running_app().stop()


class IvisApp(App):
    name_app = 'App'

    def build(self):
        return StartMenu(current_app=self)

    def on_pause(self):
        # Here you can save data if needed
        return True

    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass

    def on_stop(self, *args):
        print('Save data')
        print('Exit from the application')


if __name__ == '__main__':
    IvisApp().run()







    # class PongBall(Widget):
    #     velocity_x = NumericProperty(0)
    #     velocity_y = NumericProperty(0)
    #     velocity = ReferenceListProperty(velocity_x, velocity_y)
    #
    #     def move(self):
    #         self.pos = Vector(*self.velocity) + self.pos

    # class ButtonNewProject()

    # def __init__(self, **kwargs):
    #     # implement the functionality of the original class being overloaded
    #     super(StartMenu, self).__init__(**kwargs)
    #     self.cols = 2
    #
    #     # row 1
    #     self.add_widget(Label(text='User Name'))
    #     self.username = TextInput(multiline=False)
    #     self.add_widget(self.username)
    #
    #     # row 2
    #     self.add_widget(Label(text='Folder'))
    #     self.folder = TextInput(multiline=False)
    #     self.add_widget(self.folder)