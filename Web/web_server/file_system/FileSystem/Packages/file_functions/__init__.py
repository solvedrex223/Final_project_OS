import sys
string = sys.path[0]
string = string.split("\\")
while string[len(string) - 1] != "web_server":
    string.pop()
for i in range(len(string) - 1):
    string[i]+= "\\"
r_sys = "".join(string)
sys.path.insert(1, r_sys)
from file_system.FileSystem.Packages.General_funcctions import write_str_bin, int_to_string, bytes_to_string, string_to_int,route
from file_system.FileSystem.Packages.Inode import Inode
import file_system.FileSystem.Packages.Block as B
import  math
from file_system.FileSystem.Packages.dir_functions import add_file_to_dir


def rm(inode_no):
    if inode_no == False:
        return False
    inode  = Inode(inode_no)
    inode.read()
    LBL = B.super_block(2)
    LBL.load()
    for block in inode.find_all_blocks():
        del_block = B.Block(block)
        del_block.write_info()
        LBL.recieve_block(block)
    LIL = B.super_block(1)
    LIL.load()
    LIL.receive_inode(inode_no)
    return True


def mk_file(user, file_content, ref, parent_inode):
    LIL = B.super_block(1)
    LBL = B.super_block(2)
    LIL.load()
    LBL.load()
    no_inodo = LIL.free_inode()
    inodo = Inode(id= no_inodo)
    inodo.read()
    inodo.filetype = 'x'
    inodo.owner = user
    inodo.size = len(file_content)
    no_blocks = math.ceil(len(file_content) / 1024)
    block = 0
    while block < no_blocks:
        if block< 8:
            inodo.table_of_contents[block] = LBL.free_block()
            file = open(route + str(inodo.table_of_contents[block]) + ".block","r+b")
            if (block+1) *1024 < len(file_content):
                write_str_bin(file, file_content[block * 1024: (block+1)*1024])
            else:
                write_str_bin(file, file_content[block * 1024:])
            file.close()
            block +=1
        elif block < 264:
            inodo.table_of_contents[8] = LBL.free_block()
            offset = 0
            file_1 = open(
                route + str(inodo.table_of_contents[8]) + ".block",
                "r+b")
            while offset < 1024 and block < no_blocks:
                offset +=4
                no_block = LBL.free_block()
                write_str_bin(file_1, int_to_string(no_block, 4))
                file_2 = open(route + str(no_block) + ".block","r+b")
                if (block + 1) * 1024 < len(file_content):
                    write_str_bin(file_2, file_content[block * 1024: (block + 1) * 1024])
                else:
                    write_str_bin(file_2, file_content[block * 1024:])
                block += 1
                file_2.close()
            file_1.close()
        elif block <65800:
            inodo.table_of_contents[9] = LBL.free_block()
            offset_1 = 0
            file_1 = open(
                route + str(inodo.table_of_contents[9]) + ".block",
                "r+b")
            while offset_1 < 1024 and block < no_blocks:
                offset_1 += 4
                no_block = LBL.free_block()
                write_str_bin(file_1, int_to_string(no_block, 4))
                file_2 = open(route + str(no_block) + ".block", "r+b")
                offset_2 = 0
                while offset_2 < 1024 and block < no_blocks:
                    offset_2 +=4
                    no_block = LBL.free_block()
                    write_str_bin(file_2, int_to_string(no_block, 4))
                    file_3 = open(route + str(no_block) + ".block", "r+b")
                    if (block + 1) * 1024 < len(file_content):
                        write_str_bin(file_3, file_content[block * 1024: (block + 1) * 1024])
                    else:
                        write_str_bin(file_3, file_content[block * 1024:])
                    block += 1
                    file_3.close()
                file_2.close()
            file_1.close()
        else:
            inodo.table_of_contents[10] = LBL.free_block()
            offset_1 = 0
            file_1 = open(
                route + str(inodo.table_of_contents[10]) + ".block",
                "r+b")
            while offset_1 < 1024 and block < no_blocks:
                offset_1 += 4
                no_block = LBL.free_block()
                write_str_bin(file_1, int_to_string(no_block, 4))
                file_2 = open(route + str(no_block) + ".block", "r+b")
                offset_2 = 0
                while offset_2 < 1024 and block < no_blocks:
                    offset_2 +=4
                    no_block = LBL.free_block()
                    write_str_bin(file_2, int_to_string(no_block, 4))
                    file_3 = open(route + str(no_block) + ".block", "r+b")
                    offset_3 = 0
                    while offset_3 < 1024  and block < no_blocks:
                        offset_3 += 4
                        no_block = LBL.free_block()
                        write_str_bin(file_3, int_to_string(no_block, 4))
                        file_4 = open(route + str(no_block) + ".block",
                                      "r+b")
                        if (block + 1) * 1024 < len(file_content):
                            write_str_bin(file_4, file_content[block * 1024: (block + 1) * 1024])
                        else:
                            write_str_bin(file_4, file_content[block * 1024:])
                        block += 1
                        file_4.close()
                    file_3.close()
                file_2.close()
            file_1.close()
    inodo.binarize_all()
    inodo.write()
    add_file_to_dir(i_dir = parent_inode, i_file = inodo.id, name= ref)
    return True

def cat(inode_no):
    inode = Inode(int(inode_no))
    inode.read()
    content = ""
    blocks = inode.find_content_blocks()
    for i in range(len(blocks)):
        file = open(route + str(blocks[i]) + ".block",
                                      "r+b")
        if i == len(blocks) -1:
            content += bytes_to_string(file.read(inode.size %1024))
        else:
            content += bytes_to_string(file.read())
        file.close()
    return content