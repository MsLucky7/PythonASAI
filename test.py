from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyStuff(GridLayout):
    def __init__(self, **kwargs):
        super(MyStuff, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="pp: "))
        self.pp = TextInput(multiline=False)
        self.inside.add_widget(self.pp)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.firstName.text
        last = self.lastName.text

        print(name, last)

class MyApp(App):
    def build(self):
        return MyStuff()

if __name__ == "__main__":
    MyApp().run()