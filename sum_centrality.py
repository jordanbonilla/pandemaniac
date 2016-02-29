#!/usr/bin/env python2
import networkx as nx
import numpy as np
from operator import itemgetter

def generate_seeds(num_players, num_seeds, G):

	# Initialize see array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)
	
	neighbors = nx.to_dict_of_lists(G).values()

	m = nx.closeness_centrality(G);
	centralities = m.values();

	# Initialize seed array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)

	sum_centralities = [(None, None)] * len(neighbors)  # tuple of (node_id, degree)

	# Assign sum of centralities to each node in the graph (over all neighbors)
	for i in range(len(neighbors)):
		sum = 0.0
		this_nodes_neighbors = neighbors[i]
		for j in range(len(neighbors[i])):
			sum = sum + centralities[this_nodes_neighbors[j]]
		sum_centralities[i] = ( i, sum )
	sorted_centralities = sorted(sum_centralities, key=itemgetter(1), reverse=True)
	for i in range(num_seeds):
		seeds[i] = sorted_centralities[i][0]

	return seeds

