# python3

from random import randint


def partition3(array, left, right):
    return 0


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    '''make a call to partition3 and then two recursive calls 
to randomized_quick_sort'''
    k = left ## where k is the pivot
    i = 1 ## where i is te actual index
    c = 1 ## where it is the counter of times the pivot apears
    for i in range(left+1, right+1):
        if array[i] <  array[k]:
            array[k+1], array[i] = array[i], array[k+1]
            array[k+1], array[k-c+1] = array[k-c+1], array[k+1]
            k+=1
        elif array[i] ==  array[k]:
            array[i], array[k] = array[k], array[i]
            array[k+1], array[i] = array[i], array[k+1]
            c+=1
            k+=1
        else:
            pass
    randomized_quick_sort(array, left, k-c)
    randomized_quick_sort(array,k+1, right)
    return array



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
