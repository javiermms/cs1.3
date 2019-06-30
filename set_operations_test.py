from set_operations import Set
import unittest

# add test cases with chars/string and mixed (nums and strings)

class SetTest(unittest.TestCase):
	def test_init(self):
		s = Set()
		assert s.elements == []
		assert s.size == 0

	def test_init_with_set(self):
		s = Set([1, 5, 9, 7])
		assert s.elements == [1, 5, 9, 7]
		assert s.size == 4

	def test_init_with_set_two(self):
		r = Set([1, 5, 7, 3, 9])
		assert r.elements == [1, 5, 7, 3, 9] 
		assert r.size == 5

	def test_contains(self):
		s = Set([1, 5, 9, 7])
		r = Set([1, 5, 7, 3, 9])

		# True Cases
		assert s.contains(1) == True
		assert s.contains(5) == True
		assert s.contains(9) == True
		assert s.contains(7) == True

		assert r.contains(1) == True
		assert r.contains(5) == True
		assert r.contains(7) == True
		assert r.contains(3) == True
		assert r.contains(9) == True

		# False Cases
		assert s.contains(8) == False
		assert s.contains(3) == False
		assert s.contains(-10) == False
		assert s.contains(17) == False

		assert r.contains(0) == False
		assert r.contains(-1) == False
		assert r.contains(2) == False
		assert r.contains(-20) == False
		assert r.contains(4) == False

	def test_add(self):
		s = Set([])
		r = Set([1, 5, 7, 3, 9])

		s.add(1) 
		assert s.contains(1)
		s.add(6)
		assert s.contains(6)
		s.add(9)
		assert s.contains(9)
		s.add(9)
		assert s.contains(9)

		r.add(12)
		assert r.contains(12)
		r.add(2)
		assert r.contains(2)
		r.add(16)
		assert r.contains(16)
		r.add(-2)
		assert r.contains(-2)

	def test_remove(self):
		s = Set([1, 6, 9])
		r = Set([1, 5, 7, 3, 9, 12, 2, 16, -2])

		s.remove(1)
		assert s.contains(1) == False
		s.remove(6)
		assert s.contains(6) == False
		s.remove(9)
		assert s.contains(9) == False

		with self.assertRaises(KeyError):
			s.remove(9)

		r.remove(12)
		assert r.contains(12) == False
		r.remove(2)
		assert r.contains(2) == False
		r.remove(16)
		assert r.contains(16) == False
		r.remove(-2)
		assert r.contains(-2) == False

	def test_union(self):
		s = Set([1, 6, 9])
		r = Set([1, 5, 7, 3, 9, 12, 2, 16, -2])

		result = s.union(r)

		assert 1 in result.elements
		assert 6 in result.elements
		assert 9 in result.elements
		assert 5 in result.elements
		assert 7 in result.elements
		assert 3 in result.elements
		assert 12 in result.elements
		assert 2 in result.elements
		assert 16 in result.elements
		assert -2 in result.elements
		assert result.size == 10 #check size is right
		

	def test_intersection(self):
		s = Set([1, 6, 9])
		r = Set([1, 5, 7, 3, 9, 12, 2, 16, -2])

		result = s.intersection(r)

		assert 1 in result.elements
		assert 9 in result.elements
		assert result.size == 2 # check size is right

	def test_difference(self):
		s = Set([1, 6, 9])
		r = Set([1, 5, 7, 3, 9, 12, 2, 16, -2])

		result = s.difference(r)

		assert 6 in result.elements
		assert 5 in result.elements
		assert 7 in result.elements
		assert 3 in result.elements
		assert 12 in result.elements
		assert 2 in result.elements
		assert 16 in result.elements
		assert -2 in result.elements
		assert result.size == 8 #checks to see if size is right

	def test_is_subset(self):
		s = Set([1, 6, 9])
		r = Set([1, 5, 7, 3, 9, 12, 2, 16, -2])

		assert s.is_subset(r) is False
		assert r.is_subset(s) is False

		r = Set([1, 6, 9, 3, 9, 12, 2, 16, -2])

		assert r.is_subset(s) is True


if __name__ == '__main__':
	unittest.main()