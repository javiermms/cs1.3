import time
start = time.process_time()

def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

def sort_dictionary(all_dictionary_words):
    word_dic = dict()
    
    for word in all_dictionary_words:
        sorted_words = ''.join(sorted(word.lower()))
        word_dic[sorted_words] = word
    
    return word_dic

def sort_words(words):
    jumble_sorted = []
    for word in words:
        sorted_words = ''.join(sorted(word.lower()))
        jumble_sorted.append(sorted_words)
    
    return jumble_sorted

def get_specific_indexes(array):
    inner_arr = []
    whole_arr = []
    for element in range(len(array)):
        for index, letter in enumerate(array[element]):
            if letter == 'O':
                inner_arr.append(index)
            
        whole_arr.append(inner_arr)
        inner_arr = []
    return whole_arr

def get_word_count_and_size(array):
    new_array = []
    for element in array:
        new_array.append(len(element))
    return new_array

def unjumble_words(jumble_sorted, word_dic):
    answers = []
    for word in jumble_sorted:
        for key in word_dic.items():
            if key[0] == word:
                answers.append(key[1])
    return answers

def solve_word_jumble(words, circles, final, word_dic, jumble_sorted):
    """Solve a word jumble by unscrambling four jumbles, then a final jumble.
    Parameters:
    - words: list of strings, each is the scrambled letters for a single word
    - circles: list of strings, each marks whether the letter at that position
        in the solved anagram word will be used to solve the final jumble.
        This string contains only two different characters:
        1. O (letter "oh") = the letter is in the final jumble
        2. _ (underscore) = the letter is not in the final jumble
    - final: list of strings in the same format as circles parameter that shows
        how the final jumble's letters are arranged into a word or phrase."""
    
    # unjumbles word
    answers = unjumble_words(jumble_sorted, word_dic)

    # gets needed indexes to get letters
    whole_arr = get_specific_indexes(circles)

    # gets the letter where the circles are
    letter = ""
    count = 0 #keep it on array until incremented to next
    for element in whole_arr: #element is [2,4]
        for _, num_in_array in enumerate(element): #num in array 2 then 4
            letter += answers[count][num_in_array] 
        count += 1

    return answers


def main():
    sorted_dic = sort_dictionary(get_file_lines())
    
    # Word Jumble 1. Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his ___."
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles1 = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final1 = ['OO', 'OOOOOO']
    
    sorted_jumble = sort_words(words1)

    print(solve_word_jumble(words1, circles1, final1, sorted_dic, sorted_jumble))

    # # Word Jumble 2. Cartoon prompt for final jumble: "What a dog house is."
    words2 = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles2 = ['____O', '_OO__', '_O___O', 'O____O']
    final2 = ['OOOO', 'OOO']

    sorted_jumble = sort_words(words2)

    print(solve_word_jumble(words2, circles2, final2, sorted_dic, sorted_jumble))

if __name__ == '__main__':
    main()
    print('Time:'+' '+str(time.process_time() - start))