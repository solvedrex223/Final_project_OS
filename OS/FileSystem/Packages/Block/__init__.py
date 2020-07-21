from Packages.Inode import Inode, string_to_int


class Block:
    def __init__(self, id, filepath):
        self.info = "\0" *1024
        self.mem_usada  = 0
        self.id = id
        self.filepath = filepath
    def write_info(self, info):
        if self.mem_usada == 1024:
            return False
        for i in range(len(info)):
            self.info[self.mem_usada] = info[i]
            self.mem_usada +=1
        return True
    def read_info(self):
        file  =  open(self.filepath)
        self.info = file.read()
        return True
    def reset_info(self):
        self.info = ["\0"] * 1024
        self.mem_usada = 0
        return True

class inodeBlock(Block):
    def __init__(self, id, filepath):
        Block.__init__(id, filepath)
        self.inodes = [] * 16
    def load_inodes(self):
        Block.read_info()
        for i in range(16):
            mult  = i * 64
            owner =  mult
            group =  mult + 1
            filetype = mult +2
            access_permissions = mult + 3
            file_access_time = mult + 5
            links = mult + 11
            size =  mult + 14
            table_of_contents = mult + 18
            self.inodes[i] = Inode(self.info[owner:group],self.info[group:filetype],self.info[filetype:access_permissions],
                                   self.info[access_permissions:file_access_time],
                                   self.info[file_access_time:links], self.info[links:size],
                                   self.info[size:table_of_contents], self.info[table_of_contents: (i+1)*64])
            self.inodes[i].parse_all()

class super_block(Block):
    def __init__(self, filepath):
        Block.__init__(filepath)
        self.LBL = []
        self.LIL = []
    def load(self):
        file  = open(self.filepath)
        content = file.read()
        file.close()
        for i in range((len(content)//4)//2):
            self.LBL.append(string_to_int(content[i*4:(i+1)*4]))
        for i in range((len(content) // 4) // 2,(len(content) // 4) ):
            self.LIL.append(string_to_int(content[i * 4:(i + 1) * 4]))
