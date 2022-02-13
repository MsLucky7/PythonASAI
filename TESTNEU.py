# A line used mostly as the first one, imports App class
# that is used to get a window and launch the application
from kivy.app import App

# Casual Kivy widgets that reside in kivy.uix
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.spinner import Spinner

from kivy.uix.floatlayout import FloatLayout

from mainNeu import *

# Inherit Screen class and make it look like
# a simple page with navigationation

genres = []
movies = []
topTenMoviesIndices = []

class GenreScreen(Screen):
    
    def __init__(self, **kwargs):
        super(GenreScreen, self).__init__(**kwargs)
        global lableText
        # Content (FloatLayout)
        layout = FloatLayout()

        # Spinners
        self.spinnerObject_1 = Spinner(text="1. Genre auswählen", values=("Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western"))
        self.spinnerObject_1.size_hint  = (0.3, 0.2)
        self.spinnerObject_1.pos_hint={'x': .01, 'y':.75}

        self.spinnerObject_2 = Spinner(text="2. Genre auswählen", values=("Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western"))
        self.spinnerObject_2.size_hint  = (0.3, 0.2)
        self.spinnerObject_2.pos_hint={'x': .35, 'y':.75}

        self.spinnerObject_3 = Spinner(text="2. Genre auswählen", values=("Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "Thriller", "TV Movie", "War", "Western"))
        self.spinnerObject_3.size_hint  = (0.3, 0.2)
        self.spinnerObject_3.pos_hint={'x': .69, 'y':.75}

        self.spinnerSelection = Label(text="Genre")
        self.spinnerSelection.font_size = 50

        # Add Spinners
        layout.add_widget(self.spinnerSelection)
        layout.add_widget(self.spinnerObject_1)
        layout.add_widget(self.spinnerObject_2)
        layout.add_widget(self.spinnerObject_3)

        # Navigation (BoxLayout)
        navigation = BoxLayout(size_hint_y=0.2)

        # Create buttons with a custom text
        prev = Button(text='Previous')
        next = Button(text='Next')

        # Bind to 'on_release' events of Buttons
        prev.bind(on_release=self.switch_prev)
        next.bind(on_release=self.switch_next)
        self.spinnerObject_1.bind(text=self.on_spinner_select_1)
        self.spinnerObject_2.bind(text=self.on_spinner_select_2)        
        self.spinnerObject_3.bind(text=self.on_spinner_select_3)

        # Add buttons to navigationation
        # and the navigationation to layout
        navigation.add_widget(prev)
        navigation.add_widget(next)
        layout.add_widget(navigation)

        # Add the layout to the Screen
        self.add_widget(layout)

    def on_spinner_select_1(self, spinner, text):
        global genre1

        genre1 = text
        
        self.spinnerSelection.text = text + " hinzugefügt"

        print(self.spinnerSelection.text)
        
    def on_spinner_select_2(self, spinner, text):
        global genre2

        self.spinnerSelection.text = text + " hinzugefügt"

        genre2 = text

    def on_spinner_select_3(self, spinner, text):
        global genre3
    
        self.spinnerSelection.text = text + " hinzugefügt"

        genre3 = text

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

    def switch_next(self, *args):
        list_votes = []
        topTenMoviesTitle = []

        genres.append(genre1)
        genres.append(genre2)
        genres.append(genre3)

        for i in range (len(df)):

            for j in range (len(genres)):

                if df["genres"].str.contains(genres[j])[i]:

                    movies.append(df["title"][i])

        indices_titles = get_index_from_title(movies)

        for i in indices_titles:
            list_votes.append([df["vote_average"][i], i])
        # print("Index: ", indices_titles)
        # print("Votes: ", list_votes)
        sorted_list_votes = sorted(list_votes, reverse=True)

        for i in range (10):
            topTenMoviesIndices.append(sorted_list_votes[i][1])
        print(topTenMoviesIndices)
            # print(df["genres"].str.contains("Action"))

        # titles = get_title_from_index(movies)

        # for topMovie in titles:
        #     topTenMoviesTitle.append([df["title"][topMovie], topMovie])

        # print(topTenMoviesTitle)


        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.next()
    
class MovieScreen(Screen):

    def __init__(self, **kwargs):
        super(MovieScreen, self).__init__(**kwargs)
        # Content (FloatLayout)
        layout = BoxLayout()
        layout.my_buttons = []

        for i in topTenMoviesIndices:
            button = Button(text=i)
            layout.my_buttons.append(button)
            layout.add_widget(button)

        # Buttons
        self.movieButton = Button(text="topTenMoviesIndices")
        self.movieButton.size_hint  = (0.3, 0.2)
        self.movieButton.pos_hint={'x': .01, 'y':.75}

        # Add Spinners
        layout.add_widget(self.movieButton)

        # Navigation (BoxLayout)
        navigation = BoxLayout(size_hint_y=0.2)

        # Create buttons with a custom text
        prev = Button(text='Previous')
        next = Button(text='Next')

        # Bind to 'on_release' events of Buttons
        prev.bind(on_release=self.switch_prev)
        next.bind(on_release=self.switch_next)

        # Add buttons to navigationation
        # and the navigationation to layout
        navigation.add_widget(prev)
        navigation.add_widget(next)
        layout.add_widget(navigation)

        # Add the layout to the Screen
        self.add_widget(layout)

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

    def switch_next(self, *args):

        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.next()

class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()

        root.add_widget(GenreScreen(name="Genre Auswahl"))
        root.add_widget(MovieScreen(name="Movies"))

        return root


if __name__ == '__main__':
    # And run the App with its method 'run'
    ScreenManagerApp().run()