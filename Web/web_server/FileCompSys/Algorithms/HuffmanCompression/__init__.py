import FileCompSys.Algorithms.FrequencyHashTable as Freq
import FileCompSys.DataStructures.HuffmanTree as Ht
import FileCompSys.Algorithms.FileCompression as Fp
import FileCompSys.Algorithms.TreeToFile as Ttf
import FileCompSys.Algorithms.TreeFromList as Tfl

#performs huffman compression algorithm.

#coded and maintained by zikln - rodrigoor1999@outlook.com

def HuffmanCompression(inode_no , filename, parent_inode):
    freqTable = Freq.buildFreqHashTable(inode_no= inode_no)
    freqList = []
    for key in freqTable.keys(): freqList.append(Ht.HuffTree(freqTable[key], key))
    del freqTable
    freqList.sort(key=lambda x: x.root.freq, reverse=True)
    Ttf.TreeToFile(freqlist = freqList, filename = filename, parent_inode= parent_inode)
    huffTree = Tfl.buildTree(freqList)
    del freqList
    compTable = huffTree.CompressionTable()
    Fp.FileCompression(inode_no,filename , compTable, parent_inode)
    return
