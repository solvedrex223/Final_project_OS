
import Algorithms.FrequencyHashTable as Freq
import DataStructures.HuffmanTree as Ht
import Algorithms.InsertionSort as Is
import Algorithms.FileCompression as Fp
import Algorithms.binarizeTable as BT
filepath = "../words_alpha.txt"
freqTable = Freq.buildFreqHashTable(filepath)
freqList = []
for key in freqTable.keys(): freqList.append(Ht.HuffTree(freqTable[key], key))
del freqTable
freqList.sort(key=lambda x: x.root.freq, reverse=True)
while len(freqList)>1:
    freqList[-1].merge(freqList[-2])
    temptree = freqList[-1]
    freqList.pop()
    freqList.pop()
    freqList.append(temptree)
    Is.insertionSort(freqList)
huffTree = freqList[0]
del freqList
print(huffTree.root.freq)
compTable = huffTree.CompressionTable()
for key in compTable.keys(): print(key,compTable[key])
##compTable = BT.binarize(compTable)
for key in compTable.keys(): print(key,compTable[key])
Fp.FileCompression(filepath,compTable)
