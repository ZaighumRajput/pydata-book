'''
The movie lens example Chapter 2: Python for Data Analysis
'''
import pandas as pd
userNames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('movielens/users.dat', sep='::', header=None,
						names=userNames)
ratingNames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movielens/ratings.dat', sep='::', header=None,
						names = ratingNames)
						
movieNames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movielens/movies.dat', sep='::', header=None,
						names = movieNames)
						
ratingUsersAndMovies = pd.merge(pd.merge(ratings, users), movies)