import csv
import sys

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)

def get_avg_latlng(arg0):
	permits = readCSV(arg0)
	counterlat = 0
	counterlon = 0
	counterdemoninator=0
	for row in permits:
		if row[128] == "":
			continue
		else:
			parsed = row[128]
			counterlat = counterlat + float(row[128])
			parse = row[129]
			counterlon =counterlon + float(row[129])
			counterdemoninator= counterdemoninator + 1
	lat_average= counterlat / counterdemoninator
	lon_average= counterlon / counterdemoninator
	print lat_average, lon_average
### enter your code below
get_avg_latlng("permits_hydepark.csv")

import matplotlib.pyplot as plot

def zip_code_barchart(arg0):
	master_list= []
	zipcode = readCSV(arg0)
	for row in zipcode:
		if row[28] == "":
			continue
		else:
			a1=(row[28])
			a=int(a1[0:5])
			master_list.append(a)
		if row[35] == "":
			continue
		else:
			b1=row[35]
			b=int(b1[0:5])
			master_list.append(b)
		if row[42] == "":
			continue
		else:
			c1=row[42]
			c=int(c1[0:5])
			master_list.append(c)
		if row[49] == "":
			continue
		else:
			d1=row[49]
			d=int(d1[0:5])
			master_list.append(d)
		if row[56] == "":
			continue
		else:
			e1=row[56]
			e=int(e1[0:5])
			master_list.append(e)
		if row[63] == "":
			continue
		else:
			f1=row[63]
			f=int(f1[0:5])
			master_list.append(f)
		if row[70] == "":
			continue
		else:
			g1=row[70]
			g=int(g1[0:5])
			master_list.append(g)
		if row[77] == "":
			continue
		else:
			h1=row[77]
			h=int(h1[0:5])
			master_list.append(h)
		if row[84] == "":
			continue
		else:
			i1=row[84]
			i=int(i1[0:5])
			master_list.append(i)
		if row[91] == "":
			continue
		else:
			j1=row[91]
			j=int(j1[0:5])
			master_list.append(j)
	plot.hist(master_list)
	plot.show()
zip_code_barchart("permits_hydepark.csv")