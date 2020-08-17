import requests
import yaml
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, file_name='InfoCreeper/dodofile.txt'):
        self.file_name = file_name

    def get_info(self, specs):
        url = specs['website']
        response = requests.get(url)
        element_classes = specs['element_classes'].split(',')
        valute_name = []
        value = []
        file = response.text
        soup = BeautifulSoup(file, "html.parser")
        for element in soup.find_all(specs['parent'], {'class': [specs['class']]}):
            try:
                valute_name = [s.find(text=True) for s in
                               element.find_all(specs['element_type'], {'class': [element_classes[0]]}, text=True)]
                value = [s.find(text=True) for s in
                         element.find_all(specs['element_type'], {'class': [element_classes[1]]}, text=True)]
            except:
                print()
                pass

        return dict(zip(valute_name, value))
