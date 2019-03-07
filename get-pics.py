import csv
import requests
import re

img = []
with open('output.txt') as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvrows:
        filename = row[0]
        filename = re.sub('["\bhttps://www.cambridgeairphotos.com/data/thumbnails\b"]', '', filename)
        url = row[0]
        print(url)
        result = requests.get(url, stream=True)
        if result.status_code == 200:
            image = result.raw.read()
            open(filename + ".jpg","wb").write(image)
