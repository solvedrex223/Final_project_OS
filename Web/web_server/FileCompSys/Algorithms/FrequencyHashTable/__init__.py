'''
The next alogrithm generates a freq hash table from a given file.
Time Complexity O(n)
Space Complexity O(n)
where n are the characters in a file.
'''

#coded and maintained by zikln - rodrigoor1999@outlook.com
from file_system.FileSystem.Packages.file_functions import cat

def buildFreqHashTable(inode_no):
    '''
    file  = open(filepath, "r")
    content =  file.read()
    '''
    content = cat(inode_no= inode_no)
    freqTable = {}
    for char in content:
        if freqTable.get(char, False):
            freqTable[char] += 1
        else: freqTable[char] = 1
    return freqTable
'''
if __name__ == "__main__":
    buildFreqHashTable("text.txt")
'''