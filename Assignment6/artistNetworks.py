import pandas as pd
import numpy as np
import sys
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re


def getRelatedArtists(artistID):
	related_list=[]
	url="https://api.spotify.com/v1/artists/" + artistID + "/related-artists"
	req = requests.get(url)
	json_data = req.json()
	my_json=json_data
	n=len(my_json['artists'])
	for i in range(0,n):
		a=my_json['artists'][i]['id']
		related_list.append(a)
	return related_list

def getDepthEdges(artistID, depth):
	"""Given an artist and a level of depth, returns a list of directioned tuples
	that give the original artist id, along with the id of a related artist for
	the given levels of depth"""
	related_artists=[]
	depth_counter=0
	artists=[artistID]
	while depth_counter < depth:
		for artist in artists:
			related_artistids=getRelatedArtists(artist)
			for related_artistid in related_artistids:
				related_artists.append((artist, related_artistid))
			artists=related_artistids
		depth_counter+=1
	return related_artists

def getEdgeList(artistID, depth):
	list_values=getDepthEdges(artistID, depth)
	tuples_df = pd.DataFrame(list_values, columns=['in','out'])
	return tuples_df

def writeEdgeList(artistID, depth, filename):
	f=open(filename, 'a')
	data_for_csv=getEdgeList(artistID, depth)
	data_for_csv.to_csv(f, index=False)
	f.close()