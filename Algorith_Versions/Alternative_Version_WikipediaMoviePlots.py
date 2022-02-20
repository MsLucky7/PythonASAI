import pandas as pd
from rake_nltk import Rake
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df4 = pd.read_csv("wiki_movie_plots_deduped.csv")
df4.drop(df4[df4['Release Year'] < 2000].index, inplace=True)
df4.drop(['Wiki Page','Origin/Ethnicity'],axis=1, inplace=True)
df4.drop(df4[df4.Genre == 'unknown'].index, inplace=True)
df4.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

df4['Key_words'] = ""
df4 = df4.apply(lambda x: x.astype(str).str.lower())

for index, row in df4.iterrows():
    plot = row['Plot']

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

features = ['Cast', 'Director', 'Genre','Key_words']

for feature in features:
  df4[feature] = df4[feature].apply(clean_data)

def create_soup(x):
    return ' '.join(x['Key_words']) + ' ' + ' '.join(x['Cast']) + ' ' + x['Director'] + ' ' + ' '.join(x['Genre'])

df4['soup'] = df4.apply(create_soup, axis=1)

display(df4)

def get_genres():
  genres = input("What Movie Genre are you interested in?")
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

def make_recommendation(df4=df4):
  new_row = df4.iloc[-1,:].copy()

  searchTerms = get_searchTerms()
  new_row.iloc[-1] = " ".join(searchTerms)

  df4 = df4.append(new_row)

  count = CountVectorizer(stop_words='english')
  count_matrix = count.fit_transform(df4['soup'])

  cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

  sim_scores = list(enumerate(cosine_sim2[-1,:]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

  ranked_titles = []
  for i in range(1, 11):
    indx = sim_scores[i][0]
    ranked_titles.append([df4['Title'].iloc[indx],df4['Genre'].iloc[indx], df4['soup'].iloc[indx]])

  return ranked_titles, sim_scores

make_recommendation()