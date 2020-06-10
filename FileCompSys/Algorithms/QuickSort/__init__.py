# python3

from random import randint

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    '''make a call to partition3 and then two recursive calls 
to randomized_quick_sort'''
    k = left ## where k is the pivot
    c = 1 ## where it is the counter of times the pivot apears
    for i in range(left+1, right+1):
        try:
            if array[i].root.freq <  array[k].root.freq:
                array[k+1], array[i] = array[i], array[k+1]
                array[k+1], array[k-c+1] = array[k-c+1], array[k+1]
                k+=1
            elif array[i].root.freq ==  array[k].root.freq:
                array[i], array[k] = array[k], array[i]
                array[k+1], array[i] = array[i], array[k+1]
                c+=1
                k+=1
            else:
                pass
        except Exception: pass
    randomized_quick_sort(array, left, k-c)
    randomized_quick_sort(array,k+1, right)
    return array


