#!python

def contains(text, pattern):
	"""Return a boolean indicating whether pattern occurs in text."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	
	length = len(pattern)
	index = 0

	while index < len(text) + 1 - length:
		if text[index: index + (length)] == pattern:
			return True
		index += 1
 
	return False

def find_index(text, pattern):
	"""Return the starting index of the first occurrence of pattern in text,
	or None if not found."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	
	text_index = 0

	if pattern == '':
		return text_index

	while text_index != len(text):
		for num in range(len(pattern)):
			if text_index + num < len(text):
				if text[text_index + num] != pattern[num]:
					break
				if num == len(pattern) - 1:
					return text_index
		text_index += 1

def find_all_indexes(text, pattern):
	"""Return a list of starting indexes of all occurrences of pattern in text,
	or an empty list if not found."""
	assert isinstance(text, str), 'text is not a string: {}'.format(text)
	assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
	
	indexes = []

	if pattern == "":
		num = 0
		for num in range(0, len(text)):
			indexes.append(num)
		return indexes

	for index, letter in enumerate(text):
		if pattern == "":
			return indexes
		if letter == pattern[0]:
			if text[index: index + len(pattern)] == pattern:
				indexes.append(index)
			else: continue

	return indexes


	
def test_string_algorithms(text, pattern):
	found = contains(text, pattern)
	print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
	# TODO: Uncomment these lines after you implement find_index
	index = find_index(text, pattern)
	print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
	# TODO: Uncomment these lines after you implement find_all_indexes
	indexes = find_all_indexes(text, pattern)
	print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
	"""Read command-line arguments and test string searching algorithms."""
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 2:
		text = args[0]
		pattern = args[1]
		test_string_algorithms(text, pattern)
	else:
		script = sys.argv[0]
		print('Usage: {} text pattern'.format(script))
		print('Searches for occurrences of pattern in text')
		print("\nExample: {} 'abra cadabra' 'abra'".format(script))
		print("contains('abra cadabra', 'abra') => True")
		print("find_index('abra cadabra', 'abra') => 0")
		print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
	# main()
	# print(contains('abc', 'abz')) 
	# print(find_index('abc', 'abc'))
	 print(find_all_indexes('abc', 'abz'))