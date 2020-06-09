'''
The next alogrithm generates a freq hash table from a given file.
Time Complexity O(n)
Space Complexity O(n)
where n are the characters in a file.
'''


def buildFreqHashTable(filepath):
    file  = open(filepath, "r")
    content =  file.read()
    freqTable = {}
    for char in content:
        if freqTable.get(char, False):
            freqTable[char] += 1
        else: freqTable[char] = 1
    file.close()
    return freqTable

if __name__ == "__main__":
    buildFreqHashTable("text.txt")