# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

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
with open("fonts/font_sevnseg.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

        

pygame.init()

clock = pygame.time.Clock()
FPS=1
screen = pygame.display.set_mode([900, 500])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)


display1 = LCD_font(screen)
display1.init_col(BLOCK_SIZE=5, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display1.init_row(X_ORG=8, Y_ORG=35, COL_INTV=6)
dt_now = datetime.now()
display2 = LCD_font(screen)
display2.init_col(BLOCK_SIZE=5, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display2.init_row(X_ORG=8, Y_ORG=20, COL_INTV=6)
dt_now = datetime.now()
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)
    mc.postToChat('kadai #8  時計(完成)')
lcd1 = LCD_font(mc)
def LCD_display(x):
    code = int((x / 8) % 9)
    lcd1.update_col(col=1, code=code)
Z=-24
Y=148
for y in range(9):
            Y-=1
            Z=-24
            for x in range(49):
                Z+=1
                mc.setBlock(48, Y,Z,param.SMOOTH_QUATZ) 

Z=-25
Y=149
for y in range(11):
            Y-=1
            Z=-25
            for x in range(51):
                Z+=1
                mc.setBlock(47, Y,Z,param.DIAMOND_BLOCK)   
    
# infinite loop top ----
running = True
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
           
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。
    # LCD sim
        code=dt_now.second

        display1.update_col(col=0, code=dt_now.hour // 10)
        display1.update_col(col=1, code=dt_now.hour % 10)
        display1.update_col(col=2, code=10)
        display1.update_col(col=3, code=dt_now.minute // 10)
        display1.update_col(col=4, code=dt_now.minute % 10)
        display1.update_col(col=5, code=10)
        display1.update_col(col=6, code=dt_now.second // 10)
        display1.update_col(col=7, code=dt_now.second % 10)
        Z=-24
        Y=148
        for y in range(9):
                    Y-=1
                    Z=-24
                    for x in range(49):
                        Z+=1
                        mc.setBlock(47, Y,Z,param.AIR) 
        BLOCKOFF=param.AIR
        BLOCKON=param.SEA_LANTERN_BLOCK
        BLOCK_INTV=1
        Y=146
        Z=19
        print(code)
        # 秒
        code=dt_now.second % 10
        Z=19
        Y=147
        for y in range(7):
            Y-=1
            Z=19
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
        code=dt_now.second // 10
        Z=13
        Y=147
        for y in range(7):
            Y-=1
            Z=13
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
        code=10
        Z=7
        Y=147
        for y in range(7):
            Y-=1
            Z=7
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                    # 分 
        code=dt_now.minute % 10
        Z=1
        Y=147
        for y in range(7):
            Y-=1
            Z=1
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
        code=dt_now.minute // 10  
        Z=-5
        Y=147
        for y in range(7):
            Y-=1
            Z=-5
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
        code=10
        Z=-11
        Y=147
        for y in range(7):
            Y-=1
            Z=-11
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                    # 時
        code=dt_now.hour % 10 
        Z=-17
        Y=147
        for y in range(7):
            Y-=1
            Z=-17
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
        code=dt_now.hour // 10
        Z=-23
        Y=147
        for y in range(7):
            Y-=1
            Z=-23
            for x in range(5):
                Z+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(47, Y,Z,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く

                     
        display2.update_col(col=0, code=int(str(dt_now.year)[0]))
        display2.update_col(col=1, code=int(str(dt_now.year)[1]))
        display2.update_col(col=2, code=int(str(dt_now.year)[2]))
        display2.update_col(col=3, code=int(str(dt_now.year)[3]))
        display2.update_col(col=4, code=11)
        display2.update_col(col=5, code=int(str(dt_now.month)[0]))
        display2.update_col(col=6, code=11)
        display2.update_col(col=7, code=int(str(dt_now.day)[0]))
        display2.update_col(col=8, code=int(str(dt_now.day)[1]))  
        Z+=1
        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        

        pygame.display.flip()  # update_col
        clock.tick(FPS)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----