# A graph utility
from collections import defaultdict

class Graph():
	def __init__(self, nodes, edges, directed=False, weighted=False):
		self._graph = defaultdict(set)
		self._nodes = nodes
		self._directed = directed
		for i, j in edges:
			self.add_edge(i, j)

	def add_edge(self, i, j):
		self._graph[i].add(j)
		if not self._directed:
			self.graph[j].add(i)
	"""
	def add_node(self, i):
		self._graph[i].add(set())
	"""
	def remove_edge(self, i, j):
		self._graph[i].remove(j)
		if not self._directed:
			self.graph[j].remove(i)

	def remove_node(self, i):
		for j, k in self._graph.iteritems():
			try:
				k.remove_edge(i)
			except KeyError:
				pass

		try:
			del self._graph[i]
		except KeyError:
			pass

	def __str__(self):
		return '{}({})'.format(self.__class__.__name__, dict(self._graph))