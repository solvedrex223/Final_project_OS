import DataStructures.HuffmanTree as Ht
import Algorithms.TreeFromList as Tfl



#Takes a file
#reads the file line by line
#each line has the following format line[0] = char, line[:-1] = freq
#with the content of the file forms an array of trees.
#returns the built tree.

#coded and maintained by zikln - rodrigoor1999@outlook.com

def fileToTree(filepath):
    treefile = open(filepath, "r")
    treelist = []
    newline = None
    for line in treefile.readlines():
        if newline:
            newline = None
            treelist.append(Ht.HuffTree(freq=int(line[:-1]), char=line[-1]))
            continue
        if len(line) == 1:
            newline = True
            continue
        treelist.append(Ht.HuffTree(freq=int(line[1:-1]), char=line[0]))
    treefile.close()
    return Tfl.buildTree(treelist)