#!/usr/bin/env python2

import networkx as nx
import numpy as np
from operator import itemgetter
DEGREE_WEIGHT = .5
CENT_WEIGHT = 1.0 - DEGREE_WEIGHT

def generate_seeds(num_players, num_seeds, G):
	# Initialize see array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)
	neighbors = nx.to_dict_of_lists(G).values()
	m = nx.closeness_centrality(G)
	
	centralities = m.values()
	degrees = np.zeros(len(neighbors), dtype=np.int)  # tuple of (node_id, degree)
	for i in range(len(neighbors)):
		degrees[i] = len(neighbors[i])
		
	scores = [(None, None)] * len(neighbors)
	
	degree_max = max(degrees)
	cent_max = max(centralities)
	
	for i in range(len(neighbors)):
		norm_degree = float(degrees[i]) / degree_max
		norm_cent = float(centralities[i]) / cent_max
		scores[i] = (i, norm_degree * DEGREE_WEIGHT + norm_cent * CENT_WEIGHT)

	sorted_scores = sorted(scores, key=itemgetter(1), reverse=True)
	for i in range(num_seeds):
		seeds[i] = sorted_scores[i][0]

	return seeds

