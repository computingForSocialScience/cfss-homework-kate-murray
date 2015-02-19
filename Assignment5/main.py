import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
	artist_names = sys.argv[1:]
	print "input artists are ", artist_names
	infos=[]
	ids=[]
	album_infos=[]
	for current_name in artist_names:
		print "current name is", current_name
		current_id=fetchArtistId(current_name)
		print "current id is", current_id
		current_info=fetchArtistInfo(current_id)
		infos.append(current_info)
		ids.append(current_id)
	for new_id in ids:
		album_ids=fetchAlbumIds(new_id)
		for album_id in album_ids:
			album_info=fetchAlbumInfo(album_id)
			album_infos.append(album_info)
	writeArtistsTable(infos)
	print "album_info is ", album_info
	writeAlbumsTable(album_infos)


	
    

