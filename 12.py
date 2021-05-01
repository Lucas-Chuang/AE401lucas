# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:11:51 2021

@author: lucas
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import choice

mineral= [14,15,16,56,74,129]

r=choice(mineral)

myID=mc.getPlayerEntityId('Guy_that_yeet')
x,y,z=mc.entity.getTilePos(myID)
mc.setBlock(x,y,z,r)

list2d =[[12,41,14],
         [35,73,86]]

x,y,z = mc.player.getTilePos()
startX=x

for list1d in list2d:
    
    for i in list1d:
        mc.setBlock(x,y,z,i)
        
        x=x+1
        
    x=startX
    z=z+1