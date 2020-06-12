import Algorithms.FileToTree as Ftt

#Inputs File
#1Rebuilds the hufftre from file,
#2 takes the compressed file, reads it as integers, transforms it to a binary string,
#3 Then uses the string to traverse the tree.
#4 when finds a char writes it out in the uncompressed file, and returns to the root of the tree.
#output none, but writes the uncommpressed file.

#coded and maintained by zikln - rodrigoor1999@outlook.com


def FileDecompression(filepath):
    huffTree = Ftt.fileToTree(filepath[:-3]+"tree")
    file = open(filepath, "rb")
    node = huffTree.root
    newfile = open(filepath[:-3]+"dcmp", "w")
    for line in file.readlines():
        for num in line:
            binary = "{:08b}".format(num)
            for bit in binary:
                if bit == "0":
                    node = node.left
                else:
                    node = node.right
                if node.char:
                    if node.freq > 0:
                        newfile.write(node.char)
                        node.freq -= 1
                    node = huffTree.root
    newfile.close()
    file.close()
    return

if __name__ == "__main__":
    filepath = "../words_alpha.txt"
    FileDecompression(filepath+"cmp")



