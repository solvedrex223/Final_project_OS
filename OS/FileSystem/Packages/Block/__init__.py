from Packages.General_funcctions import string_to_int, write_str_bin, bytes_to_string, int_to_string
from Packages.Inode import Inode
'''

superblock:
super_block(1) -> LIL
super_block(2) -> LBL

use
init()
load()
code ...

Useful SuperBlocks methods
load()
free_block()
free_inode()
receive_block(int)
receive_inode(int)
all other methods should not be called on regular basis since they are used to built the "Useful ones".
'''

class Block:
    def __init__(self, id):
        self.info = chr(0) *1024
        self.mem_usada  = 0
        self.id = id
        self.filepath = "/home/zikin/Documents/Final_project_OS/hard_drive/"+str(id)+".block"
    def append_info(self, info): #Adds new info to self.info
        if self.mem_usada > 1024:
            return False
        for i in range(len(info)):
            self.info[self.mem_usada] = info[i]
            self.mem_usada +=1
        return True
    def read_info(self): #Reads binary from file and updates self.info with string formatted info
        file  =  open(self.filepath, "rb")
        self.info = bytes_to_string(file.read())
        self.info += chr(0) * (1024 - len(self.info))
        file.close()
        return True

    def reset_info(self): #Resets the block
        self.info = chr(0) * 1024
        self.mem_usada = 0
        return True
    def write_info(self): #Writes the whole Block to disk
        file = open(self.filepath, "r+b")
        write_str_bin(file=file,  string=self.info)
        return True

class inodeBlock(Block):
    def __init__(self, id):
        Block.__init__(id)
        self.inodes = [] * 16
    def load_inodes(self): ##Loads an inode Block Needs Rework
        Block.read_info()
        for i in range(16):
            mult  = i * 64
            owner =  mult
            group =  mult + 1
            filetype = mult +2
            access_permissions = mult + 4
            file_access_time = mult + 6
            links = mult + 12
            size =  mult + 15
            table_of_contents = mult + 19
            self.inodes[i] = Inode(self.info[owner:group],self.info[group:filetype],self.info[filetype:access_permissions],
                                   self.info[access_permissions:file_access_time],
                                   self.info[file_access_time:links], self.info[links:size],
                                   self.info[size:table_of_contents], self.info[table_of_contents: (i+1)*64])
            self.inodes[i].parse_all()

class super_block(Block):

    def __init__(self, id):
        Block.__init__(self, id)
        if self.id == 1:
            self.LIL = []
            self.LBL = None
        else:
            self.LBL = []
            self.LIL = None

    def write_info(self):
        self.update_info()
        Block.write_info(self)
        return True

    def append(self, num):
        if self.LBL != None:
            file = open(self.filepath, "r+b")
            file.seek(len(self.LBL)*4, 0)
            write_str_bin(file = file, string= int_to_string(num, 4))
            self.LBL.append(num)
            self.update_info()
            file.close()
            return True
        else:
            file = open(self.filepath, "r+b")
            file.seek(len(self.LIL)*4, 0)
            self.clear_inode(num)
            write_str_bin(file=file, string=int_to_string(num, 4))
            self.LIL.append(num)
            self.update_info()
            return True



    def pop(self):
        if self.LBL != None:
            file = open(self.filepath, "r+b")
            num = self.LBL.pop() ##checar
            file.seek(len(self.LBL)*4, 0)
            write_str_bin(file = file, string= int_to_string(0, 4))
            self.update_info()
            file.close()
            return num
        else:
            file = open(self.filepath, "r+b")
            num = self.LIL.pop()
            file.seek(len(self.LIL)*4, 0)
            write_str_bin(file = file, string= int_to_string(0, 4))
            self.update_info()
            file.close()
            return num


    def load(self): #Reads the file content and sets up the LBL or LIL
        Block.read_info(self)
        if self.LBL != None:
            for i in range((len(self.info)//4)):
                num = string_to_int(self.info[i*4:(i+1)*4])
                if num != 0:
                    self.LBL.append(num)
        else:
            for i in range((len(self.info)//4)):
                num = string_to_int(self.info[i*4:(i+1)*4])
                if num != 0:
                    self.LIL.append(num)

    def update_info(self): #Updates self.info to be up to date with LBL or LIL
        new_info = ""
        if self.id == 1:
            for num in self.LIL:
                new_info += int_to_string(num, 4)
        else:
            for num in self.LBL:
                new_info += int_to_string(num, 4)
        self.info = new_info + chr(0) * (1024-len(new_info))
        return True

    def free_block(self): #Frees a Memory Block from the LBL, returns the freed Block
        if len(self.LBL) > 1:
            return self.pop()
        else:
            return self.refill_LBL()

    def refill_LBL(self): #Refills the the LBL when would empty, returns the pending BLock
        if len(self.LBL) != 1:
            return False
        block = self.LBL.pop()
        self.filepath = "/home/zikin/Documents/Final_project_OS/hard_drive/" + str(block) + ".block"
        self.load()
        self.filepath = "/home/zikin/Documents/Final_project_OS/hard_drive/" + str(self.id) + ".block"
        self.write_info()
        return block

    def recieve_block(self, block_no):
        if len(self.LBL) < 256:
            self.append(block_no)
        else:
            self.clean_LBL(block_no)
        return True

    def clean_LBL(self,block_no):
        self.filepath = "/home/zikin/Documents/Final_project_OS/hard_drive/" + str(block_no) + ".block"
        self.write_info()
        self.LBL = [block_no]
        self.filepath = "/home/zikin/Documents/Final_project_OS/hard_drive/2.block"
        self.write_info()
        return True

    def receive_inode(self, inode_no):
        if len(self.LIL) < 256:
            self.append(inode_no)
        elif self.LIL[0] > inode_no:
            self.change_rem_inode(inode_no)
        else:
            self.clear_inode(inode_no)
        return True

    def change_rem_inode(self,inode_no):
        file  =  open(self.filepath, "r+b")
        self.LIL[0] = inode_no
        self.clear_inode(inode_no)
        write_str_bin(file= file, string=int_to_string(inode_no,4))
        file.close()
        return True

    def clear_inode(self, inode_no):
        inode = Inode(id=inode_no)
        inode.read()
        inode.filetype = "0"
        inode.delete()
        return True

    def free_inode(self):
        if len(self.LIL) > 1:
            return self.pop()
        else:
            inode_no = self.LIL.pop()
            for i in range(inode_no + 1,16001):
                if len(self.LIL)  == 256:
                    break
                inode = Inode(id = i)
                inode.read()
                if inode.filetype == "0":
                    self.LIL.append(i)
                del inode
            self.LIL.reverse()
            self.write_info()
            return True