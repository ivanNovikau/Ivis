import os
import importlib

import kivy
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

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

# replace with your current kivy version !
kivy.require('1.11.1')


class StartScreen(Screen):  # Empty screen
    pass


class NewProjectScreen(Screen):
    root_path = None
    project_name = None
    init_conf_file_name = None

    def __init__(self, **kwargs):
        super(NewProjectScreen, self).__init__(**kwargs)

        # create inputs
        self.ids.root_path_input.bind(on_text_validate=self.set_root_path)
        self.ids.project_name_input.bind(on_text_validate=self.set_project_name)
        self.ids.init_conf_input.bind(on_text_validate=self.set_init_conf_file_name)

    def set_root_path(self, instance):
        self.root_path = instance.text

    def set_project_name(self, instance):
        self.project_name = instance.text

    def set_init_conf_file_name(self, instance):
        self.init_conf_file_name = instance.text


class StartMenu(Screen):
    # running application
    app = None

    # screen manage
    sm = None
    nscr_start = 'start'
    nscr_new_project = 'new_project'

    # modules
    dir_with_modules = "Modules"
    names_available_modules = []
    available_modules = {}
    work_module = None

    def __init__(self, current_app, **kwargs):
        super(StartMenu, self).__init__(**kwargs)
        self.app = current_app

        # * Create Screens *
        self.sm = self.ids.sm
        self.sm.add_widget(StartScreen(name=self.nscr_start))
        self.sm.add_widget(NewProjectScreen(name=self.nscr_new_project))

        # * Find available modules *
        self.find_modules()

        # * File Button *
        self.drop_file()

    # --- create DropDown File list ---
    def drop_file(self):
        dd_file = DropDown()

        # - New Project -
        btn = Button(text="New Project", size_hint_y=None, height=44)
        btn.bind(on_release=lambda _: self.new_project(dd_file))
        dd_file.add_widget(btn)

        # - Open Project -
        btn = Button(text="Open Project", size_hint_y=None, height=44)
        btn.bind(on_release=lambda _: self.open_project(dd_file))
        dd_file.add_widget(btn)

        # - Open Recent Project -
        btn = Button(text="Open Recent Project", size_hint_y=None, height=44)
        btn.bind(on_release=lambda _: self.open_recent_project(dd_file))
        dd_file.add_widget(btn)

        # - Exit -
        btn = Button(text="Exit", size_hint_y=None, height=44)
        btn.bind(on_release=lambda _: self.quit(dd_file))
        dd_file.add_widget(btn)

        # -- Connect the DropDown list with the File button --
        bfile = self.ids.start_bFile
        bfile.bind(on_release=dd_file.open)
        dd_file.bind(on_select=lambda _: None)

    def new_project(self, dd_file):
        print("New Project")
        dd_file.dismiss()
        self.sm.current = "new_project"

        # - Put names of available modules to the Spinner on the New Project Screen -
        scrNewProject = self.sm.get_screen(self.nscr_new_project)
        spModule = scrNewProject.ids.spModule
        spModule.values = self.names_available_modules
        spModule.bind(text=self.module_chosen)

    def open_project(self, dd_file):
        print("Open Project")
        dd_file.dismiss()

    def open_recent_project(self, dd_file):
        print("Open Recent Project")
        dd_file.dismiss()

    def quit(self, dd_file):
        dd_file.dismiss()
        stopTouchApp()

    def find_modules(self):
        sub_dires = [x[0] for x in os.walk(self.dir_with_modules)]
        res_modules = []
        for one_sub_dir in sub_dires:
            res_dir = one_sub_dir.replace(self.dir_with_modules, '')[1:]
            res_dir = res_dir.split("\\", 1)[0]
            if len(res_dir) > 0:
                res_modules.append(res_dir)
        self.names_available_modules = list(set(res_modules))
        print(self.names_available_modules)

        # import modules
        for name_module in self.names_available_modules:
            module_folder = "Modules." + name_module
            self.available_modules[name_module] = importlib.import_module(
                module_folder + "." + name_module
            )

    def module_chosen(self, _, name_module):
        # clean the module specific screen
        scrNewProject = self.sm.get_screen(self.nscr_new_project)
        mspScreen = scrNewProject.ids.mspScreen
        mspScreen.clear_widgets()

        # create the module specific screen
        class_module = getattr(self.available_modules[name_module], name_module)
        class_module.new_project_screen(name_module, self)


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