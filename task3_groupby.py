import pandas as pd

"""
Using the ratings.csv file, calculate the average lifetime of users who have rated
more than 100 ratings. The lifetime is the difference between the maximum and 
minimum values of the timestamp column for a given userId value.
"""

ratings = pd.read_csv('ratings.csv')

agg = ratings.groupby('userId').aggregate({'timestamp': ['min', 'max'], 'rating': 'count'})
agg['life_time'] = agg['timestamp']['max'] - agg['timestamp']['min']
avg_life_time = agg.loc[agg['rating']['count'] > 100]['life_time'].mean()

print(avg_life_time)
