import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request


url = 'https://www.maxifoot.fr/palmares-ballon-or.htm'

page = urllib.request.urlopen(url, timeout=20)
soup = bs(page)

joueurs = soup.find_all('td', {'class': 'td3'})
liste_joueurs = []
for e in joueurs:
    e = e.text
    liste_joueurs.append(e)


clubs = soup.find_all('td', {'class': 'td4'})
liste_clubs = []
for e in clubs:
    e = e.text
    liste_clubs.append(e)


years = soup.find_all('td', {'class': 'td1'})
liste_years = []
for e in years:
    e = e.text
    if e != "2020":
        liste_years.append(e)


df = pd.DataFrame({'Année': liste_years, 'Joueur': liste_joueurs, 'Club': liste_clubs})
df.to_csv('ballonOr.csv', index=False, encoding='utf-8')