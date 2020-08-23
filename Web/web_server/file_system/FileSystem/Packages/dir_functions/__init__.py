import sys
sys.path.insert(1, 'D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server')
from file_system.FileSystem.Packages.General_funcctions import bytes_to_string, string_to_int, write_str_bin, int_to_string
from file_system.FileSystem.Packages.Inode import Inode
import file_system.FileSystem.Packages.Block as B


def mkdir(name, cwd):
    LIL = B.super_block(1)
    LIL.load()
    LBL = B.super_block(2)
    LBL.load()
    dir = Inode(id = LIL.free_inode(), filetype='d')
    dir.read()
    dir.filetype = 'd'
    dir.size = 13
    dir.table_of_contents[0] = LBL.free_block()
    file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(dir.table_of_contents[0]) + ".block", "r+b")
    write_str_bin(file,int_to_string(dir.id,4)+'.'+'\n')
    write_str_bin(file,int_to_string(cwd.id,4)+'..'+'\n')
    dir.binarize_all()
    dir.write()
    add_file_to_dir(cwd.id,dir.id,name)

def mkroot():
    LIL = B.super_block(1)
    LIL.load()
    LBL = B.super_block(2)
    LBL.load()
    dir = Inode(id = 2)
    dir.read()
    dir.filetype = 'd'
    dir.size = 13
    dir.table_of_contents[0] = LBL.free_block()
    file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(dir.table_of_contents[0]) + ".block", "r+b")
    write_str_bin(file,int_to_string(2,4)+'.'+'\n')
    write_str_bin(file,int_to_string(2,4)+'..'+'\n')
    dir.binarize_all()
    dir.write()
    return


#la funcion falla si el archivo no esiste
def add_file_to_dir(i_dir, i_file,name):
    i_dir = Inode(i_dir)
    i_dir.read()
    i_file = Inode(i_file)
    i_file.read()
    current_size = i_dir.size
    future_size = current_size +4 + 1 + len(name)
    block = future_size//1024
    if (future_size //1024 == current_size //1024):
        offset = current_size % 1024
        writing_block = find_block(block, i_dir.table_of_contents)
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(writing_block) + ".block", "r+b")
        file.seek(offset)
        write_str_bin(file, int_to_string(i_file.id, 4) + name + "\n")
        file.close()
    else:
        offset = current_size % 1024
        writing_block = find_block(block, i_dir.table_of_contents)
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(writing_block) + ".block", "r+b")
        file.seek(offset)
        string1 = int_to_string(i_file.id, 4) + name + "\n"[0:1024 - offset]
        string2 = int_to_string(i_file.id, 4) + name + "\n"[1024 - offset:]
        write_str_bin(file, string1)
        file.close()
        LBL = B.super_block(2)
        LBL.load()
        if block < 8:
            i_dir.table_of_contents[block] =  LBL.free_block()
            last_block = i_dir.table_of_contents[block]
        if block < 264:
            offset_1 = (block - 8) % 256
            if  offset_1== 0:
                i_dir.table_of_contents[8] = LBL.free_block()
            file_1 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(i_dir.table_of_contents[8]) + ".block", "r+b")
            file_1.seek(offset_1 *4)
            new_block = LBL.free_block()
            write_str_bin(file_1,int_to_string(new_block,4))
            last_block = new_block
            file_1.close()
        if block < 65800:
            offset_1 = (block - 264) % 65536
            offset_R1 = (block - 264) // 256
            offset_2 = (block - 264) % 256
            if  offset_1== 0:
                i_dir.table_of_contents[9] = LBL.free_block()
            file_1 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(i_dir.table_of_contents[9]) + ".block", "r+b")
            file_1.seek(offset_R1 *4)
            if offset_2 == 0:
                new_block = LBL.free_block()
                write_str_bin(file_1, int_to_string(new_block, 4))
            else:
                new_block = string_to_int(bytes_to_string(file_1.read(4)))
            file_1.close()
            file_2 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(new_block) + ".block", "r+b")
            file_2.seek(offset_2 *4)
            new_block = LBL.free_block()
            write_str_bin(file_2, int_to_string(new_block, 4))
            last_block = new_block
            file_2.close()
        else:
            offset_1 = (block - 65800) // 65536
            offset_2 = (block - 65800) // 256
            offset_3 = (block - 65800) % 256
            if  block == 65800:
                i_dir.table_of_contents[10] = LBL.free_block()
            file_1 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(i_dir.table_of_contents[10]) + ".block", "r+b")
            file_1.seek(offset_1 *4)
            if offset_2 == 0:
                new_block = LBL.free_block()
                write_str_bin(file_1, int_to_string(new_block, 4))
            else:
                new_block = string_to_int(bytes_to_string(file_1.read(4)))
            file_1.close()
            file_2 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(new_block) + ".block", "r+b")
            file_2.seek(offset_2 *4)
            if offset_3 == 0:
                new_block = LBL.free_block()
                write_str_bin(file_2, int_to_string(new_block, 4))
            else:
                new_block = string_to_int(bytes_to_string(file_2.read(4)))
            file_2.close()
            file_3 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(new_block) + ".block", "r+b")
            file_3.seek(offset_3 *4)
            new_block = LBL.free_block()
            write_str_bin(file_3, int_to_string(new_block, 4))
            last_block = new_block
            file_3.close()
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(last_block) + ".block", "r+b")
        write_str_bin(file, string2)
        file.close()
    i_dir.size = future_size
    i_dir.binarize_all()
    i_dir.write()
    return True

def find_block(no_block, array):
    if no_block < 8:
        return array[no_block]
    elif no_block < 264:
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/"+array[8]+".block", "rb")
        file.seek((no_block - 8) *4)
        data_block  = string_to_int(bytes_to_string(file.read(4)))
        file.close()
        return data_block
    elif no_block < 65800:
        offset_1 = (no_block - 264)//256
        offset_2 = (no_block - 264)%256
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + array[9] + ".block", "rb")
        file.seek(offset_1 * 4)
        data_block = string_to_int(bytes_to_string(file.read(4)))
        file.close()
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" +data_block + ".block", "rb")
        file.seek(offset_2 * 4)
        data_block = string_to_int(bytes_to_string(file.read(4)))
        file.close()
        return data_block

    else:
        offset_1 = (no_block - 65800)//65536
        offset_2 = (no_block - 65800)%65536
        offset_3 = (no_block - 65800)%256
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + array[9] + ".block", "rb")
        file.seek(offset_1 * 4)
        data_block = string_to_int(bytes_to_string(file.read(4)))
        file.close()
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" +data_block + ".block", "rb")
        file.seek(offset_2 * 4)
        data_block = string_to_int(bytes_to_string(file.read(4)))
        file.close()
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" +data_block + ".block", "rb")
        file.seek(offset_3 * 4)
        data_block = string_to_int(bytes_to_string(file.read(4)))
        file.close()
        return data_block


def ls(cwd):
    content = [[], []]
    stored = ""
    for block in cwd.find_content_blocks():
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(block) + ".block", "rb")
        offset = 0
        while offset < 1024:
            for line in file.readlines():
                line = bytes_to_string(line)
                if offset == 0:
                    offset += len(line)
                    line = stored + line
                    stored = ""
                else:
                    offset += len(line)
                if offset == 1024:
                   stored = line
                else:
                    content[0].append(string_to_int(line[0:4]))
                    content[1].append(line[4:])
                    offset +=1
    if content[0][-1] == 0:
        content[0].pop()
        if len(content[0]) != len(content[1]):
            content[1].pop()
    returnable=[[],[]]
    for i in range(len(content[0])):
        if int(content[0][i]) != 0:
            returnable[0].append(content[0][i])
            returnable[1].append(content[1][i])
    return returnable



def rm_from_dir(dir_name, cwd):
    byte_no = find_file(cwd, dir_name)
    files = find_files(cwd)
    if files.get(dir_name,False):
        inode_no = files[dir_name]
    else:
        return False
    block = find_block(byte_no // 1024, cwd.table_of_contents)
    file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(block) + ".block", "r+b")
    file.seek(byte_no%1024)
    bytes = (byte_no % 1024 + len(dir_name) + 1)
    if bytes < 1024:
        write_str_bin(file, chr(0)*(len(dir_name)+4))
        file.close()
    else:
        write_str_bin(file, chr(0) * (1024- (byte_no%1024)))
        file.close()
        block = find_block(byte_no // 1024 +1, cwd.table_of_contents)
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(block) + ".block", "r+b")
        write_str_bin(file, chr(0) * (bytes -1023))
        file.close()
    return int(inode_no)


def find_files(cwd):
    files = {}
    content = ls(cwd)
    for i in range(len(content[0])):
        files[content[1][i][:-1]] = int(content[0][i])
    return files

def find_file(cwd, name):
    content = ls(cwd)
    offset = 0
    for i in range(len(content[0])):
        if content[1][i] == name+'\n':
            return offset
        else:
            offset += 4 + len(content[1][i])
    return -1


def cd(dir_name, files):
    if files.get(dir_name, False):
        wd = files[dir_name]
        wd = Inode(wd)
        wd.read()
        if wd.filetype == 'd':
            return wd
        else:
            print(dir_name+" is not a directory.")
            wd = files['.']
            wd = Inode(wd)
            wd.read()
            return wd
    else:
        print("directory doesn't exist")
        wd = files['.']
        wd = Inode(wd)
        wd.read()
        return wd