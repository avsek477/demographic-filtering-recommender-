import pandas as pd
import numpy as np

df1 = pd.read_csv('./credits.csv')
df2 = pd.read_csv('./movies.csv')

df1.columns = ['id', 'title', 'cast', 'crew']
df2 = df2.merge(df1, on = 'id')

C = df2['vote_average'].mean()

m = df2['vote_count'].quantile(0.9)

q_movies = df2.copy().loc[df2['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m)*R) + (m/(v+m)*C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)
print(q_movies[['title_x', 'vote_count', 'vote_average', 'score']].head(10))
