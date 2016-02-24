#!/usr/bin/env python2
import networkx as nx
import numpy as np
from operator import itemgetter

def generate_seeds(num_players, num_seeds, G):
	# Initialize seed array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)

	neighbors = nx.to_dict_of_lists(G).values()

	degrees = np.zeros(len(neighbors), dtype=np.int)
	sum_degrees = [(None, None)] * len(neighbors)  # tuple of (node_id, degree)
	# Assign degrees to each node in the graph
	for i in range(len(neighbors)):
		degrees[i] = len(neighbors[i])
	# Assign sum of degrees to each node in the graph (over all neighbors)
	for i in range(len(neighbors)):
		sum = 0
		this_nodes_neighbors = neighbors[i]
		for j in range(len(neighbors[i])):
			sum = sum + degrees[this_nodes_neighbors[j]]
		sum_degrees[i] = ( i, sum )
	sorted_degrees = sorted(sum_degrees, key=itemgetter(1), reverse=True)
	for i in range(num_seeds):
		seeds[i] = sorted_degrees[i][0]

	return seeds

