class node:
    def __init__(self, freq, char = None):
        self.freq = freq
        self.left = None
        self.right = None
        self.char = char
        self.cmpValue = "" ##Compressed value
    def inLevelTraversal(self):
        if self.left:
            self.left.inLevelTraversal()
        print(self.freq, end= ",")
        if self.right:
            self.right.inLevelTraversal()
    # Returns the hufftable needed for decompresion, it is based on inlevelTraversal
    def HuffmanTable(self,hufftable):
        if self.char:
            hufftable[self.cmpValue] =  self.char
        else:
            if self.left:
                self.left.cmpValue = self.cmpValue + "0"
                self.left.HuffmanTable(hufftable)
            if self.right:
                self.right.cmpValue = self.cmpValue + "1"
                self.right.HuffmanTable(hufftable)
    def CompressionTable(self, CompTable):
        if self.char:
            CompTable[self.char] = self.cmpValue
        else:
            if self.left:
                self.left.cmpValue = self.cmpValue + "0"
                self.left.CompressionTable(CompTable)
            if self.right:
                self.right.cmpValue = self.cmpValue + "1"
                self.right.CompressionTable(CompTable)


class HuffTree:
    def __init__(self, freq, char = None):
        self.root = node(freq, char)
    def  merge(self, hufftree):
        newroot = node(self.root.freq + hufftree.root.freq)
        newroot.left = self.root
        newroot.right = hufftree.root
        self.root = newroot
    def inLevelTraversal(self):
        if self.root:
            self.root.inLevelTraversal()
        else: return False
    def HuffmanTable(self):
        # Returns the hufftable needed for decompresion
        huffTable = {}
        if self.root:
            self.root.HuffmanTable(huffTable)
            return huffTable
        else: return False
    def CompressionTable(self):
        if self.root:
            CompTable = {}
            self.root.CompressionTable(CompTable)
            return CompTable
    def toFile(self, filepath):
        #stores the tree in a file
        return True
    def FromFile(filename):
        #builds the tree from the path
        return True




###Samples
if __name__ == "__main__":
    a = HuffTree(5,"h")
    b = HuffTree(3,"s")
    c = HuffTree(1,"4")
    c.merge(b)
    c.merge(a)
    print(c.root.freq)
    c.inLevelTraversal()
    HuffmanTable = c.HuffmanTable()
    print()
    for key in HuffmanTable.keys():
        print(key, HuffmanTable[key])