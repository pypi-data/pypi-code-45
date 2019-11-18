# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty


class LoadDialog(StackLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(StackLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)
