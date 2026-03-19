import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

rating_df = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\Recommendation Engine-Part 2\\ratings.csv')
rating_df.head()
movie_df = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\Recommendation Engine-Part 2\\movies.csv')
movie_df.head()

movie_df['year'] = movie_df.title.str.extract('(\(\d\d\d\d\))', expand=True)
movie_df.head()

movie_df['year'] = movie_df['year'].str.extract('(\d\d\d\d)', expand=True)
movie_df.head()

movie_df['title'] = movie_df.title.str.replace('(\(\d\d\d\d\))', '')
movie_df.head()
movie_df['title'] = movie_df['title'].apply(lambda x: x.strip())

movie_df['genres'] = movie_df['genres'].str.split('|')
movie_df.head()

movie_copy = movie_df.copy()

for index, row in movie_copy.iterrows():
    for genre in row['genres']:
        movie_df.at[index, genre] = 1

movie_copy.head()

movie_copy = movie_copy.fillna(0)
movie_copy.head()

ratings_df = rating_df.drop('timestamp', axis=1)
ratings_df.head()

user_input = [
    {'title': 'Grand Slam', 'rating': 5.6},
    {'title': 'Zero', 'rating': 7},
    {'title': 'Jumanji', 'rating': 8.5},
    {'title': 'Toy Story', 'rating': 4.5},
]

movie_input = pd.DataFrame(user_input)
movie_input
print(movie_input)

input_id = movie_df[movie_df['title'].isin(movie_input['title'].tolist())]
movie_input = pd.merge(input_id, movie_input)
movie_input
print(movie_input)

movie_input = movie_input.drop(['genres', 'year'], axis=1)
movie_input
print(movie_input)

movie_user = movie_copy[movie_copy['movieId'].isin(movie_input['movieId'].tolist())]
movie_user
print(movie_user)

movie_user = movie_user.reset_index(drop=True)
movie_user
print(movie_user)

UserGenreTable = movie_user.drop(['movieId', 'title','genres',  'year'], axis=1)
UserGenreTable
print(UserGenreTable)