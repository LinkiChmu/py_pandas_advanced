import pandas as pd

"""
Using the ratings.csv file, calculate the average lifetime of users who have rated
more than 100 ratings. The lifetime is the difference between the maximum and 
minimum values of the timestamp column for a given userId value.
"""

df = pd.read_csv('ratings.csv')
grouped = df.groupby('userId')

min_max = grouped.agg(['min', 'max'])['timestamp']
min_max['life_time'] = min_max['max'] - min_max['min']

counts = grouped.count()
active_users = counts.loc[counts.rating > 100]  # select users who have given > 100 ratings

joined = active_users.join(min_max, how='left')
avg_life_time = joined.life_time.mean()

print(avg_life_time)
