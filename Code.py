# GUI
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import sqlite3

class MyGrid(GridLayout)
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        


class MyApp (App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()