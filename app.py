import requests
from bs4 import BeautifulSoup

def fetch():
    url = "https://www.mercadolivre.com.br/console-sony-playstation-5-digital-slim-1tb-branco-jogos-returnal-e-ratchet-clank-controle-sem-fio-dualsense-branco/p/MLB37494438"
    
    response = requests.get(url)
    
    return response.text

def parse(html):
 

    soup = BeautifulSoup(html, 'html.parser')
    
    product_name_tag = soup.find('h1', class_='ui-pdp-title').get_text().strip()
    price = soup.find('span',class_ = 'andes-money-amount__fraction').get_text().strip()

    return product_name_tag,price
    

if __name__ == "__main__":
    dados = fetch()
    
    print(parse(dados))
