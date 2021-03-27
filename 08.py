# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:02:46 2021

@author: lucas
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
x,y,z=mc.player.getTilePos()
for i in range(50):
    for j in range(50):
        for k in range(50):
        plantTree(x+i*5,y+i*j,z+i*k)