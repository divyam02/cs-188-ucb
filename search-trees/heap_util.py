import heapq

class heap(object):
	def __init__(self, raw_input=None, key=lambda x:x):
		self.key = key
		if raw_input:
			self._data = [(key(item), item) for item in raw_input]
			heapq.heapify(self._data)
		else:
			self._data=[]

	def push(self, item):
		heapq.heappush(self._data, (self.key(item), item))

	def pop(self):
		return heapq.heappop(self._data)[1]