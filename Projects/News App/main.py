import requests as r
from datetime import date, timedelta

d=date.today() - timedelta(days=1)
api = "17ed2eb7de8e47608ec281e64eb3f3f0"
query = input("What news are you interested in today?\n")
url = ('https://newsapi.org/v2/everything?'
       f'q={query}&'
       f'from={d}&'
       'sortBy=popularity&'
       f'apiKey={api}')

req = r.get(url)

for index, article in enumerate(req.json()['articles']):
    print(index+1, article['title'])
    print(article['description'])
    print(article['url'])
    print("\n********************************\n")