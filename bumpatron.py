import operator
import requests
import pprint
from bs4 import BeautifulSoup

URL = 'https://secure.runescape.com/m=forum/c=Iyk8C3QTDCQ/sl=0/forums?320,321,950,66159476,goto,'
pagenum = 1
page = requests.get(URL+str(pagenum))
soup = BeautifulSoup(page.content, 'html.parser')
numpages = soup.find('a','forum-pagination__top-last')

bumps = []

while (pagenum <= int(numpages.text)):
    page = requests.get(URL+str(pagenum))
    soup = BeautifulSoup(page.content, 'html.parser')
    posts = soup.find_all('a','post-avatar__name-link')
    for post in posts:
        bumps.append(post.text)
    print("Processing page " + str(pagenum))
    pagenum = pagenum + 1

hiscores = {}

for bump in bumps:
    if bump not in hiscores:
        hiscores[bump] = 1
    else:
        hiscores[bump] += 1

sortedScores = dict(sorted(hiscores.items(), key=operator.itemgetter(1), reverse=True))

for k in sortedScores:
    print(k, ': ', sortedScores[k])
