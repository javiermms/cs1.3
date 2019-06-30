class Set(object):

	def __init__(self, elements=None):
		"""Initialize set with the given data."""
		self.elements = []
		self.size = 0

		if elements is not None:
			for item in elements:
				self.add(item)

	def __repr__(self):
		"""Return a string representation of this node."""
		return 'Set: {!r} Size: {!r}'.format(self.elements, self.size)

	def contains(self, element):
		"""Returns a boolean depending on if element is in the set"""
		return element in self.elements


	def add(self, element):
		"""Inserts element into set"""
		if not self.contains(element):
			self.elements.append(element)
			self.size += 1

	def remove(self, element):
		"""Deletes element from set"""
		if not self.contains(element):
			raise KeyError('Element {} not in set'.format(element))

		index = self.elements.index(element)
		self.elements.pop(index)
		self.size -= 1

	def union(self, other_set):
		"""Returns a new set of two sets added together"""
		new_set = Set()

		for element in other_set.elements:
			new_set.add(element)
		
		for element in self.elements:
			new_set.add(element)

		return new_set

	def intersection(self, other_set):
		"""---"""
		# TODO: return a new set that is the intersection of this set and other_set
		pass

	def difference(self, other_set):
		"""---"""
		# TODO: return a new set that is the difference of this set and other_set
		pass

	def is_subset(self, other_set):
		"""---"""
		# TODO: return a boolean indicating whether other_set is a subset of this set
		pass

def test_set():
	s = Set([1, 5, 9, 7, 3])
	r = Set([20, 30, 15, 7, 3])
	# print(s)  #set size
	# s.add(10)
	# s.add('cheese')
	# s.add(False)
	# print(s) 
	# s.remove(9)
	# s.remove('cheese')
	# s.remove(False) 
	print(s)
	print(r)
	print(s.union(r))
	
if __name__ == '__main__':
	test_set()
		