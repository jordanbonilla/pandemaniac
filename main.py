import json
import networkx as nx
import matplotlib.pyplot as plt
import sys

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

	print "num players:", num_players
	print "num seeds:", num_seeds
	print "unqiue id:", unique_id

	with open(filename) as json_file:
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

	#raw = data.values();
	#data = [len(x) for x in raw]
	
	



	