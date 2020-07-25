from Packages.General_funcctions import int_to_string, string_to_int, write_str_bin, bytes_to_string


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

all other methods should not be called on regular basis since they are used to built the "Useful ones".
'''


class Inode():
    def __init__(self, id ,owner = "", group = "", access_permissions = [[],[],[]], filetype = "", file_access_time = "",
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
                else: string +=0
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
        return 3 + self.id//16

    def get_offset(self):
        return ((self.id-1)%16) * 64

    def write(self):
        file = open("/home/zikin/Documents/Final_project_OS/hard_drive/"+str(self.get_block())+".block", "r+b")
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
        file = open("/home/zikin/Documents/Final_project_OS/hard_drive/" + str(self.get_block()) + ".block", "r+b")
        offset = self.get_offset()
        file.seek(offset + 2)
        file.write(bytes([ord(self.filetype)]))
        file.close()
        return

    def read(self):
        file = open("/home/zikin/Documents/Final_project_OS/hard_drive/" + str(self.get_block()) + ".block", "rb")
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