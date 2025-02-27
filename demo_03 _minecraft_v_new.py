# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
# まだ あ～おまでしか作っていない
import sys
from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg

import pygame
import pygame.freetype
# import time
from lcd_font_pg_seven_seg import LCD_font
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
with open("fonts/font.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

        

pygame.init()

pygame.display.set_caption("pygame 7-segment display simulation")

dt_now = datetime.now()
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)
    mc.postToChat('kadai #ラスト  文字表示')

Z=40
Y=133
for y in range(7):
    Y-=1
    Z=40
    for x in range(5):
        Z+=1
       
        mc.setBlock(50, Y,Z,param.AIR)    
Z=30
Y=133
for y in range(7):
    Y-=1
    Z=30
    for x in range(5):
        Z+=1
       
        mc.setBlock(50, Y,Z,param.AIR)     
lcd1 = LCD_font(mc)
code=5
BLOCKON=param.SMOOTH_QUATZ
X=50
Z=40
Y=133
for y in range(7):
    Y-=1
    Z=40
    for x in range(5):
        Z+=1
        if LCD_font_styles[int(code*7+y)][x] == "1":
                BLOCK= BLOCKON
                mc.setBlock(X, Y,Z,BLOCK)
code=10
Z=30
Y=133
for y in range(7):
    Y-=1
    Z=30
    for x in range(5):
        Z+=1
        if LCD_font_styles[int(code*7+y)][x] == "1":
                BLOCK= BLOCKON
                mc.setBlock(50, Y,Z,BLOCK)      
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く


        

# infinit loop bottom ----

