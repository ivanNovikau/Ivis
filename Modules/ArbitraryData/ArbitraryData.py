from kivy.uix.label import Label

class ArbitraryData:
    name = "ArbitraryData"

    @staticmethod
    def new_project_screen(name, root):
        scrNewProject = root.sm.get_screen(root.nscr_new_project)
        mspScreen = scrNewProject.ids.mspScreen
        print('Create module specific screen')

        label_name_module = Label(text='Module name: {}'.format(name))
        mspScreen.add_widget(label_name_module)

    def __init__(self, **kwargs):
        self.name = kwargs['name']
