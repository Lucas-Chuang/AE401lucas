# -*- coding: utf-(8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x=100
y=69
z=100

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0

while True:
    t=t+1
    mc.postToChat(str(t)+'times')
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True :
    x,y,z=mc.player.getTilePos()
    mc.PostToChat("x:"+str(x)+"y:"+str(y)+"z:"+str(z))
    