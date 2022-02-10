from multiprocessing.spawn import import_main_path
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty, ObjectProperty        # zum lesen der Variablen "Category" und "Movie"
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# import sys
# sys.path.insert(0, '..main')
from mainNeu import *

print(x)

set_titles = set()

# genres = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western"]
class Layout(BoxLayout):
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


        # chosen_genres = set()
        # def getMoviesOfGenres():
        #     for i in range (len(df)):
        #         for j in range (len(selected_values)):
        #             if df["genres"].str.contains(selected_values[j])[i]:
        #                 chosen_genres.add(df["title"][i])
        #         for elements in chosen_genres:
        #             print(elements) #hier sind die Filme

        def hell():
            print("hi")
        hallo = Button(text="hi")
        hallo.bind(on_press=hell)

        # btnSubmit = Button(text="Submit")
        # btnSubmit.bind(on_press=sayHello())

        # class Launch(BoxLayout):
        #     def __init__(self, **kwargs):
        #         super(Launch, self).__init__(**kwargs)
        #         mybutton = Button(
        #                             text = 'Click me',
        #                             size = (80,80),
        #                             size_hint = (None,None)
        #                         )
        #         mybutton.bind(on_press = self.say_hello) # Note: here say_hello doesn't have brackets.
        #         Launch.add_widget(mybutton)

        # def say_hello(self):
        #     print("hello")
    

test_categories = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:

        Label:
            text: 'Genre auswählen'

        MultiSelectSpinner:
            id: genre
            values: "Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western"
            

    BoxLayout:

        Label:
            text: 'Du hast {} als Genres gewählt.'.format(genre.text)

        

        
<MultiSelectOption@ToggleButton>:
    size_hint: 1, None
    height: '30dp'

'''



runTouchApp(Builder.load_string(test_categories))