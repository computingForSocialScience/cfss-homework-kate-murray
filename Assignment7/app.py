from flask import Flask, render_template, request, redirect, url_for
import pymysql
import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from artistNetworks import getRelatedArtists, getDepthEdges, getEdgeList, writeEdgeList
from analyzeNetworks import readEdgeList, degree, combineEdgelists, pandasToNetworkX, randomCentralNode
from random import randint
import requests
from io import open

dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
app = Flask(__name__)

def createNewPlaylist(artist_name):
	cur = db.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS songs(
 	playlistId INTEGER PRIMARY KEY
 	AUTO_INCREMENT,
 	songOrder VARCHAR(255),
 	artistName VARCHAR(255),
 	albumName VARCHAR(255),
 	trackName VARCHAR(255));''')
	cur.execute('''CREATE TABLE IF NOT EXISTS playlists(
 	id INTEGER PRIMARY KEY
 	AUTO_INCREMENT,
 	rootArtist VARCHAR(255));''')
	a=artist_name
	ID=fetchArtistId(a)
	combined_Edge_List=getEdgeList(ID, 2)
	b=combined_Edge_List
	c=pandasToNetworkX(b)
	nodes=[]
	albums=[]
	tracks=[]
	tracks_names=[]
	#for i in range(30):
	#	d=randomCentralNode(c)
	#	nodes.append(d)
	while len(albums)<30:
		#e=nodes[i]
		e=randomCentralNode(c)
		f=fetchAlbumIds(e)
		if len(f)==0:
			continue
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
	for i in range(30):
		x=fetchAlbumInfo(albums[i])
		ALBUM_NAME=x['name']
		print(x['artist_id'])
		y=fetchArtistInfo(x['artist_id'])
		ARTIST_NAME=y['name']
		TRACK_NAME=tracks_names[i]
		x=i+1
		cur.execute('''
 		INSERT INTO songs
 		(songOrder, artistName, albumName, trackName)
 		VALUES
 		(%s, %s, %s, %s )''',(x,ARTIST_NAME,ALBUM_NAME,TRACK_NAME))
 	cur.execute('''
 	INSERT INTO playlists
 	(rootArtist)
 	VALUES
 	(%s)''',(artist_name))
 	db.commit()
createNewPlaylist("Feist")
@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        # YOUR CODE HERE
        return(redirect("/playlists/"))



if __name__ == '__main__':
	app.debug=True
	app.run()