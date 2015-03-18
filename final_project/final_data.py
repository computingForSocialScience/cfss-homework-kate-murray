import MySQLdb
from io import open
import unicodecsv
import datetime
import sys
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import nltk
import pandas as pd
import numpy as np
import pymysql
from flask import Flask, render_template, request, redirect, url_for

tablecodes=["B06012","B01001", "B17001", "B19052", "B19057"]

column_names=[]
dbname="final_data"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
app = Flask(__name__)

FIPSdict={ "Connecticut": 10, "Montana": 30,"Connecticut": 15, "Montana": 1}
area_ids=[]
final_column_data=[]
def gettabledata():
	cur = db.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS new_data_info(
	row_id VARCHAR(255),
	row_name VARCHAR(255),
	tableId VARCHAR(255),
	table_name VARCHAR(255),
	table_denominator VARCHAR(255));''')
	cur.execute('''CREATE TABLE IF NOT EXISTS new_data(
	tableId VARCHAR(255),
	FIPSCode VARCHAR(255),
	geographyId VARCHAR(255),
	row_id VARCHAR(255),
	row_name VARCHAR(255),
	estimate INTEGER);''')
	print "success one"
	for tablecode in tablecodes:
		print "success two"
		db.commit()
		cur = db.cursor()
		for key,value in FIPSdict.items():
			FIPSvalue=value
			apiUrl="http://api.censusreporter.org/1.0/data/show/latest?table_ids="+tablecode+"&geo_ids=140|04000US"+str(FIPSvalue)
			print "api url is",apiUrl
			if apiUrl=="http://api.censusreporter.org/1.0/data/show/latest?table_ids=B06012&geo_ids=140|04000US9":
				print "skipped"
			elif apiUrl=="http://api.censusreporter.org/1.0/data/show/latest?table_ids=B06012&geo_ids=140|04000US6":
				print "skipped"
			else:
				area_ids=[]
				column_ids=[]
				req = requests.get(apiUrl)
				json_data = req.json()
				my_json=json_data
				x=my_json['tables'][tablecode]['columns']
				k=my_json['tables'][tablecode]['title']
				j=my_json['tables'][tablecode]['denominator_column_id']
				for key in x:
					column_ids.append(key)
				for column_id in column_ids:
					column_name=my_json['tables'][tablecode]['columns'][column_id]['name']
					data=my_json['data']
					for key in data:
						area_ids.append(key)
					for area_id in area_ids:
						string_area=str(area_id)
						y=data[string_area][tablecode]['estimate'][column_id]
						cur.execute('''
						INSERT INTO new_data
						(tableId,FIPSCode,geographyId,row_id,row_name,estimate)
						VALUES
						(%s, %s, %s, %s, %s, %s)''',(tablecode,FIPSvalue,area_id,column_id,column_name,y))
				cur.execute('''
				INSERT INTO new_data_info
				(row_id, row_name, tableId, table_name,table_denominator)
				VALUES
				(%s, %s, %s, %s, %s)''',(column_id,column_name,tablecode,k,j))

	db.commit()	
#index page
@app.route('/',methods=['GET','POST'])
def make_index_resp():
	# this function just renders templates/index.html when
	# someone goes to http://127.0.0.1:5000/
	return(render_template('indexpage.html'))
@app.route('/compareColumns')
def show_histogram():
	import numpy as np
	from bokeh.plotting import figure
	from bokeh.resources import CDN
	from bokeh.embed import components
	a=request.args.get("state")
	b=request.args.get("column1")
	c=request.args.get("column2")
	from bokeh.plotting import figure, output_file, show
	# get some data to use
	cur = db.cursor()
	cur.execute('''
 	SELECT estimate from new_data where FIPSCode=%s and row_id=%s''',(a,b))
 	d = cur.fetchall()
 	cur.execute('''
 	SELECT estimate from new_data where FIPSCode=%s and row_id=%s''',(a,c))
 	e=cur.fetchall()
# plotting
	p = figure(title="Comparison")
	p.scatter(d,e)
	show(p)
	figJS,figDiv = components(p,CDN)
	rendered = render_template(
 	'histogram.html',
 	d=d,e=e,figJS=figJS,figDiv=figDiv)
	return(rendered)
if __name__ == '__main__':
	app.debug=True
	app.run()

