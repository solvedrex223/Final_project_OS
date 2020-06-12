#Takes as parameter the sorted freqlist, and the filepath
#write on the file to store the tree with the next format.
#each line has the following format line[0] = char, line[:-1] = freq

#coded and maintained by zikln - rodrigoor1999@outlook.com

def TreeToFile(freqlist, filepath):
    file = open(filepath+"tree","w")
    for tree in freqlist:
        file.write(tree.root.char+str(tree.root.freq)+"\n")
    file.close()
    return
