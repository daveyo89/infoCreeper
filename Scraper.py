import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, file_name='InfoCreeper/dodofile.txt'):
        self.file_name = file_name

    def get_info(self):
        url = 'https://www.mnb.hu/arfolyamok'
        response = requests.get(url)
        valute_name = []
        value = []
        file = response.text
        soup = BeautifulSoup(file, "html.parser")
        for element in soup.find_all('div', {'class': ['exchangeTable']}):
            try:
                valute_name = [s.find(text=True) for s in element.find_all('td', {'class': ['valutename']}, text=True)]
                value = [s.find(text=True) for s in element.find_all('td', {'class': ['value']}, text=True)]
            except:
                print()
                pass

        return dict(zip(valute_name, value))
