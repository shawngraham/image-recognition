from bs4 import BeautifulSoup
import csv
import requests

file = open("output.txt", "w")
# f = csv.writer(open("output.csv", "w"))
# f.writerow(["domain", "fulllink"])

pages = []

for i in range(1,2):
    url = 'https://www.cambridgeairphotos.com/themes/earthworks/page' + str(i) + '.html'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.content, "html.parser")


    divs = soup.find_all('div', attrs={"class": "cucapgallery naturalwidth compressed"})

    for div in divs:
        for link in div.find_all('a', attrs={"class": "lightbox"}):
            fulllink = link.get ('href')
            file.writelines(["https://www.cambridgeairphotos.com", fulllink, "\n"])
