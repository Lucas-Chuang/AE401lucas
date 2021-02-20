# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:10:22 2021

@author: lucas
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()


try:
    a=int(input('enter your block:'))
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,a)

except:
    print('plz enter number')
  
    
name=input('enter your name:')
message=input('enter your message')
mc.postToChat("<"+name+">"+message)