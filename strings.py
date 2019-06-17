#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    text_length = len(text)
    pattern_length = len(pattern)
    count= 0
    pattern_count = 0
    repeats = 0

    for num in range(0, text_length):

        if text[num] == pattern[pattern_count]:
            count += 1
            if count == pattern_length:
                repeats += 1
                count = 0
        elif text[num] != pattern[pattern_count]:
            count = 0
            if text[num] == pattern[0]:
                count = 1
                pattern_count = 0
        
        if pattern_count <= pattern_length:
            pattern_count += 1
            if pattern_count == pattern_length:
                pattern_count = 0

    # print(count)
    # print(repeats)

    if repeats <= 0:
        return False
    else:
        return True
   
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    # for char in text:
    #     if char == pattern[0]:
    #         return text.index(char)

    for num in range(0, len(text)):
        if text[num] == pattern[0]:
            return num



def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    text_length = len(text)
    pattern_length = len(pattern)
    count= 0
    pattern_count = 0
    repeats = 0
    index_array =[]

    for num in range(0, text_length):

        if text[num] == pattern[pattern_count]:
            count += 1
            index_array.append(num)
            if count == pattern_length:
                repeats += 1
                count = 0
        elif text[num] != pattern[pattern_count]:
            count = 0
            if text[num] == pattern[0]:
                count = 1
                pattern_count = 0
        
        if pattern_count <= pattern_length:
            pattern_count += 1
            if pattern_count == pattern_length:
                pattern_count = 0
    
    if pattern_count == 0:
        return index_array
    
    return index_array

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
    # print(contains('bananas', 'nas')) 
    # print(find_index('bananas', 's'))
    print(find_all_indexes('bananas', 'p'))