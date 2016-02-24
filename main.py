import json
import networkx as nx
import sys
import copy

import sim

NUM_ROUNDS = 50 # Given in the homework set

def scanfile(filename):
	G = nx.Graph()

	# "Graphs are named in the following (semantic) way:
	# num_players.num_seeds.unique_id "
	game_specifications = filename.split(".")
	num_players = int(game_specifications[0]);
	num_seeds = int(game_specifications[1]);

	# Read json file and populate networkx graph struct
	with open(filename) as json_file:
		data = json.load(json_file)
		for i in range(len(data)):
			G.add_node(i)
			for j in range(len(data[str(i)])):
				G.add_edge(i, int(data[str(i)][j]))

	return (num_players, num_seeds, data, G)

def writeseeds(seeds):
	# Re-use the same seeds for every round
	for j in range(NUM_ROUNDS):
		for i in range(num_seeds):
			print seeds[i]


if __name__ == "__main__":
	if(len(sys.argv) != 4):
		print "python main.py <json_file> <strat1> <strat2>"
		sys.exit(-1);

	# Parse the JSON file into a graph.
	(num_players, num_seeds, data, G) = scanfile(sys.argv[1])

	# Generate the seeds based on graph data.
	seeds1 = __import__(sys.argv[2]).generate_seeds(num_players, num_seeds, G)
        seeds1 = map(str, list(seeds1))
        seeds2 = __import__(sys.argv[3]).generate_seeds(num_players, num_seeds, G)
        seeds2 = map(str, list(seeds2))

        nodes = {sys.argv[2]: seeds1[:num_seeds], sys.argv[3]: seeds2[:num_seeds]}
        print sim.run(data, nodes)

