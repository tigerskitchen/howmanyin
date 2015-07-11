#!/usr/bin/python3
#This scraper is specific to IMDB's URLs
#Typical usage:
#python howmanyin.py url namevariation1 namevariation2 etc...

from bs4 import BeautifulSoup
import requests
from sys import argv
import re

default_movie = 'http://www.imdb.com/title/tt0441773/fullcredits'
#Default url if none is provided

if len(argv) == 1:
    url = default_movie 
elif argv[1].startswith("http://www.imdb.com/"):
    movie_id = re.sub('\D', '', argv[1])
    url = 'http://www.imdb.com/title/tt' + movie_id[:7] + 'fullcredits'
else:
    argv.insert(1, default_movie) 
    url = default_movie


if len(argv) < 3:
    names_to_search = ('Matt', 'Matthew', 'Matti', 'Matty', 'Mat', 'Mathew')
    #Default names to search if none is provided
else:
    names_to_search = tuple([str(i.lower().capitalize()) for i in argv[2:]])
    #Add names as command line arguments to override default names to search

r = requests.get(url)
soup = BeautifulSoup(r.text)
links = soup.find_all('a')

movie_title = soup.find('a', class_='subnav_heading').string

all_names = [i.string.strip() for i in links if i.string != None]
filtered_names = [i for i in all_names if i.startswith(names_to_search)]

if __name__ == '__main__':
    print(str(movie_title) + " has " + str(len(filtered_names)) + "!!!")
    print(filtered_names)
