from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty        # zum lesen der Variablen "Category" und "Movie"
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class My_class(BoxLayout):

    def on_checkbox_active(checkbox_ref, name, checkbox_value):
        if checkbox_value:
            print('', name, 'is active')
        else:
            print('', name, 'is inactive')
    pass