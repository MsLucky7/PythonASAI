from kivy.uix.button import Button # You would need futhermore this
from kivy.uix.boxlayout import BoxLayout

class Launch(BoxLayout):
    def __init__(self, **kwargs):
        super(Launch, self).__init__(**kwargs)
        mybutton = Button(
                            text = 'Click me',
                            size = (80,80),
                            size_hint = (None,None)
                          )
        mybutton.bind(on_press = self.say_hello) # Note: here say_hello doesn't have brackets.
        Launch.add_widget(mybutton)

    def say_hello(self):
        print("hello")




# from kivy.app import App

# from kivy.uix.button import Button

# from kivy.uix.label import Label

# class Test(App):

#     def press(self,instance):
#         print("Pressed")
#     def build(self):
#         butt=Button(text="Click")
#         butt.bind(on_press=self.press) #dont use brackets while calling function
#         return butt

# Test().run()

