import pandas as pd
import matplotlib.pyplot as plt
import json
import os


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

# read in the csv file for movie data
df = pd.read_csv(f'assets/tmdb_5000_movies.csv', low_memory=False)

x = df.iloc[0] # retrieve first row of using iloc

x['genres']
x['keywords']
j = json.loads(x['genres'])

' '.join(''.join(jj['name'].split()) for jj in j)

# convert the relevant data for each movie into a single string 
# to be ingested by the TfidVectorizer

def genres_and_keywords_to_string(row):
  genres = json.loads(row['genres'])
  genres = ' '.join(''.join(j['name'].split()) for j in genres)

  keywords = json.loads(row['keywords'])
  keywords = ' '.join(''.join(j['name'].split()) for j in keywords)
  return "%s %s" % (genres, keywords)

# create a new string representation of each movie
df['string'] = df.apply(genres_and_keywords_to_string, axis=1)

# create a tf-idf vectorizer object
tfidf = TfidfVectorizer(max_features=2000)

# create a data matrix from the overviews
X = tfidf.fit_transform(df['string'])

# generate mapping from movie title -> index (in df)
movie2idx= pd.Series(df.index, index=df['title'])
# movie2idx

idx = movie2idx['Avatar']
# idx

query = X[idx]
# query

# print the query vector
query.toarray()

# compute similarity between query and every vector in x
scores = cosine_similarity(query, X)
# scores

# currently the array is 1 x N, make it jusr a 1-D array
scores = scores.flatten()

(-scores).argsort()

# get top 5 matches
# exclude self (similarity between query and itself yields max score)
reccommend_idx = (-scores).argsort()[1:6]

# convert indices back to titles
df['title'].iloc[reccommend_idx]

# create a function that generates reccommendations

def reccommend(title):
  # get the row in the dataframe for this movie
  idx = movie2idx[title]
  if type(idx) == pd.Series:
      idx = idx.iloc[0]
  
  # calculate the pairwise similarites for this movie
  query = X[idx]
  scores = cosine_similarity(query, X)

  # currently the array is 1 x N, make it jusr a 1-D array
  scores = scores.flatten()

  # get the indexes of the highest scoring movies
  # get the first K reccommendations
  # don't return itself
  reccommend_idx = (-scores).argsort()[1:6]

  # return the titles of the reccommendations
  return df['title'].iloc[reccommend_idx]


print(f"Here are your film reccommendations:")
print(reccommend('Star Trek Into Darkness'))



