#Used for testing if file 1 == file2 prints true

#coded and maintained by zikln - rodrigoor1999@outlook.com

if __name__ == "__main__":
    noncomp = open("../words_alpha.txt", "r")
    comp = open("../words_alpha.txtdcmp", "r")
    content1 = noncomp.read()
    content2 = comp.read()
    print(content1 == content2)