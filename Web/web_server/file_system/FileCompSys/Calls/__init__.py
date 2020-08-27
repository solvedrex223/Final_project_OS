from file_system.FileCompSys.Algorithms.HuffmanCompression import HuffmanCompression
from file_system.FileCompSys.Algorithms.FileDecompression import FileDecompression
from file_system.FileSystem.Packages.dir_functions import ls
from file_system.FileSystem.Packages.Inode import Inode


def cmp(filename, parent_inode_no, new_name=""):
    if new_name == "":
        new_name = filename
    cwd = Inode(parent_inode_no)
    cwd.read()
    blocks = ls(cwd)
    for i in range(len(blocks[1])):
        if blocks[1][i][:-1] == filename:
            inode_no = blocks[0][i]
    HuffmanCompression(inode_no=inode_no, filename=filename, parent_inode=parent_inode_no)
    return True


def dcmp(file_name, cwd, new_file_name):
    blocks = ls(cwd)
    print(blocks)
    for i in range(len(blocks[1])):
        if blocks[1][i][:-1] == file_name:
            inode_no_cmp = int(blocks[0][i])
        if blocks[1][i][:-1] == file_name[:-3] + 'tree':
            inode_no_tree = int(blocks[0][i])

    FileDecompression(inode_no_tree=inode_no_tree, inode_no_cmp=inode_no_cmp, file_name=new_file_name, cwd=cwd.id)
    return True
