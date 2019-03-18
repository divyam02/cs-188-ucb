import heapq
import math

class uniform_cost_search():
	def __init__(self, graph, start, goals):
		self._graph = graph
		self._start = start
		self._goals = goals

	def heuristic_distance(self, node, goals):
		"""
		Single goal only, add heuristic!
		"""
		self._graph[node]._h = 0

	def find_optimal_path(self):
		min_dist = math.inf
		heap = heapq()
		nodes = self._nodes.keys()
		heap.heapify(nodes)
		
