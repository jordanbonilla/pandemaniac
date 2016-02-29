import json
import networkx as nx
import sys
import copy

import sim
import multiprocessing

NUM_ROUNDS = 1 # Given in the homework set

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


jsonfiles = ['13','14','22','23','24','30','31','32','33','34']

def test_params(n):
	w = (n % (20 ** 4)) / (20 ** 3)
	x = (n % (20 ** 3)) / (20 ** 2)
	y = (n % (20 ** 2)) / (20 ** 1)
	z = (n % (20 ** 1)) / (20 ** 0)
	successes = 0
	answers = []
	for g in range(len(jsonfiles)):
		nodes = {}
		(num_players, num_seeds, data, G) = scanfile('2.10.' + jsonfiles[g] + '.json')
		seeds =  __import__('cdn').generate_seeds(num_players, num_seeds, G,w,x,y,z)
		seeds = map(str, list(seeds))[:num_seeds]
		nodes['cdn'] = seeds
		seeds =  __import__('degree').generate_seeds(num_players, num_seeds, G)
		seeds = map(str, list(seeds))[:num_seeds]
		nodes['degree'] = seeds
		answers.append(sim.run(data,nodes))
		if(answers[len(answers) - 1]['cdn'] > answers[len(answers) - 1]['degree']):
			successes = successes + 1
		
	if(successes > len(jsonfiles) - 2):
		print 'successes:', successes, 'params:',w,x,y,z
		for h in range(len(jsonfiles)):
			print answers[h]

if __name__ == "__main__":
	# Parse the JSON file into a graph.
    pool = multiprocessing.Pool(processes=16)
    pool.map(test_params, range(20 ** 4))
    pool.close()
    pool.join()   
    print('done')





