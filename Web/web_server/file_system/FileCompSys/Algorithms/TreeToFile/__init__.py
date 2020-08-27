#Takes as parameter the sorted freqlist, and the filepath
#write on the file to store the tree with the next format.
#each line has the following format line[0] = char, line[:-1] = freq

#coded and maintained by zikln - rodrigoor1999@outlook.com
from file_system.FileSystem.Packages.file_functions import mk_file

def TreeToFile(freqlist, filename, parent_inode):
    content = ""
    for tree in freqlist:
        content += tree.root.char+str(tree.root.freq)+"\n"
    mk_file(user= 0, file_content= content,ref= filename+'.tree',parent_inode = parent_inode)
    return
