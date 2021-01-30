# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:44:33 2021

@author: lucas
"""
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(5)
x,y,z = mc.player.getTilePos()

mc.setBlock(x-1,y,z,202)
mc.setBlock(x+1,y,z,202)
mc.setBlock(x,y,z-1,202)
mc.setBlock(x,y,z+1,202)
mc.setBlock(x+1,y,z+1,202)
mc.setBlock(x-1,y,z+1,202)
mc.setBlock(x+1,y,z-1,202)
mc.setBlock(x-1,y,z-1,202)

mc.setBlocks (x+50,y-50,z+50,x-50,y+50,z-50,0)