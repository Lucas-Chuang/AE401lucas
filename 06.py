# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:13:58 2021

@author: lucas
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits) >0:
        hit=hits[0]
        x,y,z=hit.pos.x, hit.pos.y, hit.pos.z
        block=mc.getBlock(x,y,z)
        mc.postToChat("Block ID:"+str(block))
        if block==1:
            mc.setBlock(x,y,z,41)
            
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,0,"1","2","3","4")

            
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import random
import time

i=1
while i<20:
    pos=mc.player.getPos()
    x=pos.x+random.uniform(-20,20)
    y=pos.y+random.uniform(3,0)
    z=pos.z+random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.1)