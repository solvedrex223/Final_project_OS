import file_system.FileCompSys.DataStructures.HuffmanTree as Ht
import file_system.FileCompSys.Algorithms.TreeFromList as Tfl



#Takes a file
#reads the file line by line
#each line has the following format line[0] = char, line[:-1] = freq
#with the content of the file forms an array of trees.
#returns the built tree.

#coded and maintained by zikln - rodrigoor1999@outlook.com
from file_system.FileSystem.Packages.file_functions import cat

def fileToTree(inode_no):
    content = cat(inode_no)

    content = content.split('\n')
    print(len(content[0]))
    treelist = []
    newline = None
    for line in content:
        if newline:
            newline = None
            treelist.append(Ht.HuffTree(freq=int(line), char= '\n'))
            continue
        if len(line) == 0:
            newline = True
            continue
        treelist.append(Ht.HuffTree(freq=int(line[1:]), char=line[0]))
    return Tfl.buildTree(treelist)