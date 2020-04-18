import requests
import bs4

from scrap import RightbrosDataScrapper

def remove(obj, lst):
    """
    This function is to remove the extra links
    """
    pass


  
def worker(url, path, count):
    done = list()
    done.append(url)
    count = count + 1
    print(count)
    scrapper = RightbrosDataScrapper(url, path)
    scrapper.write_data()
    data = scrapper.assign_data()
    for i in data:
        if i not in done:
            worker(i, path, count)
        else:
            remove(i, done)

def recursive():
    start_url = 'https://en.wikipedia.org/wiki/Black_hole/'
    file_path = 'link_scrapper/computer.txt'
    scrapper = RightbrosDataScrapper(start_url, file_path)
    starter = scrapper.assign_data()
    scrapper.write_data()
    count = 0
    for i in starter:
        worker(i, file_path, count)

recursive()