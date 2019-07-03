# Lomuto partition scheme

def quick_sort_lumuto(array, lo, hi):
    """
    Sorts elements between indices lo and hi inclusive
    array - a list to sort
    lo - index of the lower end in the range
    hi - index of the higher end
    """
    if lo < hi:
        p = partition_lumuto(array, lo, hi)
        # Recursively sort the 'less than' partition
        quick_sort_lumuto(array, lo, p - 1)
        # Recursively sort the 'greater than' partition
        quick_sort_lumuto(array, p + 1, hi)
    
    return array
    
def partition_lumuto(array, lo, hi):
    """
    Sorts array from lowest to highest element
    """
    pivot = array[hi]

    i = lo - 1
    for j in range(lo, hi):
        if array[j] < pivot:
            i += 1
            # print(str(j) + ' '+str(i))
            # swap indexes if num greater than pivot
            array[i], array[j] = array[j], array[i]
            # print(str(array[i]) +' '+ str(array[j])+' '+'less than pivot switch i & j')
    # swap pivot if partition is complete ()
    # print(str(array[hi]) +' '+ str(array[i + 1])+' '+'switches pivot & i+1')
    array[i + 1], array[hi] = array[hi], array[i + 1]
    return i + 1

# hoare partition scheme

def quick_sort_hoare(array, lo, hi):
    
    if lo < hi:
        p = partition_hoare(array, lo, hi)
        # Recursively sort the 'less than' partition
        quick_sort_hoare(array, lo, p)
            # Recursively sort the 'greater than' partition
        quick_sort_hoare(array, p+1, hi)

    return array

def partition_hoare(array, lo, hi):
    i = lo - 1
    j = hi + 1

    pivot = array[(hi + lo) // 2]
  
    while True:
        while True:
            i += 1
            if array[i] >= pivot:
                break

        while True:
            j -= 1
            if array[j] <= pivot:
                break

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]

array = [3, 7, 8, 2, 1, 9, 5, 4, 9, 9, 7, 5, 20, 40, 80 , 100, 200, 34, 67, 97]
# array = ['hello', 'apple', 'dog', 'cats']
last_index = len(array) - 1
# print(quick_sort_lumuto(array, 0, last_index))
print(quick_sort_hoare(array, 0, last_index))