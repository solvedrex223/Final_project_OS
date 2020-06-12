import Algorithms.FrequencyHashTable as Freq
import DataStructures.HuffmanTree as Ht
import Algorithms.FileCompression as Fp
import Algorithms.TreeToFile as Ttf
import Algorithms.TreeFromList as Tfl

#performs huffman compression algorithm.

#coded and maintained by zikln - rodrigoor1999@outlook.com

def HuffmanCompression(filepath):
    freqTable = Freq.buildFreqHashTable(filepath)
    freqList = []
    for key in freqTable.keys(): freqList.append(Ht.HuffTree(freqTable[key], key))
    del freqTable
    freqList.sort(key=lambda x: x.root.freq, reverse=True)
    Ttf.TreeToFile(freqList,filepath)
    huffTree = Tfl.buildTree(freqList)
    del freqList
    compTable = huffTree.CompressionTable()
    Fp.FileCompression(filepath,compTable)
    return

if __name__ == "__main__":
    filepath = "../words_alpha.txt"
    HuffmanCompression(filepath)