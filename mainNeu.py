import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import itertools

df = pd.read_csv("movie_dataset.csv")

features = ['keywords','cast','genres','director']

def combine_features(row):
    return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]

for feature in features:
    df[feature] = df[feature].fillna('')
df["combined_features"] = df.apply(combine_features,axis=1)
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    index_list = []
    for i in range (len(title)):
        index_list.append(df[df.title == title[i]]["index"].values[0])
    return index_list

movies_user_likes = ["The Dark Knight Rises", "Spider-Man 2", "X-Men: The Last Stand", "Diary of a Wimpy Kid: Dog Days", "Avatar", "Skyfall"]
movie_index = get_index_from_title(movies_user_likes)

length_list = len(movies_user_likes)
similar_movies_user_likes_list = []

for i in range (length_list):
    similar_movies_user_likes_list.append( list(enumerate(cosine_sim[movie_index[i]])) )

# make list one dimensional, sort list by most liked according to cosine
list_of_similar_movies_user_likes = list(itertools.chain.from_iterable(similar_movies_user_likes_list))
sorted_similar_movies_user_likes = sorted(list_of_similar_movies_user_likes,key=lambda x:x[1],reverse=True)[1:]

# remove first few movies, which are "movies user likes" itself
for i in range (length_list):
    sorted_similar_movies_user_likes.pop(0)

i=0
print("Top 5 similar movies_user_likes to " + " are:\n")
for element in sorted_similar_movies_user_likes:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>=5:
        break