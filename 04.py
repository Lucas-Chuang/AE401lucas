# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:15:45 2021

@author: lucas
"""




from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()
width=10
height=6
lenght=5


mc.setBlocks(x,y,z, x+width, y+height,z+lenght,57)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+lenght-1, 0)

while True:
    x,y,z=mc.player.getTilePos()
    
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x-1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x,y-1,z-1)
    
    if a ==8 or a == 9 or b==8 or b==9 or c == 8 or c == 9 or d ==8 or d==9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1, 020)
        
        
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getPos()
    mc.setBlocks(x,y,z)
    time.sleep(0.2)