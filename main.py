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
	if(len(sys.argv) < 3):
		print "python main.py <json_file> [strategies...]"
		sys.exit(-1);

	# Parse the JSON file into a graph.
	(num_players, num_seeds, data, G) = scanfile(sys.argv[1])

	# Generate the seeds based on graph data.
        nodes = {}
        for i in range(2, len(sys.argv)):
            seeds = __import__(sys.argv[i]).generate_seeds(num_players, num_seeds, G)
            seeds = map(str, list(seeds))[:num_seeds]
            nodes[sys.argv[i]] = seeds

        print sim.run(data, nodes)

