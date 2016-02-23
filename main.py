import json
import networkx as nx
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
	G = nx.Graph();
	if(len(sys.argv) != 2):
		print "please specify graph json file"
		sys.exit(-1);
	with open(sys.argv[1]) as json_file:
		data = json.load(json_file)
		for i in range(len(data)):
			G.add_node(i)
			for j in range(len(data[str(i)])):
				G.add_edge(i, int(data[str(i)][j]));
				#print data[str(i)][j]
			#print "\n"
			
	print "Average clustering coefficient:", nx.average_clustering(G);
	print "Overall clustering coefficient:", nx.transitivity(G) ;
	print "Maximal diameter:", nx.diameter(G) ;
	print "Average diameter:", nx.average_shortest_path_length(G) ;

	raw = data.values();
	data = [len(x) for x in raw]
	
	data_sorted = np.sort(data)
	p = 1. * np.arange(len(data)) / (len(data) - 1)
	fig = plt.figure()
	ax1 = fig.add_subplot(121)
	ax1.plot(data_sorted, 1 - p)
	ax1.set_ylabel('$p$')
	ax1.set_xlabel('$x$')
	ax2 = fig.add_subplot(122)	
	pl.hist(data)
	pl.show()
	



	