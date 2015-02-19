from io import open
import csv

def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """
    f=open('artists.csv', 'w')
    for i in range(0,len(artist_info_list)):
        artist_dictionary=artist_info_list[i]
        for key, value in artist_dictionary.iteritems():
            ARTIST_NAME=artist_dictionary['name']
            ARTIST_ID=artist_dictionary['id']
            ARTIST_FOLLOWERS=artist_dictionary['followers']['total']
            ARTIST_POPULARITY=artist_dictionary['popularity']
        f.write(u'"%s","%s","%s","%s"\n' % (ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY))

      
#writeArtistsTable([{'genres': [u'chamber pop', u'indie christmas', u'indie pop'], 'popularity': 72, 'followers': {u'total': 248621, u'href': None}, 'id': u'6CWTBjOJK75cTE8Xv8u1kj', 'name': u'Feist'},{'genres': [u'chamber pop', u'indie christmas', u'indie pop'], 'popularity': 72, 'followers': {u'total': 248621, u'href': None}, 'id': u'6CWTBjOJK75cTE8Xv8u1kj', 'name': u'Feist'}])
def writeAlbumsTable(album_info_list):
    """Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'. """

    f=open('albums.csv', 'w')
    print "writeAlbumsTable(): type of album info", type(album_info_list)
    for i in range(0,len(album_info_list)):
        album_dictionary=album_info_list[i]
        ALBUM_ID=album_dictionary['album_id']
        ARTIST_ID=album_dictionary['artist_id']
        ALBUM_NAME=album_dictionary['name']
        ALBUM_YEAR=album_dictionary['year']
        ALBUM_POPULARITY=album_dictionary['popularity']
        f.write(u'"%s","%s","%s","%s","%s"\n' % (ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY))

#writeAlbumsTable([{'popularity': 33, 'artist_id': u'6CWTBjOJK75cTE8Xv8u1kj', 'year': u'2011', 'name': u'Metals', 'album_id': '4LU705gOOt3DHS4kFvdQJz'},{'popularity': 33, 'artist_id': u'6CWTBjOJK75cTE8Xv8u1kj', 'year': u'2011', 'name': u'Metals', 'album_id': '4LU705gOOt3DHS4kFvdQJz'}])
"""The csv file should have a header line that looks like this:
ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
"""
