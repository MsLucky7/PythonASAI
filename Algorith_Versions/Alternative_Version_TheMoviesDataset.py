import pandas as pd
import numpy as np

metadata = pd.read_csv("movies_metadata.csv")
ratings = pd.read_csv("ratings.csv")
credits = pd.read_csv("credits.csv")
keywords = pd.read_csv("keywords.csv")

metadata = metadata.iloc[0:8000,:]

keywords['id'] = keywords['id'].astype('int')
credits['id'] = credits['id'].astype('int')
metadata['id'] = metadata['id'].astype('int')

metadata = metadata.merge(credits, on='id')
metadata = metadata.merge(keywords, on='id')
metadata.drop(['adult','belongs_to_collection','budget','homepage','original_language','original_title','tagline','video','vote_count'],axis=1, inplace=True)
metadata.drop(['vote_average','imdb_id'],axis=1, inplace=True)
metadata.drop(['popularity','poster_path','production_companies','production_countries','release_date','runtime','revenue','spoken_languages','status'],axis=1, inplace=True)
metadata.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
metadata.drop(metadata[metadata.keywords == '[]'].index, inplace=True)
metadata.drop(metadata[metadata.genres == '[]'].index, inplace=True)
metadata.drop(metadata[metadata.overview == '[]'].index, inplace=True)

from ast import literal_eval
features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
  metadata[feature] = metadata[feature].apply(literal_eval)

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

#Getting a list of the actors, keywords and genres
def get_list(x):
    if isinstance(x, list): # if input is a list or not
        names = [i['name'] for i in x] #to get names of actors

        if len(names) > 7:
            names = names[:7]
        return names

    return []


metadata['director'] = metadata['crew'].apply(get_director)

features = ['cast', 'keywords', 'genres']
for feature in features:
    metadata[feature] = metadata[feature].apply(get_list)

metadata[['title', 'cast', 'director', 'keywords', 'genres','overview']].head()

metadata['Key_words'] = ""
metadata['overview'] = metadata['overview'].apply(str)


for index, row in metadata.iterrows():
    plot = row['overview']
    r = Rake()
    r.extract_keywords_from_text(plot)
    key_words_dict_scores = r.get_word_degrees()
    row['Key_words'] = list(key_words_dict_scores.keys())

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x] #cleaning up spaces in the data
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


features = ['cast', 'keywords', 'director', 'genres','Key_words']

for feature in features:
  metadata[feature] = metadata[feature].apply(clean_data)

metadata.head()

def create_soup(x):
    return ' '.join(x['Key_words']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres']) + ' ' + ' '.join(x['keywords'])

metadata['soup'] = metadata.apply(create_soup, axis=1)
metadata[['title', 'soup', 'cast', 'director', 'keywords', 'genres','Key_words']].head()

display(metadata)

#User input for genre, movies

def get_genres():
  genres = input("What Movie Genre are you interested in (if multiple, please separate them with a comma)?")
  genres = " ".join(["".join(n.split()) for n in genres.lower().split(',')])
  return genres

def get_movies():
  movies = input("What are some movies within the genre that you love?")
  movies = " ".join(["".join(n.split()) for n in movies.lower().split(',')])
  return movies

def get_searchTerms():
  searchTerms = []
  genres = get_genres()
  searchTerms.append(genres)

  movies = get_movies()
  searchTerms.append(movies)

  return searchTerms

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def make_recommendation(metadata=metadata):
  new_row = metadata.iloc[-1,:].copy()

  # new wordsoup
  searchTerms = get_searchTerms()
  new_row.iloc[-1] = " ".join(searchTerms)

  metadata = metadata.append(new_row)

  #Vectorizing matrix
  count = CountVectorizer(stop_words='english')
  count_matrix = count.fit_transform(metadata['soup'])

  #Get Similarity Matrix
  cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

  sim_scores = list(enumerate(cosine_sim2[-1,:]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  ranked_titles = []
  for i in range(1, 11):
    indx = sim_scores[i][0]
    ranked_titles.append([metadata['title'].iloc[indx], metadata['genres'].iloc[indx], metadata['soup'].iloc[indx]])

  #Return similarity scores for quality check
  return ranked_titles, sim_scores

make_recommendation()