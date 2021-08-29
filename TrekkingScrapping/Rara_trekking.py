import requests
from bs4 import BeautifulSoup
import csv
root = 'https://www.welcomenepal.com/'
website = f'{root}/places-to-see/rara.html'
result = requests.get(website)
content = result.text
"""using parser to get the html code"""
soup = BeautifulSoup(content, "lxml")
#print(soup.prettify())
"""We look at element and then class. we have given the variable name box to store title"""
box = soup.find('div', class_='carousel-caption')
title = box.find('h2').get_text()
title_description = box.find('h4').get_text()
"""print(title)
print(title_description)"""
page_header = soup.find('div', class_='col-md-7 col-sm-7')
header_title = page_header.find('h1').get_text()
"""print(header_title)"""
links = []
for link in page_header.find_all('a', href=True):
    links.append(link['href'])
print(links)

images = []
for img in page_header.findAll('img'):
    images.append(img.get('src'))
print(images)

information =''
for information in page_header.find_all("p"):
    print(information.get_text(strip=True, separator=''))
    output = {'title': title, 'title_description': title_description, 'header_title':header_title,'links':links, 'images_links':images, 'information': information}
    with open('rara_treeking.csv', 'w') as file:
        file.write(str(output))


