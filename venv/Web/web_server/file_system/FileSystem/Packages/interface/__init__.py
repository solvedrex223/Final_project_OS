import sys

string = sys.path[0]
string = string.split("/")
while string[len(string) - 1] != "web_server":
    string.pop()
for i in range(len(string) - 1):
    string[i]+= "/"
r_sys = "".join(string)
sys.path.insert(1, r_sys)

from file_system.FileSystem.Packages.file_functions import *
from file_system.FileSystem.Packages.dir_functions import *
from file_system.FileSystem.Packages.Block import *
from file_system.FileSystem.Packages.Inode import *
from file_system.FileCompSys.Calls import *
ruta = ''
cwd = Inode(id= 2)
past_rt = []
def lexo(command,user,data):
    global ruta
    global cwd
    cwd.read()
    ipt = command
    if len(ipt) >= 2 and ipt[1] == 'ls':
        try:
            if ipt [2]:
                return [ls_format(ls(cwd,ipt[2])),ruta]
            else:
                return [ls_format(ls(cwd)),ruta]
        except:
            return [ls_format(ls(cwd)),ruta]
    elif len(ipt) == 3 and ipt[1] == 'cd':
        dest = ipt[2]
        wd = cwd.id
        cwd = cd(dest,find_files(cwd))
        if (cwd.id == wd):
            for i in range(len(past_rt)):
                    ruta = ''
                    if i == 0:
                        ruta += past_rt[i]
                    else:    
                        ruta += "/" + past_rt[i]
            return["No es una ruta valida\n",ruta]
        else:
            if (dest == ".."):
                if user != "admin" and cwd.id == 2:
                    cwd = Inode(wd)
                    ruta = ''
                    for i in range(len(past_rt)):
                        if i == 0:
                            ruta += past_rt[i]
                        else:    
                            ruta += "/" + past_rt[i]
                    return ["No tienes permiso para acceder a ese directorio\n",ruta]
                elif (len(past_rt) == 0):
                    ruta = ''
                    return [ruta]
                else:
                    ruta = ''
                    past_rt.pop(len(past_rt) - 1)
                    for i in range(len(past_rt)):
                        if i == 0:
                            ruta += past_rt[i]
                        else:    
                            ruta += "/" + past_rt[i]
                    return[ruta]  
            else:
                try:
                    if past_rt[len(past_rt) - 1] == 'home' and user != 'admin' and dest != user:
                        cwd = Inode(wd)
                        ruta = ''
                        for i in range(len(past_rt)):
                            if i == 0:
                                ruta += past_rt[i]
                            else:    
                                ruta += "/" + past_rt[i]
                        return["No tienes permiso para acceder a ese directorio\n",ruta]
                    else:
                        ruta = ''
                        past_rt.append(dest)
                        for i in range(len(past_rt)):
                            if i == 0:
                                ruta += past_rt[i]
                            else:    
                                ruta += "/" + past_rt[i]
                        return [ruta]
                except:
                    ruta = ''
                    past_rt.append(dest)
                    for i in range(len(past_rt)):
                        if i == 0:
                            ruta += past_rt[i]
                        else:    
                            ruta += "/" + past_rt[i]
                    return [ruta]
    elif len(ipt) == 3 and ipt[1] == 'mkdir':
        dest = ipt[2]
        mkdir(dest, cwd)
        return [ruta]

    elif len(ipt) == 3 and ipt[1] == 'mkfile':
        dest = ipt[2]
        mk_file(0, data,dest,cwd.id)
        return [ruta]
            
    elif len(ipt) == 3 and ipt[1] == 'rm':
        dest = ipt[2]
        rm(rm_from_dir(dest,cwd))
        return [ruta]
    elif len(ipt) == 3 and ipt[1] == 'rmdir':
        dest = ipt[2]
        rm(rm_from_dir(dest,cwd))
        return [ruta]
    elif len(ipt) == 3 and ipt[1] == 'cat':
        dest = ipt[2]
        files =  find_files(cwd)
        if files.get(dest, False):
            return [cat(files[dest]) + "\n",ruta]
        else:
            return ["File not Found...\n",ruta]
            
    elif len(ipt) > 2 and ipt[1] == 'cmp':
        if len(ipt) == 3:
            cmp(filename= ipt[2],parent_inode_no= cwd.id,new_name="")
            return [ruta]
        elif len(ipt) == 4:
            cmp(filename=ipt[2], parent_inode_no=cwd.id, new_name=ipt[3])
            return [ruta]
        else:
            return ["File doesn't exist or more than 2 args for cmp\n",ruta]
    elif len(ipt) > 2 and ipt[1] == 'dcmp':
        if len(ipt) == 4:
            dcmp(file_name=ipt[2],cwd = cwd, new_file_name=ipt[3])
            return [ruta]
        else:
            return("File doesn't exist or more than 2 args for dcmp\n" + ruta)
    elif len(ipt) > 3 and ipt[1] == 'mv':
        if len(ipt) == 4:
            mv(cwd = cwd,filename=ipt[2], dest=ipt[3])
            return [ruta]
        else:
            mv(cwd=cwd, filename=ipt[2], dest=ipt[3], dest_name = ipt[4])
            return [ruta]
    elif ipt[0] == "log_out" and data == True:
        while cwd.id != 2:
            cwd = cd('..',find_files(cwd))
            past_rt.pop(len(past_rt) - 1)
        return [True]
    else:
        return [ruta]

if __name__ == "__main__":
    pass