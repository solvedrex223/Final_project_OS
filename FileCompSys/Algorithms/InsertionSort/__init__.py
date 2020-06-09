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
        if A[i] < A[i-1] and i >= 1:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1
        else:
            maxindex += 1
            i = maxindex
        #print(A) shows the algorithm
    return True
                    
if __name__ == '__main__':
    A =  A = [15,10, 25, 40,12, 18, 1]
    insertionSort(A)
    print(A)
    