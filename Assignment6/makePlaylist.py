import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from artistNetworks import getRelatedArtists, getDepthEdges, getEdgeList, writeEdgeList
from analyzeNetworks import readEdgeList, degree, combineEdgelists, pandasToNetworkX, randomCentralNode
from random import randint
import requests
from io import open
import csv

if __name__ == '__main__':
	artist_names = sys.argv[1:]
	a=artist_names[0]
	ID=fetchArtistId(a)
	combined_Edge_List=getEdgeList(ID, 2)
	if len(artist_names)>1:
		for artist_name in artist_names:
			ID=fetchArtistId(artist_name)
			edgeList1=getEdgeList(ID, 2)
			combined_Edge_List=combineEdgelists(combined_Edge_List, edgeList1)
	b=combined_Edge_List
	c=pandasToNetworkX(b)
	nodes=[]
	albums=[]
	tracks=[]
	tracks_names=[]
	for i in range(30):
		d=randomCentralNode(c)
		nodes.append(d)
	for i in range(30):
		e=nodes[i]
		f=fetchAlbumIds(e)
		i=len(f)-1
		g=randint(0,i)
		h=f[g]
		albums.append(h)
	for i in range(30):
		album_id=albums[i]
		url="https://api.spotify.com/v1/albums/" + album_id + "/tracks"
		req = requests.get(url)
		json_data = req.json()
		j=len(json_data['items'])-1
		k=json_data['items'][j]['id']
		tracks.append(k)
	for i in range(30):
		track_id=tracks[i]
		url="https://api.spotify.com/v1/tracks/" + track_id
		req = requests.get(url)
		json_data = req.json()
		names=json_data['name']
		tracks_names.append(names)
	f=open('playlist.csv', 'w')
	for i in range(30):
		x=fetchAlbumInfo(albums[i])
		ALBUM_NAME=x['name']
		y=fetchArtistInfo(x['artist_id'])
		ARTIST_NAME=y['name']
		TRACK_NAME=tracks_names[i]
		f.write(u'"%s","%s","%s"\n' % (ARTIST_NAME,ALBUM_NAME,TRACK_NAME))
	f.close()