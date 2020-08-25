#Takes a pathfile and a hash table that contains key == char value == binary as str
#runs to every bit of the file
#when 8 ar stored tansforms the binary into a byte and writes it in the comppressed file
#If bitss are leftover their are given each the highest bit denomination available  and converted to int
#ie 0b101 = 0b10100000 = 128+32 = 160 and writes the corresponding byte.
#returns nothing.

#coded and maintained by zikln - rodrigoor1999@outlook.com
from file_system.FileSystem.Packages.file_functions import cat, mk_file
from file_system.FileSystem.Packages.General_funcctions import *

def FileCompression(inode_no,filename, Comptable, parent_directory):
    power = 7
    binary = None
    content = cat(inode_no)
    filename = filename + ".cmp"
    compressed = ""
    for char in content:
        for bit in Comptable[char]:
            if power == -1:
                power = 7
                compressed += chr(binary)
                binary = None
            if binary == None:
                binary = (2 ** power)  * int(bit)
            else:
                binary += (2 ** power)  * int(bit)
            power -= 1
    if binary:
        compressed += chr(binary)
    mk_file(user = 0, file_content=  compressed, ref = filename, parent_inode = parent_directory)
    return



