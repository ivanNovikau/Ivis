import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# replace with your current kivy version !
kivy.require('1.11.1')


class StartMenu(GridLayout):
    def __init__(self, **kwargs):
        # implement the functionality of the original class being overloaded
        super(StartMenu, self).__init__(**kwargs)
        self.cols = 2

        # row 1
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # row 2
        self.add_widget(Label(text='Folder'))
        self.folder = TextInput(multiline=False)
        self.add_widget(self.folder)


class Ivis(App):  # -> subclass of the kivy.app class
    def build(self):  # -> has to be implemented
        return StartMenu()  # -> has to return a Widget Instance

# class Ivis(App):  # -> subclass of the kivy.app class
#
#     def build(self):  # -> has to be implemented
#         return Label(text='Hello world 2')  # -> has to return a Widget Instance


# *** Starting point ***
if __name__ == '__main__':
    Ivis().run()
