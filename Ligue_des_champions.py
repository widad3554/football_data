import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request


url = 'https://www.maxifoot.fr/palmares-ligue-champion.htm'

page = urllib.request.urlopen(url, timeout=20)
soup = bs(page)

lieux = soup.find_all('td', {'class': 'l1'})
liste_lieux = []
for e in lieux:
    e = e.text
    liste_lieux.append(e)


clubs = soup.find_all('td', {'class': 'e1'})
liste_clubs = []
for e in clubs:
    e = e.text
    liste_clubs.append(e)


years = soup.find_all('td', {'class': 'a1'})
liste_years = []
for e in years:
    e = e.text
    liste_years.append(e)


df = pd.DataFrame({'Année': liste_years, 'Club': liste_clubs, 'Lieu_finale ': liste_lieux})
df.to_csv('ligue_des_champions.csv', index=False, encoding='utf-8')