import requests
import bs4

# Requesting the Url to get the data
req = requests.get('https://en.wikipedia.org/wiki/Black_hole')

# Converting the requests object to bs4 object to do the operations
soup = bs4.BeautifulSoup(req.text, 'lxml')

# Selecting the type of data we want
f = open("link_scrapper/data.txt", "w+")
for i in soup.find_all('a', href=True):
    flow = i['href']
    if flow.startswith('https://') or flow.startswith('http://'):
        f.write(flow + "\n")
    elif flow.startswith('/wiki/File:'):
        new_flow = "https://en.wikipedia.org" + str(flow)
        f.write(new_flow + "\n")
    elif flow.startswith('//'):
        new_flow = "https:" + str(flow)
        f.write(new_flow + "\n")
    elif flow.startswith('/') or flow.startswith('#'):
        new_flow = "https://en.wikipedia.org/wiki/Black_hole" + str(flow)
        f.write(new_flow + "\n")
    else:
        new_flow = "https://en.wikipedia.org/wiki/Black_hole/" + str(flow)
        f.write(new_flow + "\n")

f.close()


class RightbrosDataScrapper:
    """
    Simple Data Scrapper from a url
    """
    def __init__(self, url, file):
        self.url = url
        self.file = file
        self.name = 'The Rightbros Scrapper'

    