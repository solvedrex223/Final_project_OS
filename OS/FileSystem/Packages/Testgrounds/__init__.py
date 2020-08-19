import Packages.Block as B
from Packages.Setup import set_block_list

##set_block_list()

block = B.Block(2)
block.read_info()
LBL = B.super_block(2)
LBL.load()
print(LBL.LBL)
for i in range(200):
    LBL.free_block()
print(LBL.LBL)
