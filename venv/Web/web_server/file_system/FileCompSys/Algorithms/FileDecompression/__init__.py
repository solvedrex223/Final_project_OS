import file_system.FileCompSys.Algorithms.FileToTree as Ftt

#Inputs File
#1Rebuilds the hufftre from file,
#2 takes the compressed file, reads it as integers, transforms it to a binary string,
#3 Then uses the string to traverse the tree.
#4 when finds a char writes it out in the uncompressed file, and returns to the root of the tree.
#output none, but writes the uncommpressed file.

#coded and maintained by zikln - rodrigoor1999@outlook.com
from file_system.FileSystem.Packages.file_functions import cat, mk_file

def FileDecompression(inode_no_tree, inode_no_cmp, file_name, cwd):
    huffTree = Ftt.fileToTree(inode_no_tree)
    '''
    file = open(filepath, "rb")
    '''
    content = cat(inode_no_cmp)
    new_content = content.split('\n')
    for i in range(len(new_content)): new_content[i] +='\n'
    testable = ''.join(new_content)
    if len(testable) == content:
        pass
    else:
        new_content[-1] = new_content[-1][:-1]
    node = huffTree.root
    new_file_content = ""

    for line in new_content:
        for num in line:
            binary = "{:08b}".format(ord(num))
            for bit in binary:
                if bit == "0":
                    node = node.left
                else:
                    node = node.right
                if node.char:
                    if node.freq > 0:
                        new_file_content += node.char
                        node.freq -= 1
                    node = huffTree.root
    mk_file(user= 0,file_content=new_file_content,ref=file_name ,parent_inode= cwd)
    return
