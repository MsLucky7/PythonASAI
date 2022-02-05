from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from kivy.base import runTouchApp

class MyStuff(GridLayout):
    meinGenre = "action"
    

    def __init__(self, **kwargs):
        super(MyStuff, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        dropdown = DropDown()
        for index in range(10):
            btn = Button(text="Value %d" % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            self.inside.add_widget(btn)

        mainbutton = Button(text="Genre wählen", size_hint=(None, None))

        mainbutton.bind(on_release=dropdown.open)

        self.inside.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        self.inside.add_widget(Label(text="Titel: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Tags: "))
        self.pp = TextInput(multiline=False)
        self.inside.add_widget(self.pp)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        genre = self.genre
        titel = self.lastName.text

        # Konsolen ausgaben
        print("Genre: " + genre)
        print("title:" + titel)

        return genre, titel

class MyApp(App):
    def build(self):
        return MyStuff()

if __name__ == "__main__":
    MyApp().run()