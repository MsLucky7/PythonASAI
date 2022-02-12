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

# print(df["genres"])

# def get_title_from_index(index):
#     return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    index_list = []
    for i in range (len(title)):
        index_list.append(df[df.title == title[i]]["index"].values[0])
    return index_list

genres = ['Horror']
chosen_genres = []

for i in range (len(df)):
    for j in range (len(genres)):
        if df["genres"].str.contains(genres[j])[i]:
            chosen_genres.append(df["title"][i])

indices_titles = get_index_from_title(chosen_genres)
list_votes = []

for i in indices_titles:
    list_votes.append([df["vote_average"][i], i])
# print("Index: ", indices_titles)
# print("Votes: ", list_votes)
sorted_list_votes = sorted(list_votes, reverse=True)

for i in range (10):
    print(sorted_list_votes[i])
    print(df["vote_average"][2170])
    print(df["combined_features"][2170])
    print(df["title"][2170])
    # print(df["genres"].str.contains("Action"))

