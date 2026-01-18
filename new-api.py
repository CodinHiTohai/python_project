import requests

query="artificial intelligence"
api="98d12a78bfae452194f24548d54f90dd"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-12-18&sortBy=publishedAt&apiKey={api}"

#print(url)
r=requests.get(url)
data=r.json()
articles=data["articles"]

for index, article in enumerate(articles):
    print( index+1, article["title"],article["url"])
    print("\n*******************************\n")
