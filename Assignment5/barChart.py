import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')
    #open the documents that this function uses
    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)
    #use csv file reader to get row contents of files
    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = []
    #create empty list of artist names
    decades = range(1900,2020, 10)
    #range of decades each album comes out
    decade_dict = {}
    #create empty decade dictionary
    for decade in decades:
    #iterate over the decades in the dictionary
        decade_dict[decade] = 0
    #start out the decade dictionary counter at 0
    
    for artist_row in artists_rows:
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name)
    #iterate over the rows in artists.csv, test whether it's an empty row, if not, append the results
    #of the row to the list artist_names

    for album_row  in albums_rows:
        print "album row is", album_row
        if not album_row:
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break
    #iterate over the rows in albums.csv, test whether it's an empty row, if not,
    #add to the count for a specific decade
    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    return x_values, y_values, artist_names
    # the x-value for the graph is the name of each decade, the y value is the count of albums in each decade

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()
    
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names))
    plt.show()
    #Create a histogram of the above data, label the axes


    
