import sys
sys.path.insert(1, 'D:/Documentos/Proyectos Uni/FP_OS/Final_project_OS/Web/web_server')
import file_system.FileSystem.Packages.Block as B
from file_system.FileSystem.Packages.Setup import set_block_list

##set_block_list()

block = B.Block(2)
block.read_info()
LBL = B.super_block(2)
LBL.load()
print(LBL.LBL)
for i in range(200):
    LBL.free_block()
print(LBL.LBL)
