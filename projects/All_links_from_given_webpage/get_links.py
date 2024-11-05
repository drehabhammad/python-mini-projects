import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link:https://www.msn.com/en-us/news/politics/trump-vs-harris-us-voters-head-to-polls-as-turbulent-campaign-concludes/ar-AA1ty1Tu?ocid=msedgdhp&pc=U531&cvid=1c0b1253dea3495f92314010dae3f7bf&ei=9 ")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("myLinks.txt", 'a') as saved:
    print(links[:10], file=saved)
