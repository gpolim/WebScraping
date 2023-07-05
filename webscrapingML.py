import requests
from bs4 import BeautifulSoup
import pandas as pd

lista = []

url = "https://lista.mercadolivre.com.br/"

produto_name = input("Qual o produto que deseja encontrar? ")

response = requests.get(url + produto_name)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = produto.find('span', attrs={'class': 'andes-money-amount__cents'})

    #print('Título do produto:', titulo.text)
    #print('Link do produto:', link['href'])
    #print('Preço do produto: R$', real.text)

    
    lista.append([titulo.text, real.text, link['href']])
    
valores = pd.DataFrame(lista, columns=['Título', 'Valor', "Link"])

valores.to_excel('Valores.xlsx', index=False)
