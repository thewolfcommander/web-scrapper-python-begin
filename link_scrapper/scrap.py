import requests
import bs4


# # Selecting the type of data we want
# f = open("link_scrapper/data.txt", "w+")
# for i in soup.find_all('a', href=True):
#     flow = i['href']
#     if flow.startswith('https://') or flow.startswith('http://'):
#         f.write(flow + "\n")
#     elif flow.startswith('/wiki/File:'):
#         new_flow = "https://en.wikipedia.org" + str(flow)
#         f.write(new_flow + "\n")
#     elif flow.startswith('//'):
#         new_flow = "https:" + str(flow)
#         f.write(new_flow + "\n")
#     elif flow.startswith('/') or flow.startswith('#'):
#         new_flow = "https://en.wikipedia.org/wiki/Black_hole" + str(flow)
#         f.write(new_flow + "\n")
#     else:
#         new_flow = "https://en.wikipedia.org/wiki/Black_hole/" + str(flow)
#         f.write(new_flow + "\n")
# f.close()


class RightbrosDataScrapper:
    """
    Simple Data Scrapper from a url
    """
    def __init__(self, url, file):
        """
        Initialize the scrapper
        """
        self.url = url
        self.file = file
        self.name = 'The Rightbros Scrapper'

    def opener(self):
        """
        Opens the request to the url, convert the requests object to bs4 Object
        """
        # Requesting the Url to get the data
        req = requests.get(self.url)
        # Converting the requests object to bs4 object to do the operations
        soup = bs4.BeautifulSoup(req.text, 'lxml')
        return soup

    def getSelector(self):
        """
        Take input from the User, which selector of data he/she wants to scrap
        """
        selector = str(input('Enter a selector ... '))
        self.selector = selector
    
    def select_data(self):
        """
        Select the Target Data which user wants to scrap
        """
        raw = self.opener()
        data = raw.find_all(self.selector)
        return data

    def write_data(self):
        """
        Write Data to the file
        *************************************************************
        WARNING: Configured to scrap all links
        *************************************************************
        """
        data = select_data()
        f = open(self.file, "w+")
        for i in data:
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
        return "Scrapping Done. Please check the file."

    
url = "https://en.wikipedia.org/wiki/Black_hole"
file_path = "link_scrapper/wiki.txt"
obj = RightbrosDataScrapper(url, file_path)