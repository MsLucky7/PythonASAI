# Sample spinner app in kivy 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from kivy.uix.floatlayout import FloatLayout

from kivy.app import App

from mainNeu import *

genres = set()
movies = set()
genre1 = ''

# Make an App by deriving from the App class
class ChooseGenre(App):
    
    def build(self):
        layout = FloatLayout()
        
        # add and configure spinnerObjects
        self.spinnerObject_1 = Spinner(text="1. Genre auswählen", values=("Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western")) 
        self.spinnerObject_2 = Spinner(text="2. Genre auswählen", values=("Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western")) 
        self.spinnerObject_3 = Spinner(text="3. Genre auswählen", values=("Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western")) 
        self.spinnerObject_1.size_hint  = (0.3, 0.2)
        self.spinnerObject_2.size_hint  = (0.3, 0.2)
        self.spinnerObject_3.size_hint  = (0.3, 0.2)
        self.spinnerObject_1.pos_hint={'x': .01, 'y':.75}
        self.spinnerObject_2.pos_hint={'x': .35, 'y':.75}
        self.spinnerObject_3.pos_hint={'x': .69, 'y':.75}
        layout.add_widget(self.spinnerObject_1)
        layout.add_widget(self.spinnerObject_2)
        layout.add_widget(self.spinnerObject_3)
        self.spinnerObject_1.bind(text=self.on_spinner_select_1)
        self.spinnerObject_2.bind(text=self.on_spinner_select_2)
        self.spinnerObject_3.bind(text=self.on_spinner_select_3)
        
        # add label
        self.spinnerSelection = Label(text="Deine Genres: ")
        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint={'x': .0, 'y':.0}

        # add submit Button
        self.submitButton = Button(text="Submit")
        self.submitButton.size_hint = (0.5, 0.3)
        self.submitButton.pos_hint = {'x': .25, 'y': .05}
        layout.add_widget(self.submitButton)
        self.submitButton.bind(on_press=self.returnList)
        
        return layout

    # spinnerObjects fuctions
    def on_spinner_select_1(self, spinner, text):
        global genre1

        if self.spinnerObject_2.text == "2. Genre auswählen" and self.spinnerObject_3.text == "3. Genre auswählen":
            self.spinnerSelection.text = "Dein Genre: %s"%self.spinnerObject_1.text
        if self.spinnerObject_3.text == "3. Genre auswählen" and self.spinnerObject_2.text != "2. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_2.text
        if self.spinnerObject_2.text == "2. Genre auswählen" and self.spinnerObject_3.text != "3. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_3.text
        if self.spinnerObject_2.text != "2. Genre auswählen" and self.spinnerObject_3.text != "3. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_2.text + " und %s"%self.spinnerObject_3.text

        genre1 = self.spinnerObject_1.text

    def on_spinner_select_2(self, spinner, text):
        global genre2

        if self.spinnerObject_1.text == "1. Genre auswählen" and self.spinnerObject_3.text == "3. Genre auswählen":
            self.spinnerSelection.text = "Dein Genre: %s"%self.spinnerObject_2.text
        if self.spinnerObject_3.text == "3. Genre auswählen" and self.spinnerObject_1.text != "1. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_2.text
        if self.spinnerObject_1.text == "1. Genre auswählen" and self.spinnerObject_3.text != "3. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_2.text + ", %s"%self.spinnerObject_3.text
        if self.spinnerObject_1.text != "1. Genre auswählen" and self.spinnerObject_3.text != "3. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_2.text + " und %s"%self.spinnerObject_3.text

        genre2 = self.spinnerObject_2.text

    def on_spinner_select_3(self, spinner, text):
        global genre3
        
        if self.spinnerObject_2.text == "2. Genre auswählen" and self.spinnerObject_1.text == "1. Genre auswählen":
            self.spinnerSelection.text = "Dein Genre: %s"%self.spinnerObject_3.text
        if self.spinnerObject_1.text == "1. Genre auswählen" and self.spinnerObject_2.text != "2. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_2.text + ", %s"%self.spinnerObject_3.text
        if self.spinnerObject_2.text == "2. Genre auswählen" and self.spinnerObject_1.text != "1. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_3.text
        if self.spinnerObject_2.text != "2. Genre auswählen" and self.spinnerObject_1.text != "1. Genre auswählen":
            self.spinnerSelection.text = "Deine Genres: %s"%self.spinnerObject_1.text + ", %s"%self.spinnerObject_2.text + " und %s"%self.spinnerObject_3.text

        genre3 = self.spinnerObject_3.text
    
    def returnList(spinnerID, spinnerButtonID):
        genres.add(genre1)
        genres.add(genre2)
        genres.add(genre3)

        for i in range (len(df)):

            for j in range (len(genres)):

                if df["genres"].str.contains(genres[j])[i]:

                    movies.add(df["title"][i])

        for elements in movies:

            print(elements)
        
        print(genres)

# Run the app
if __name__ == '__main__':
    ChooseGenre().run()    