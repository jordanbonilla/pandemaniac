#!/usr/bin/env python2

import networkx as nx
import numpy as np
from operator import itemgetter

def generate_seeds(num_players, num_seeds, G):
	# Initialize seed array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)

	neighbors = nx.to_dict_of_lists(G).values()

	degrees = [(None, None)] * len(neighbors)  # tuple of (node_id, degree)
	for i in range(len(neighbors)):
		degrees[i] = ( i, len(neighbors[i]) )
	sorted_degrees = sorted(degrees, key=itemgetter(1), reverse=True)
	for i in range(num_seeds):
		seeds[i] = sorted_degrees[i][0]

	return seeds
