'''
Created on 12 abr. 2020
@author: Zikin

Insertion sort
Avg Case: O(n^2)
worst Case: O(n^2)
Best Case: O(n)
'''

def insertionSort(A):
    l = len(A)
    i = 1
    maxindex = 1 
    while(i < l):
        if A[i].root.freq > A[i-1].root.freq and i >= 1:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1
        else:
            maxindex += 1
            i = maxindex
        #print(A) shows the algorithm
    return True