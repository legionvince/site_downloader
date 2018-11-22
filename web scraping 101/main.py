import requests
import re
from bs4 import BeautifulSoup

#url = 'https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486'
url1 = input("Enter a URL: ")
file_name = input("Enter a filename: ") + ".html"
response = requests.get(url1)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]

with open(file_name, "w+", encoding = 'utf-8') as f:
    f.write(soup.get_text())
    f.close

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url: 
            url = '{}{}'.format(url1, url)
        response = requests.get(url)
        f.write(response.content)
