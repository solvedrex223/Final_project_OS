import os
import datetime

import sys
sys.path.insert(1, 'D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server')
from file_system.FileSystem.Packages.General_funcctions import int_to_string, string_to_int, bytes_to_string
from file_system.FileSystem.Packages.Inode import Inode
from file_system.FileSystem.Packages.dir_functions import mkroot



def set_hard_drive(dir_path = "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/"):
    '''try:
        print(True)
        os.mkdir(dir_path)
    except:
        Exception
        print("error")
    '''
    #placeholder = chr(0) * 1024
    for i in range(1, 1000001):
        print(i)
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/"+str(i)+".block","wb")
        file.write(bytes([0]*1024))
        file.close()
    return True
    
def set_inodes_list(dir_path = "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/"):
    filepath = dir_path + "/1.block"
    file = open(filepath, "wb")
    for i in range(264,8,-1):
        for char in int_to_string(num=i, bytes=4):
            file.write(bytes([ord(char)]))
    file.close()
    return True

def set_block_list(dir_path = "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/"):
    filepath = dir_path + "/2.block"
    file = open(filepath, "wb")
    for i in range(1003 + 255, 1003 - 1, -1):
        for char in int_to_string(num=i, bytes=4):
            file.write(bytes([ord(char)]))
    file.close()
    for block in range(1003 +256,1000000,256):
        file = open(dir_path+"/"+str(block-1)+".block", "wb")
        for i in range(block + 255, block - 1, -1):
            print(i)
            if i <= 1000000:
                for char in int_to_string(num=i, bytes=4):
                    file.write(bytes([ord(char)]))
            else:
                for char in int_to_string(num=0, bytes=4):
                    file.write(bytes([ord(char)]))
        file.close()
    return True

def set_inodes():
    x = str(datetime.datetime.now())
    x = x[:10]
    x = x.replace("-", "")
    for i in range(1,9):
        inode = Inode(owner=chr(1), group=chr(1), filetype="d", access_permissions=chr(255) + chr(128), file_access_time=x,
                  links=int_to_string(1, 3),size = int_to_string(0, 4), table_of_contents = int_to_string(0, 4) * 11, id = i)
        inode.write()
        del inode
    for i in range(9,16001):
        inode = Inode(owner=chr(0), group=chr(0), filetype="0", access_permissions=chr(0)*2, file_access_time=x,
                  links=int_to_string(0, 3),size = int_to_string(0, 4), table_of_contents = int_to_string(0, 4) * 11, id = i)
        inode.write()
        del inode

    return True
def read_inodes(min = 1, max = 16000 ):
    for i in range(min,max +1):
        inode = Inode(id=i)
        inode.read()
        print(inode.owner,inode.group,inode.filetype,inode.file_access_time ,inode.access_permissions,inode.links,inode.size ,inode.table_of_contents)
        del inode
    return True

if __name__ == "__main__":
    #set_hard_drive()
    set_inodes_list()
    set_inodes()
    set_block_list()
    mkroot()