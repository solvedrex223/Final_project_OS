class Bloque:

    def __init__(self,id):
        self.info = ["\0"] * 1024
        self.mem_usada = 0
        self.id = id

    def write_info(self,info):
        if (self.mem_usada == 1024):
            return False
        else:
            for i in range(len(info)):
                self.info[self.mem_usada] = info[i]
                self.mem_usada += 1
            return True

    def read_info (self):
        return self.info

    def reset_info (self):
        self.info = "\0" * 1024
        self.mem_usada = 0