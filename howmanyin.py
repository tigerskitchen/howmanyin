from bs4 import BeautifulSoup
import requests
from sys import argv
import re

#This scraper is specific to IMDB's URLs
#Typical usage:
#python howmanyin.py url namevariation1 namevariation2 etc...

#Kung Fu Panda is the default url if none is provided

kung_fu = 'http://www.imdb.com/title/tt0441773/fullcredits'

if len(argv) == 1:
    url = kung_fu 
elif argv[1].startswith("http://www.imdb.com/"):
    movie_id = re.sub('\D', '', argv[1])
    url = 'http://www.imdb.com/title/tt' + movie_id[:7] + 'fullcredits'
else:
    argv.insert(1, kung_fu) 
    url = kung_fu

#Additional names can be added to the command line arguments after the the addition of a url

if len(argv) < 3:
    names_to_search = ('Matt', 'Matthew', 'Matti', 'Matty', 'Mat', 'Mathew')
else:
    names_to_search = tuple([str(i.lower().capitalize()) for i in argv[2:]])

r = requests.get(url)
soup = BeautifulSoup(r.text)
links = soup.find_all('a')

movie_title = soup.find('a', class_='subnav_heading').string

all_names = [i.string.strip() for i in links if i.string != None]
final_results = [i for i in all_names if i.startswith(names_to_search)]

if __name__ == '__main__':
    print(str(movie_title) + " has " + str(len(final_results)) + "!!!")
    print(final_results)
