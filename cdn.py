#!/usr/bin/env python2
import networkx as nx
import numpy as np
from operator import itemgetter

def generate_seeds(num_players, num_seeds, G,w,x,y,z):
	DEGREE_WEIGHT = w
	CENTRALITY_WEIGHT = x
	NEIGHBOR_WEIGHT = y
	NEIGHBOR_WEIGHT2 = z
	# Initialize see array to zeros
	seeds = np.zeros(num_seeds, dtype=np.int)
	neighbors = nx.to_dict_of_lists(G).values()
	m = nx.closeness_centrality(G)
	
	centralities = m.values()
	sum_degrees = np.zeros(len(neighbors), dtype=np.int) 
	sum_centralities = np.zeros(len(neighbors), dtype=np.float32)  
	degrees = np.zeros(len(neighbors), dtype=np.int)  # tuple of (node_id, degree)
	for i in range(len(neighbors)):
		degrees[i] = len(neighbors[i])
	# Assign sum of degrees to each node in the graph (over all neighbors)
	for i in range(len(neighbors)):
		sum = 0
		this_nodes_neighbors = neighbors[i]
		for j in range(len(neighbors[i])):
			sum = sum + degrees[this_nodes_neighbors[j]]
		sum_degrees[i] = sum

	# Assign sum of centralities to each node in the graph (over all neighbors)
	for i in range(len(neighbors)):
		sum = 0.0
		this_nodes_neighbors = neighbors[i]
		for j in range(len(neighbors[i])):
			sum = sum + centralities[this_nodes_neighbors[j]]
		sum_centralities[i] = sum
		
	scores = [(None, None)] * len(neighbors)
	
	degree_max = max(degrees)
	cent_max = max(centralities)
	neighbors_max = max(sum_degrees)
	neighbors_max2 = max(sum_centralities)
	
	for i in range(len(neighbors)):
		norm_degree = float(degrees[i]) / degree_max
		norm_cent = float(centralities[i]) / cent_max
		norm_neighbors = float(sum_degrees[i]) / neighbors_max
		norm_neighbors2 = float(sum_centralities[i]) / neighbors_max2
		
		scores[i] = (i, norm_degree * DEGREE_WEIGHT + norm_cent * CENTRALITY_WEIGHT + norm_neighbors * NEIGHBOR_WEIGHT + norm_neighbors2 * NEIGHBOR_WEIGHT2)

	sorted_scores = sorted(scores, key=itemgetter(1), reverse=True)
	for j in range(50):
		for i in range(num_seeds):
			seeds[i] = sorted_scores[i][0]
			
	return seeds

