import pandas as pd

"""
The URLs.txt file contains the URLs of the news site pages.
You need to filter it by the addresses of pages with news texts. 
It is known that the news page template has a structure inside the URL: 
/, then 8 digits, then a hyphen.
"""

df = pd.read_csv('URLs.txt')

pattern = r'/\d{8}-'  # for example:  /36012692-
news_urls = df.loc[df.url.str.contains(pattern, case=False, regex=True)]

print(news_urls.head(10))
