import sys
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re


def fetchArtistId(name):
    url="https://api.spotify.com/v1/search?q=" + name + "&type=artist"
    req = requests.get(url)
    json_data = req.json()
    my_json=json_data
    id_data=my_json['artists']['items'][0]['id']
    return id_data

"""Using the Spotify API search method, take a string that is the artist's name,
and return a Spotify artist ID."""


def fetchArtistInfo(artist_id):
    artist_dict={}
    url="https://api.spotify.com/v1/artists/"+artist_id
    req = requests.get(url)
    json_data = req.json()
    my_json=json_data
    genres1=my_json['genres']
    followers1=my_json['followers']
    id1=my_json['id']
    name1=my_json['name']
    popularity1=my_json['popularity']
    dict_value=(followers1, genres1, id1, name1, popularity1)
    dict_key=("followers", "genres", "id", "name", "popularity")
    z=zip(dict_key,dict_value)
    artist_dict=dict(z)
    return(artist_dict)


"""Using the Spotify API, takes a string representing the id and
returns a dictionary including the keys 'followers', 'genres', 
'id', 'name', and 'popularity'.
"""


