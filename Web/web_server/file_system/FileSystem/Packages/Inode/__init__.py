import sys
sys.path.insert(1, 'D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server')
from file_system.FileSystem.Packages.General_funcctions import int_to_string, string_to_int, write_str_bin, bytes_to_string
from math import  ceil

#Useful functions from the outside self.write and self.read
#id parameter should always be filled during instantiation.

'''

Inodes:
Inode(int) -> instantiates a inode object that should be used with existing inodes, needs to be read() before used.
Inode(*) -> Should be used when creating a new inode.
 
Useful SuperBlocks methods
write()
read()
delete()
parse_all()
binarize_all()
all other methods should not be called on regular basis since they are used to built the "Useful ones".
'''


class Inode():
    def __init__(self, id ,owner = 0, group = 0, access_permissions = [[True,True,True],[True,True,True],[True,True,True]], filetype = "x", file_access_time = "19700101",
                 links = 0, size = 0, table_of_contents = []):
        self.owner = owner
        self.group = group
        self.filetype = filetype
        self.access_permissions = access_permissions
        self.file_access_time = file_access_time
        self.links = links
        self.size = size
        self.table_of_contents = table_of_contents
        self.id =id

    def parse_owner(self):
        self.owner = ord(self.owner)
        return True

    def parse_group(self):
        self.group = ord(self.group)

    def parse_access_permissions(self):
        permissions = [[], [], []]
        num1 = ord(self.access_permissions[0])
        num2 = ord(self.access_permissions[1])
        num1 = '{:08b}'.format(num1)
        num2 = "{:08b}".format(num2)
        num1 += num2[0]
        for j in range(3):
            for i in range(3):
                if num1[j*3+i] == "1":
                    permissions[j].append(True)
                else:
                    permissions[j].append(False)
        self.access_permissions = permissions
        return True

    def parse_links(self):
        self.links = string_to_int(str(self.links))
        return True

    def parse_size(self):
        self.size = string_to_int(str(self.size))
        return True

    def parse_toc(self):
        new_table = []
        for i in range(len(self.table_of_contents)//4):
            new_table.append(string_to_int(self.table_of_contents[i*4:(i+1)*4]))
        self.table_of_contents = new_table
        return True

    def parse_all(self):
        self.parse_size()
        self.parse_toc()
        self.parse_group()
        self.parse_owner()
        self.parse_access_permissions()
        self.parse_links()
        return True
    def binarize_owner(self):
        self.owner = chr(self.owner)
        return True
    def binarize_group(self):
        self.group = chr(self.group)
        return True
    def binarize_links(self):
        self.links = int_to_string(self.links,3)
        return True

    def binarize_size(self):
        self.size =  int_to_string(self.size, 4)
        return True

    def binarize_toc(self):
        string = ""
        for number in self.table_of_contents:
            string += int_to_string(number,4)
        self.table_of_contents = string
        return True

    def binarize_access_permissions(self):
        string = ""
        for i in range(3):
            for bool in self.access_permissions[i]:
                if bool: string += "1"
                else: string += '0'
        string += "0" * 7
        newstring = ""
        for i in range(len(string) // 8):
            number = 0
            for j in range(7, -1, -1):
                number += int(string[i * 8 + 7 - j])* 2 ** j
            newstring += chr(number)
        self.access_permissions = newstring
        return True
    def binarize_all(self):
        self.binarize_owner()
        self.binarize_group()
        self.binarize_size()
        self.binarize_links()
        self.binarize_toc()
        self.binarize_access_permissions()
        return True
    def get_block(self):
        returnable = self.id//16
        return 3 + returnable

    def get_offset(self):
        return ((self.id-1)%16) * 64

    def write(self):
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/"+str(self.get_block())+".block", "r+b")
        offset = self.get_offset()
        file.seek(offset)
        file.write(bytes([ord(self.owner)]))
        file.write(bytes([ord(self.group)]))
        file.write(bytes([ord(self.filetype)]))
        write_str_bin(file,self.access_permissions)
        write_str_bin(file, self.file_access_time)
        write_str_bin(file, self.links)
        write_str_bin(file, self.size)
        write_str_bin(file, self.table_of_contents)
        file.close()
        return True

    def delete(self):
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.get_block()) + ".block", "r+b")
        offset = self.get_offset()
        file.seek(offset + 2)
        self.filetype = "0"
        file.write(bytes([ord(self.filetype)]))
        file.close()
        return

    def read(self):
        file = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.get_block()) + ".block", "rb")
        file.seek(self.get_offset())
        self.owner = bytes_to_string(file.read(1))
        self.group = bytes_to_string(file.read(1))
        self.filetype = bytes_to_string(file.read(1))
        self.access_permissions = bytes_to_string(file.read(2))
        self.file_access_time = bytes_to_string(file.read(8))
        self.links = bytes_to_string(file.read(3))
        self.size = bytes_to_string(file.read(4))
        self.table_of_contents  = bytes_to_string(file.read(44))
        self.parse_all()
        file.close()
        return True

    def find_all_blocks(self):
        queue = [[],[],[],[]]
        blocks = ceil(self.size / 1024)
        block  = 0
        while block < blocks:

            if block < 8:
                queue[0].append(self.table_of_contents[block])
                block += 1
            elif len(queue[1] ) ==0:
                queue[0].append(self.table_of_contents[block])
                offset = 0
                file = open(
                    "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.table_of_contents[8]) + ".block",
                    "rb")
                while block < blocks and offset < 1024:
                    offset += 4
                    queue[1].append(string_to_int(bytes_to_string(file.read(4))))
                    block +=1
                file.close()

            elif len(queue[2])==0:
                queue[0].append(self.table_of_contents[9])
                file_1 = open(
                    "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.table_of_contents[9]) + ".block",
                    "rb")
                offset_1 = 0
                while block < blocks and offset_1 < 1024:
                    offset_1 += 4
                    queue[1].append(string_to_int(bytes_to_string(file_1.read(4))))
                    offset_2 = 0
                    file_2 =  open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(queue[1][-1]) + ".block",
                    "rb")
                    while block < blocks and offset_2 < 1024:
                        offset_2 += 4
                        queue[2].append(string_to_int(bytes_to_string(file_2.read(4))))
                        block += 1
                    file_2.close()
                file_1.close()

            else:
                queue[0].append(self.table_of_contents[10])
                file_1 = open(
                    "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.table_of_contents[10]) + ".block",
                    "rb")
                offset_1 = 0
                while block < blocks and offset_1 < 1024:
                    offset_1 += 4
                    queue[1].append(string_to_int(bytes_to_string(file_1.read(4))))
                    offset_2 = 0
                    file_2 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(queue[1][-1]) + ".block",
                                  "rb")
                    while block < blocks and offset_2 < 1024:
                        offset_2 += 4
                        queue[2].append(string_to_int(bytes_to_string(file_2.read(4))))
                        file_3 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(queue[2][-1]) + ".block",
                                  "rb")
                        offset_3 = 0
                        while block < blocks and offset_3 < 1024:
                            offset_3 += 4
                            queue[3].append(string_to_int(bytes_to_string(file_3.read(4))))
                            block += 1
                        file_3.close()
                    file_2.close()
                file_1.close()
        returnable = []
        for q in queue:
            returnable += q
        return returnable

    def find_content_blocks(self):
        queue = [[],[],[],[]]
        queue2 = []
        blocks = ceil(self.size / 1024)
        block  = 0
        while block < blocks:
            if block < 8:
                queue[0].append(self.table_of_contents[block])
                queue2.append(queue[0][-1])
                block += 1
            elif len(queue[1] ) ==0:
                queue[0].append(self.table_of_contents[block])
                offset = 0
                file = open(
                    "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.table_of_contents[8]) + ".block",
                    "rb")
                while block < blocks and offset < 1024:
                    offset += 4
                    queue[1].append(string_to_int(bytes_to_string(file.read(4))))
                    queue2.append(queue[1][-1])
                    block +=1
                file.close()

            elif len(queue[2])==0:
                queue[0].append(self.table_of_contents[9])
                file_1 = open(
                    "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.table_of_contents[9]) + ".block",
                    "rb")
                offset_1 = 0
                while block < blocks and offset_1 < 1024:
                    offset_1 += 4
                    queue[1].append(string_to_int(bytes_to_string(file_1.read(4))))
                    offset_2 = 0
                    file_2 =  open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(queue[1][-1]) + ".block",
                    "rb")
                    while block < blocks and offset_2 < 1024:
                        offset_2 += 4
                        queue[2].append(string_to_int(bytes_to_string(file_2.read(4))))
                        queue2.append(queue[2][-1])
                        block += 1
                    file_2.close()
                file_1.close()

            else:
                queue[0].append(self.table_of_contents[10])
                file_1 = open(
                    "D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(self.table_of_contents[10]) + ".block",
                    "rb")
                offset_1 = 0
                while block < blocks and offset_1 < 1024:
                    offset_1 += 4
                    queue[1].append(string_to_int(bytes_to_string(file_1.read(4))))
                    offset_2 = 0
                    file_2 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(queue[1][-1]) + ".block",
                                  "rb")
                    while block < blocks and offset_2 < 1024:
                        offset_2 += 4
                        queue[2].append(string_to_int(bytes_to_string(file_2.read(4))))
                        file_3 = open("D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server/file_system/FileSystem/Packages/hard_drive/" + str(queue[2][-1]) + ".block",
                                  "rb")
                        offset_3 = 0
                        while block < blocks and offset_3 < 1024:
                            offset_3 += 4
                            queue[3].append(string_to_int(bytes_to_string(file_3.read(4))))
                            queue2.append(queue[3][-1])
                            block += 1
                        file_3.close()
                    file_2.close()
                file_1.close()
        returnable = queue2
        return returnable