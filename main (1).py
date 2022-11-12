import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"
r= requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table")
rows = soup.find_all("tr")[1:]

countries = []
i = 0

for row in rows:
  items = row.find_all('td')
  name = items[0].text
  coin =  items[2].text
  if items[1].text == "No universal currency":
      continue
  else:
    country = {
    "index": i,
    "name": name.capitalize(),
    "coin": coin
    } 
    countries.append(country)
    i += 1

def menu():
  continuar = ""
  print("Bem-vindo ao Negociador de Moedas")
  print("Escolha pelo número da lista o país que deseja consultar o código da moeda.\n")
  for country in countries:
      print(f"#{country['index']} {country['name']}")   
  while True:  
    try:
      choice = int(input("#: "))
      while choice > country['index']:
        print("Não existe. Escolha uma opção da lista: ")
        choice = int(input("#: "))
      print(f"Você escolheu {countries[choice]['name']}")
      print(f"O código da moeda é {countries[choice]['coin']}")
      continuar = input("Deseja consultar mais moedas ? s/n ")
      if continuar == "s" or continuar == "S":
        continue
      if continuar == "n" or continuar == "N":
        print("Programa finalizado com sucesso")
        break
      while continuar != "s" and continuar != "S" and continuar != "n" and continuar != "N":
        continuar = input("Opção não válida. Escreva s ou n.  ")
        if continuar == "n" or continuar == "N":
          print("Programa finalizado com sucesso")
          break
    except:
      print("Isso não é um número. Escolha uma opção da lista: ")   
menu()