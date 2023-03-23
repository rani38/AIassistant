import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# read in the csv file for movie data
df = pd.read_csv(f'assets/books.csv', on_bad_lines='skip')

df.replace(to_replace='J.K. Rowling-Mary GrandPré', value = 'J.K. Rowling', inplace=True)

data2 = df.copy()

data2.loc[ (data2['average_rating'] >= 0) & (data2['average_rating'] <= 1), 'rating_between'] = "between 0 and 1"
data2.loc[ (data2['average_rating'] > 1) & (data2['average_rating'] <= 2), 'rating_between'] = "between 1 and 2"
data2.loc[ (data2['average_rating'] > 2) & (data2['average_rating'] <= 3), 'rating_between'] = "between 2 and 3"
data2.loc[ (data2['average_rating'] > 3) & (data2['average_rating'] <= 4), 'rating_between'] = "between 3 and 4"
data2.loc[ (data2['average_rating'] > 4) & (data2['average_rating'] <= 5), 'rating_between'] = "between 4 and 5"

rating_data = pd.get_dummies(data2['rating_between'])
language_data = pd.get_dummies(data2['language_code'])

features = pd.concat([rating_data, 
                     language_data,
                     data2['average_rating'],
                     data2['ratings_count']], axis=1)

min_max_scaler = MinMaxScaler()
features_new = min_max_scaler.fit_transform(features)

model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
model.fit(features_new)
dist, idlist = model.kneighbors(features_new)

def book_recommender(book_name):

    capitalize_name = book_name.title()

    book_list_name = []
    book_id = data2[data2['title'] == capitalize_name].index
    print(book_id)
    book_id = book_id[0]
    for new_id in idlist[book_id]:
        book_list_name.append(data2.loc[new_id].title)

    return ','.join(str(item) for item in book_list_name) 

x = train_test_split(features_new, test_size=0.2, random_state=42)
x


# print(f"Here are your book reccommendations:")
# BookNames = book_recommender('The Hobbit')
# print(BookNames)