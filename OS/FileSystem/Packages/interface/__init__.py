from Packages.file_functions import *
from Packages.dir_functions import *
from Packages.Block import *
from Packages.Inode import *





def lexo():
    ruta = '/'
    user = 'root'
    cwd = Inode(id= 2)
    cwd.read()
    files = find_files(cwd)

    while (1):
        ipt = input(user+":~"+ruta+"$")
        ipt = ipt.split()
        if len(ipt) == 1 and ipt[0] == 'ls':
            print(ls(cwd))
        elif len(ipt) == 2 and ipt[0] == 'cd':
            dest = ipt[1]
            cwd = cd(dest,find_files(cwd))
            pass
        elif len(ipt) == 2 and ipt[0] == 'mkdir':
            dest = ipt[1]
            mkdir(dest, cwd)
            pass
        elif len(ipt) == 2 and ipt[0] == 'mkfile':
            dest = ipt[1]
            print("write *q + [enter] to end the file")
            content = ''
            while(True):
                newline = input()
                if newline == '*q':
                    break
                else:
                    content += newline + '\n'
            mk_file(0, content,dest,cwd.id)
            pass
        elif len(ipt) == 2 and ipt[0] == 'rm':
            dest = ipt[1]
            rm(rm_from_dir(dest,cwd))
        elif len(ipt) == 2 and ipt[0] == 'rmdir':
            dest = ipt[1]
            rm(rm_from_dir(dest,cwd))
        elif len(ipt) == 2 and ipt[0] == 'cat':
            dest = ipt[1]
            files =  find_files(cwd)
            if files.get(dest, False):
                print(cat(files[dest]))
            else:
                print("File not Found...")
            pass
        else:
            pass
if __name__ == "__main__":
    lexo()