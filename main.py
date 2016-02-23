import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import itemgetter
NUM_ROUNDS = 50 # Given in the homework set

if __name__ == "__main__":
	G = nx.Graph();
	if(len(sys.argv) != 2):
		print "python main.py [json file]"
		sys.exit(-1);
	filename = sys.argv[1];
	# "Graphs are named in the following (semantic) way: 
	# num_players.num_seeds.unique_id "
	game_specifications = filename.split(".")
	num_players = int(game_specifications[0]);
	num_seeds = int(game_specifications[1]);
	unique_id = int(game_specifications[2]);
	# Initialize seed array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)

	# Print info about this game
	print "num players:", num_players
	print "num seeds:", num_seeds
	print "unqiue id:", unique_id

	# Read json file and populate networkx graph struct
	with open(filename) as json_file:
		data = json.load(json_file)
		for i in range(len(data)):
			G.add_node(i)
			for j in range(len(data[str(i)])):
				G.add_edge(i, int(data[str(i)][j]));

	# Print some fun facts
	print "Average clustering coefficient:", nx.average_clustering(G);
	print "Overall clustering coefficient:", nx.transitivity(G) ;

	# Get the top "num_seeds" nodes in terms of degree to use for seeds
	neighbors = data.values();
	degrees = [(None, None)] * len(neighbors); # tuple of (node_id, degree)
	for i in range(len(neighbors)):
		degrees[i] = ( i, len(neighbors[i]) ) 
	sorted_degrees = sorted(degrees, key=itemgetter(1))
	for i in range(num_seeds):
		seeds[i] = sorted_degrees[i][0]

	# Write our selected seeds to file:
	outfilename = "out.txt"
	outfile = open(outfilename, 'w')
	# Re-use the same seeds for every round
	for j in range(NUM_ROUNDS):
		for i in range(num_seeds):
			outfile.write(str(seeds[i]) + '\n')
	outfile.close()



	