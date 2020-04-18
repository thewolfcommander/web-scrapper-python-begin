import requests
import bs4


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

    def select_title(self):
        """
        Select the Title of the page
        """
        raw = self.opener()
        data = raw.find('title')
        return data.text
    
    def select_data(self):
        """
        Select the Target Data which user wants to scrap
        *************************************************************
        WARNING: Configured to scrap all links
        *************************************************************
        """
        raw = self.opener()
        data = raw.find_all('a', href=True)
        return data

    def assign_data(self):
        """
        Assign the Data in separate list
        """
        data = self.select_data()
        link_data = list()
        for i in data:
            flow = i['href']
            if flow.startswith('https://') or flow.startswith('http://'):
                link_data.append(flow)
            elif flow.startswith('/wiki/File:'):
                new_flow = "https://en.wikipedia.org" + str(flow)
                link_data.append(new_flow)
            elif flow.startswith('//'):
                new_flow = "https:" + str(flow)
                link_data.append(new_flow)
            elif flow.startswith('/') or flow.startswith('#'):
                new_flow = "https://en.wikipedia.org/wiki/Black_hole" + str(flow)
                link_data.append(new_flow)
        return link_data

    def write_data(self):
        """
        Write Data to the file
        *************************************************************
        WARNING: Configured to scrap all links
        *************************************************************
        """
        data = self.select_data()
        f = open(self.file, "a+")
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
                new_flow = self.url + str(flow)
                f.write(new_flow + "\n")
            else:
                new_flow = self.url + str(flow)
                f.write(new_flow + "\n")
        f.close()
        return "Scrapping Done. Please check the file."

    
# url = "https://en.wikipedia.org/wiki/Computer"
# file_path = "link_scrapper/computer.txt"
# obj = RightbrosDataScrapper(url, file_path)

# """
# Need to call only one method of the class write_data()
# """
# print(obj.assign_data())