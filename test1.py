import requests
from bs4 import BeautifulSoup
import sys


Targeted_url = 'https://www.trademap.org/'
requested01 = requests.get(Targeted_url)

test_1 = BeautifulSoup(requested01.text, 'html.parser')

sys.stdout = open('trade.txt', 'w')

print(test_1)

sys.stdout.close()