import pandas as pd
import numpy as np
from ast import literal_eval
from rake_nltk import Rake
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import itertools
from IPython.display import display
# import nltk

# nltk.download('stopwords')
# nltk.download('punkt')

df1 = pd.read_csv("tmdb_5000_movies.csv")
df2 = pd.read_csv("tmdb_5000_credits.csv")
data = pd.merge(df1, df2)
data.drop(['budget', 'homepage', 'original_language', 'id', 'movie_id', 'release_date', 'popularity', 'tagline',
           'production_countries', 'production_companies', 'runtime', 'original_title', 'status', 'vote_count',
           'revenue', 'spoken_languages'], axis=1, inplace=True)
data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
data.drop(data[data.keywords == '[]'].index, inplace=True)
data.drop(data[data.genres == '[]'].index, inplace=True)

features = ['cast', 'keywords', 'genres', 'crew']
for feature in features:
    data[feature] = data[feature].apply(literal_eval)


def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan


def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        if len(names) > 7:
            names = names[:7]
        return names
    return []


data['director'] = data['crew'].apply(get_director)

features = ['cast', 'keywords', 'genres']
for feature in features:
    data[feature] = data[feature].apply(get_list)

data.drop('crew', axis=1, inplace=True)

data['Key_words'] = ""
data['overview'] = data['overview'].apply(str)

for index, row in data.iterrows():
    plot = row['overview']
    r = Rake()
    r.extract_keywords_from_text(plot)
    key_words_dict_scores = r.get_word_degrees()
    row['Key_words'] = list(key_words_dict_scores.keys())


def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


features = ['cast', 'keywords', 'director', 'genres', 'Key_words']

for feature in features:
    data[feature] = data[feature].apply(clean_data)


def create_soup(x):
    return ' '.join(x['Key_words']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(
        x['genres']) + ' ' + ' '.join(x['keywords'])


data['soup'] = data.apply(create_soup, axis=1)
data['index'] = data.index

display(data)

cv = CountVectorizer()
count_matrix = cv.fit_transform(data['soup'])
cosine_sim = cosine_similarity(count_matrix)

sim_scores = list(enumerate(cosine_sim[-1, :]))
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

print(data['genres'][0])