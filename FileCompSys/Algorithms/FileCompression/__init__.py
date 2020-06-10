def FileCompression(filepath, Comptable):
    file = open(filepath, "r")
    newfilepath = filepath + "cmp"
    content = file.read()
    newfile = open(newfilepath, "w")
    for char in content:
        newfile.write(Comptable[char])
    file.close()
    return



