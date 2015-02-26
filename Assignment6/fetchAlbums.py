import requests
from datetime import datetime
import sys
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re

def fetchAlbumIds(artist_id):
	id_data=[]
	url="https://api.spotify.com/v1/artists/" + artist_id + "/albums?album_type=album&market=US"
	req = requests.get(url)
	json_data = req.json()
	my_json=json_data
	n=len(my_json['items'])
	for i in range(0,n):
		a=my_json['items'][i]['id']
		id_data.append(a)
	print "length of id data is", len(id_data)
	return(id_data)
   
print fetchAlbumIds("6CWTBjOJK75cTE8Xv8u1kj")

def fetchAlbumInfo(album_id):
	"""Using the Spotify API, take an album ID 
	and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
	"""
	album_dict={}
	url="https://api.spotify.com/v1/albums/" + album_id
	req = requests.get(url)
	json_data = req.json()
	my_json=json_data['artists']
	artist_id=json_data['artists'][0]['id']
	name=json_data['name']
	year_prelim=json_data['release_date']
	year=year_prelim[0:4]
	popularity=json_data['popularity']
	dict_value=(artist_id, album_id, name, year, popularity)
	dict_key=("artist_id", "album_id", "name", "year", "popularity")
	z=zip(dict_key,dict_value)
	album_dict=dict(z)
	return album_dict

print fetchAlbumInfo("4LU705gOOt3DHS4kFvdQJz")

