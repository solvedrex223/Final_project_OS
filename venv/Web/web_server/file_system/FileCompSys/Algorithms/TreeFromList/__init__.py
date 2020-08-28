#Takes a freqlist containing huff trees
#merges the to smallers ones
#stores the result in a temp variable
#pop the merged tree from the list
#appendds the stored tree
#insertion sorts to secure smalles elements at the end of the list in O(n) time
#when there is only one node left, return it as the hufftree

#coded and maintained by zikln - rodrigoor1999@outlook.com


import file_system.FileCompSys.Algorithms.InsertionSort as Is

def buildTree(freqList):
    while len(freqList) > 1:
        freqList[-1].merge(freqList[-2])
        temptree = freqList[-1]
        freqList.pop()
        freqList.pop()
        freqList.append(temptree)
        Is.insertionSort(freqList)
    return freqList[0]
