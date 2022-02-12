from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty        # zum lesen der Variablen "Category" und "Movie"
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class MultiSelectSpinner(Button):
    
    # Dropdown initialisieren
    dropdown = ObjectProperty(None)

    # Liste aller Values
    values = ListProperty([])

    # Liste gewählter Values
    selected_values = ListProperty([])

    def __init__(self, **kwargs):
        self.bind(dropdown=self.dropdown_update)
        self.bind(values=self.dropdown_update)
        super(MultiSelectSpinner, self).__init__(**kwargs)
        self.bind(on_release=self.dropdown_toggle)

    # Ansteuern des Dropdowns
    def dropdown_toggle(self, *args):
        if self.dropdown.parent:
            self.dropdown.dismiss()
        else:
            self.dropdown.open(self)

    # Aktualisierung des Dropdowns über 
    def dropdown_update(self, *args):
        if not self.dropdown:
            self.dropdown = DropDown()
        values = self.values
        if values:
            if self.dropdown.children:
                self.dropdown.clear_widgets()
            for value in values:
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.select_value)
                self.dropdown.add_widget(b)

    # Auswählen der Values
    def select_value(self, instance, value):
        if value == 'down':
            if instance.text not in self.selected_values:
                self.selected_values.append(instance.text)
        else:
            if instance.text in self.selected_values:
                self.selected_values.remove(instance.text)

    # Vorbereitung für saubere Ausgabe
    def on_selected_values(self, instance, value):
        if value:
            self.text = ', '.join(value)
        else:
            self.text = ''


test_movies = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:

        Label:
            text: 'Filme auswählen'

        MultiSelectSpinner:
            id: movie
            values: 'Film 1', 'Film 2', 'Film 3', 'Film 4', 'Film 5', 'Film 6', 'Film 7', 'Film 8', 'Film 9', 'Film 10'

    Label:
        text: 'Du hast {} als deine Lieblingsfilme angegeben.'.format(movie.text)

<MultiSelectOption@ToggleButton>:
    size_hint: 1, None
    height: '30dp'

'''

runTouchApp(Builder.load_string(test_movies))