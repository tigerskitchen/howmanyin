#!/usr/bin/python3
#This scraper is specific to IMDB's URLs
#Typical usage:
#python howmanyin.py url namevariation1 namevariation2 etc...

from bs4 import BeautifulSoup
import requests
import re


def search_movie_for_names(url, names):
    """
    Search a movie on IMDB to see how many people in the credits match a given name.

    :param credits_url: The URL for the movie you want to search
    :param names: A list of the names you want to search for in the movie's credits
    """

    # Get the unique numeric code for the IMDB movie
    movie_id = re.sub('\D', '', url)
    # Make sure we point to the credits page
    credits_url = 'http://www.imdb.com/title/tt' + movie_id[:7] + '/fullcredits'
    # Make sure the names are correctly capitalized
    for i in range(len(names)):
        names[i] = names[i].lower().capitalize()

    r = requests.get(credits_url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all('a')

    movie_title = soup.find('a', class_='subnav_heading').string

    # TODO: filter this specifically to the div with id "fullcredits_content"
    all_names = [i.string.strip() for i in links if i.string != None]

    filtered_names = []
    for name in all_names:
        for name_to_match in names:
            if name.startswith(name_to_match):
                if name not in filtered_names:
                    filtered_names.append(name)

    return movie_title, filtered_names

# Run the code
movie_url = 'http://www.imdb.com/title/tt0441773/fullcredits'
names_to_search = ['Matt', 'Matthew', 'Matti', 'Matty', 'Mat', 'Mathew']
movie_title, filtered_names = search_movie_for_names(movie_url, names_to_search)
print(str(movie_title) + " has " + str(len(filtered_names)) + "!!!")
print(filtered_names)