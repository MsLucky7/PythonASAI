# A line used mostly as the first one, imports App class
# that is used to get a window and launch the application
from ast import IsNot
from operator import is_not
from kivy.app import App

# Casual Kivy widgets that reside in kivy.uix
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.spinner import Spinner

from kivy.properties import StringProperty, ObjectProperty, ListProperty

from kivy.uix.floatlayout import FloatLayout

from Algorithm import *

# Inherit Screen class and make it look like
# a simple page with navigationation

genres = []
movies = set()
topTenMoviesIndices = []
topTenMoviesTitle = []

class GenreScreen(Screen):
    global topTenMoviesTitle
    
    
    def __init__(self, **wwargs):
        super(GenreScreen, self).__init__(**wwargs)
        global lableText
        # Content (FloatLayout)
        layout = FloatLayout()

        # Spinners
        self.spinnerObject_1 = Spinner(text="1. Genre auswählen", values=("action", "adventure", "animation", "comedy", "crime", "documentary", "drama", "family", "fantasy", "foreign", "history", "horror", "music", "mystery", "romance", "sciencefiction", "thriller", "tvmovie", "war", "western"))
        self.spinnerObject_1.size_hint  = (0.3, 0.2)
        self.spinnerObject_1.pos_hint={'x': .01, 'y':.75}

        self.spinnerObject_2 = Spinner(text="2. Genre auswählen", values=("action", "adventure", "animation", "comedy", "crime", "documentary", "drama", "family", "fantasy", "foreign", "history", "horror", "music", "mystery", "romance", "sciencefiction", "thriller", "tvmovie", "war", "western"))
        self.spinnerObject_2.size_hint  = (0.3, 0.2)
        self.spinnerObject_2.pos_hint={'x': .35, 'y':.75}

        self.spinnerObject_3 = Spinner(text="3. Genre auswählen", values=("action", "adventure", "animation", "comedy", "crime", "documentary", "drama", "family", "fantasy", "foreign", "history", "horror", "music", "mystery", "romance", "sciencefiction", "thriller", "tvmovie", "war", "western"))
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
        #topTenMoviesTitle = []

        genres.append(genre1)
        genres.append(genre2)
        genres.append(genre3)

        for i in range (len(data)):

            for j in range (len(genres)):

                if data["genres"].str.contains(genres[j])[i]:

                    movies.add(data["title"][i])

        movies_list = list(movies)
        indices_titles = get_index_from_title(movies_list)

        for i in indices_titles:
            list_votes.append([data["vote_average"][i], i])
        # print("Index: ", indices_titles)
        # print("Votes: ", list_votes)
        sorted_list_votes = sorted(list_votes, reverse=True)

        for i in range (10):
            topTenMoviesIndices.append(sorted_list_votes[i][1])
        # print(topTenMoviesIndices)
            # print(data["genres"].str.contains("action"))

        for elements in topTenMoviesIndices:
            topTenMoviesTitle.append([get_title_from_index(elements), elements])

        # self.manager.liste = ["1", "2", "3", "4"]
        # print(topTenMoviesTitle)


        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.next()
    
class MovieScreen(Screen):
    global topTenMoviesTitle
    

    def on_enter(self):
        print(topTenMoviesTitle)
        counter = 0

        layout = GridLayout(cols=2, rows=6, spacing=4)
        liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


        # print(topTenMoviesTitle)

        for i in range(len(topTenMoviesTitle)):
            self.movieButton_1 = Button(text=str(topTenMoviesTitle[i][0]))
            self.movieButton_1.bind(on_press=self.pressed)
            layout.add_widget(self.movieButton_1)

        # Add Spinners
        #layout.add_widget(self.movieButton)

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

    def __init__(self, **wwargs):
        super(MovieScreen, self).__init__(**wwargs)
        #topTenMoviesTitle = ["Test1", "Test2", "Test3", "Test4"]
        # Content (FloatLayout)
        

    def switch_prev(self, *args):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.previous()

    def switch_next(self, *args):

        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = self.manager.next()

    def pressed(ID1, ID2):
        choosenMovies = []

class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()

        root.add_widget(GenreScreen(name="Genre Auswahl"))
        root.add_widget(MovieScreen(name="Movies"))
        

        return root


if __name__ == '__main__':
    # And run the App with its method 'run'
    ScreenManagerApp().run()