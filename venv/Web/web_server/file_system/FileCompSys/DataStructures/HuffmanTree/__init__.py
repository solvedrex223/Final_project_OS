#This file contains a huffman's tree for encoding.

#coded and maintained by zikln - rodrigoor1999@outlook.com

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

    def HuffmanTable(self,hufftable):
        #Traverses the tree and add to the hash table key = char, value = binary value for compression.
        if self.char:
            hufftable[self.cmpValue] =  self.char
        else:
            if self.left:
                self.left.cmpValue =   "0" + self.cmpValue
                self.left.HuffmanTable(hufftable)
            if self.right:
                self.right.cmpValue =   "1" + self.cmpValue
                self.right.HuffmanTable(hufftable)
    def CompressionTable(self, CompTable):
        #Traverses the tree and add to the hash table key = char, value = binary value for compression.
        if self.char:
            CompTable[self.char] = self.cmpValue
        else:
            if self.left:
                self.left.cmpValue =   self.cmpValue + "0"
                self.left.CompressionTable(CompTable)
            if self.right:
                self.right.cmpValue =  self.cmpValue + "1"
                self.right.CompressionTable(CompTable)


class HuffTree:
    def __init__(self, freq, char = None):
        self.root = node(freq, char)
        return
    def  merge(self, hufftree):
        ##Merges to tree under a parent node with no char value and wich frequency is equal to the kids.
        newroot = node(self.root.freq + hufftree.root.freq)
        newroot.left = self.root
        newroot.right = hufftree.root
        self.root = newroot
        return
    def inLevelTraversal(self):
        if self.root:
            self.root.inLevelTraversal()
            return
        else: return False
    def HuffmanTable(self):
        # Returns the hufftable needed for decompresion
        huffTable = {}
        if self.root:
            self.root.HuffmanTable(huffTable)
            return huffTable
        else: return False
    def CompressionTable(self):
        #Returns compression table needed for compression
        if self.root:
            CompTable = {}
            self.root.CompressionTable(CompTable)
            return CompTable
        return False





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