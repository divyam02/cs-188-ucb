from heapq import *
from graph_build_util import *
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
		heap = self._nodes.keys()
		heapify(heap)
		explored = []
		while len(heap) > 0:
			f_cost, index = heap.heappop()			# tuple containing f-cost and node index
			for i in self._graph[index]:
				self._nodes[i]._f += f_cost
				heap.heappush((self._nodes[i].get_f(), i))

			if index in goals:
				return(self._nodes[i].get_f())
			
	def 
