# # Lomuto partition scheme


def quick_sort(array, lo, hi):
    """
    Sorts elements between indices lo and hi inclusive
    array - a list to sort
    lo - index of the lower end in the range
    hi - index of the higher end
    """
    if lo < hi:
        p = partition(array, lo, hi)
        # Recursively sort the 'less than' partition
        quick_sort(array, lo, p - 1)
         # Recursively sort the 'greater than' partition
        quick_sort(array, p + 1, hi)
    
    return array
    
def partition(array, lo, hi):
    """
    creates a partition between smaller and greater values using pivot
    """
    pivot = array[hi]

    i = lo - 1
    for j in range(lo, hi):
        if array[j] < pivot:
            i += 1
            # swap indexes
            array[i], array[j] = array[j], array[i]
    # swap pivot with 
    array[i + 1], array[hi] = array[hi], array[i + 1]
    return i + 1


array = [3, 7, 8, 2, 1, 9, 5, 4]
last_index = len(array) - 1
print(quick_sort(array, 0, last_index))

# array = [3, 7, 8, 2, 1, 9, 5, 4]
# print(quick_sort(array,0,len(array)-1))


    