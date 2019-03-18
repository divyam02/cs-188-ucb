# A graph utility
from collections import defaultdict

class Node():
	def __init__(self, node, h=0):
		self._node = node
		self._h = h
		self._g = 0

	def get_f(self):
		return self._h + self._g

class Graph():
	def __init__(self, nodes, edges, directed=False, weighted=False):
		self._graph = defaultdict(set)
		self._directed = directed
		self._weighted = weighted
		for node in nodes:
			self._nodes[i] = Node(node, j)
		try:
			for i, j in edges:
				self.add_edge(i, j)
		# If weighted...
		except:
			for i, j, k in edges:
				self.add_edge(i, j, k)

	def add_edge(self, i, j, k=1, h=1):
		self._graph[i].add((j, k))
		if not self._directed:
			self.graph[j].add((i, k))
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

	def give_h(self, node, h):
		self._nodes[node] = h

	def __str__(self):
		return '{}({})'.format(self.__class__.__name__, dict(self._graph))