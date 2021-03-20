# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:12:08 2021

@author: lucas
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z,=mc.player.getTilePos()

for i in range(10):
    mc.setBlock(x,y-1,z+i,1)
    
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z,=mc.player.getTilePos()

for i in range(10):
    mc.setBlocks(x+i,y-1,z+i,x+i,y-1,z+i+3,1)

mc.setBlocks(x-3,y+3,z-3,x+3,y+50,z+3,46)
mc.setBlocks(x,y,z,x,y+50,z,17)