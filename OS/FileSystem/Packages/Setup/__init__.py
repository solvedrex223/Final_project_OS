import os
def set_hard_drive(dir_path = "/home/zikin/Documents/Final_project_OS/hard_drive"):
    try:
        print(True)
        os.mkdir(dir_path)
    except:
        Exception
        print("error")
    placeholder = chr(0) * 1024
    for i in range(1, 1000001):
        print(i)
        file = open("/home/zikin/Documents/Final_project_OS/hard_drive/"+str(i)+".block","w")
        file.write(placeholder)
        file.close()
    return True

print("ok")

set_hard_drive()