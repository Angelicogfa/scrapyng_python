# !pip install webbrowser -U --user
# !pip install pandas -U --user
#%% imports
import webbrowser as wb
from bs4 import BeautifulSoup
import requests as req
import pandas as pd

#%% Sample 1
address = 'Praça das Cerejeiras, 59, Bauru - SP'
wb.open('https://www.google.com/maps/place/{}'.format(address))


#%% Sample 2
# BeautifulSoup - Responsanvel por procurar os elementos html
print('Googling...')
url = 'http://google.com/search?q={}'
res = req.get(url.format('carnaval brasil'))
res.status_code
res.text
res.content

soup = BeautifulSoup(res.text, 'html.parser')

linkElements = soup.find_all('a')
for i in range(len(linkElements)):
    print(linkElements[i].get('href'))

for i in range(0, 5):
    wb.open(url.format(linkElements[i].get('href')))


#%% Documentação
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#


#%% Sample 3
doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(doc, 'html.parser')
soup

print(soup.prettify())
soup.title
soup.title.name
soup.title.text
soup.p
soup.p.text
soup.find_all('p')
soup.find_all('a')
print(soup.get_text())


#%%
# Exemplo analise de site http://guiadacozinha.com.br
url = 'http://guiadacozinha.com.br/{}'
res = req.get(url.format('receita-de-hamburguer-caseiro-facil'))
soup = BeautifulSoup(res.text, 'html.parser')
body = soup.find('article', { 'class': 'content-body'})
print(body.prettify())
print('Titulo %s' % body.find('h1').text)
details = body.find('div', { 'class': 'p402_premium' })
print(details.prettify())
for item in details.find('ul').find_all('li'):
    print(item.text)


#%% links
res = req.get(url.format('category/almoco-do-domingo'))
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())

for card in soup.find_all('div', { 'class': 'recipe-card'}):
    print(card.find('a')['href'])

#%% Tabelas
url = 'http://en.wikipedia.org/wiki/{}'
res = req.get(url.format('List_of_FIFA_World_Cup_finals'))
res.status_code

soup = BeautifulSoup(res.text, 'html.parser')

tables = soup.find_all('table')
print(tables[0].prettify())

data = []
for tr in tables[2].find_all('tr'):
    cols = tr.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols])

df = pd.DataFrame(data, columns = ['Winners', 'Final Score', 'Runners-up', 'Venue', 'Location', 'Attendance', 'Reference'])
df = df.drop(df[pd.isnull(df['Winners'])].index)
df

#%% Cripto moedas
url = 'https://coinmarketcap.com/pt-br'
res = req.get(url)
res.status_code

soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
table = soup.find('table', { 'id': 'currencies' })
table_body = table.find('tbody')

rows = table_body.find_all('tr')
# ... (continuar)