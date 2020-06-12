#Takes a pathfile and a hash table that contains key == char value == binary as str
#runs to every bit of the file
#when 8 ar stored tansforms the binary into a byte and writes it in the comppressed file
#If bitss are leftover their are given each the highest bit denomination available  and converted to int
#ie 0b101 = 0b10100000 = 128+32 = 160 and writes the corresponding byte.
#returns nothing.

#coded and maintained by zikln - rodrigoor1999@outlook.com

def FileCompression(filepath, Comptable):
    power = 7
    binary = None

    file = open(filepath, "r")
    content = file.read()
    file.close()

    newfilepath = filepath + "cmp"
    newfile = open(newfilepath, "wb")

    for char in content:
        for bit in Comptable[char]:
            if power == -1:
                power = 7
                newfile.write(bytes([binary]))
                binary = None
            if binary == None:
                binary = (2 ** power)  * int(bit)
            else:
                binary += (2 ** power)  * int(bit)
            power -= 1

    if binary:
        newfile.write(bytes([binary]))
    newfile.close()
    return



