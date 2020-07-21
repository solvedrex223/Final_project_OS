class Inode():
    def __init__(self, owner = "", group = "", access_permissions = [[],[],[]], filetype = "", file_access_time = "",
                 links = 0, size = 0, table_of_contents = []):
        self.owner = owner
        self.group = group
        self.filetype = filetype
        self.access_permissions = access_permissions
        self.file_access_time = file_access_time
        self.links = links
        self.size = size
        self.table_of_contents = table_of_contents
    def parse_owner(self):
        self.owner = ord(self.owner)
        return True
    def parse_group(self):
        self.group = ord(self.group)
    def parse_access_permissions(self):
        num1 = ord(self.access_permissions[0])
        num2 = ord(self.access_permissions[1])
        num1 = "{0:b}".format(num1)
        num2 = "{0:b}".format(num2)
        num1 += num2[0]
        for j in range(3):
            for i in range(3):
                if num1[j*3+i] == 1:
                    self.access_permissions[j].append(True)
                else:
                    self.access_permissions[j].append(False)

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
    def binarize_links(self):
        self.links = int_to_string(self.links)
        return True
    def binarize_size(self):
        self.size =  int_to_string(self.size)
        return True
    def binarize_toc(self):
        string = ""
        for number in self.table_of_contents:
            string += int_to_string(number)
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
                number += string[i * 8 + 7 - j] ** 7 - j
            newstring += chr(number)
        self.access_permissions = newstring
        return True

def string_to_int(string):
    binary  = ""
    num = 0
    for char in string:
        binary += "{0:b}".format(ord(char))
    for char in binary:
        binary = char + binary[:-1]
    for i in range(len(binary)):
        num += (int(binary[i]) * 2) ** i
    return num

def int_to_string(num):
    string = "{0:b}".format(num)
    string =  "0"* (len(string)%8) + string
    newstring = ""
    for i in range(len(string)//8):
        number = 0
        for j in range(7,-1,-1):
            number += string[i*8+7-j] ** 7-j
        newstring += chr(number)
    return newstring

