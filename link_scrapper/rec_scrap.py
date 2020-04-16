import requests
import bs4

from scrap import RightbrosDataScrapper

  
def worker(url, path, count):
    count = count + 1
    print(count)
    scrapper = RightbrosDataScrapper(url, path)
    scrapper.write_data()
    data = scrapper.assign_data()
    for i in data:
        worker(i, path, count)

def recursive():
    start_url = 'https://en.wikipedia.org/wiki/Black_hole/'
    file_path = 'link_scrapper/computer.txt'
    done = list()
    scrapper = RightbrosDataScrapper(start_url, file_path)
    starter = scrapper.assign_data()
    scrapper.write_data()
    count = 0
    for i in starter:
        worker(i, file_path, count)

recursive()