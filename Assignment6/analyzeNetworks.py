import nltk
import pandas as pd
import numpy as np
import sys
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

"""works"""
def readEdgeList(filename):
	EdgeList = pd.read_csv(filename)
	if len(EdgeList.columns) == 2:
		return EdgeList
	else:
		print "Edge List should only have 2 columns"
		return EdgeList[['in','out']]
readEdgeList("testing.csv")

def degree(edgeList, in_or_out):
	if in_or_out=="in":
		x=edgeList['in'].value_counts()
		return x
	if in_or_out=="out":
		y=edgeList['out'].value_counts()
		return y


def combineEdgelists(edgeList1, edgeList2):
	mergedlist = pd.concat([edgeList1,edgeList2])
	deduped_merged=mergedlist.drop_duplicates()
	return deduped_merged


def pandasToNetworkX(edgeList):
	g = nx.DiGraph()
	for column0, column1 in edgeList.to_records(index=False):
		g.add_edge(column0, column1)
		#nx.draw(g)
	#plt.show()
	return g

def randomCentralNode(inputDiGraph):
	probability=[]
	keys=[]
	node_centralities=nx.eigenvector_centrality(inputDiGraph)
	sum_probabilities=sum(node_centralities.values())
	for key, value in node_centralities.items():
		new_probability=value/sum_probabilities
		keys.append(key)
		probability.append(new_probability)
	x=np.random.choice(keys, p=probability)
	return x

y=readEdgeList("name.csv")
x=pandasToNetworkX(y)
randomCentralNode(x)
