# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py
# まだ あ～おまでしか作っていない
import sys
from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg
a=1234567890
import pygame
import pygame.freetype
# import time
from lcd_font_pg_seven_seg import LCD_font
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
with open("fonts/minecraft.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')
pygame.init()
screen = pygame.display.set_mode((320, 120))  # display Surfaceの生成。
pygame.display.set_caption('freetype demo')
CYAN = (120, 120, 250)

font1 = pygame.freetype.Font('fonts/natumemozi.ttf', 18)
screen.fill((250, 180, 250))
message1 = 'Letus Play Lunar-Lander game!!'


text1, rect1 = font1.render(message1, CYAN)  
print(rect1, text1.get_width(), text1.get_height(), text1.get_rect())
font1.antialiased = True  
screen.blit(text1, (20, 12))
print(a)
print(text1)


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

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
lcd1 = LCD_font(mc)
code=text1
BLOCKON=param.SMOOTH_QUATZ
Z=-7
Y=90
for y in range(7):
    Y-=1
    Z=-7
    for x in range(5):
        Z+=1
        if LCD_font_styles[int(code*7+y)][x] == "1":
                BLOCK= BLOCKON
                mc.setBlock(-40, Y,Z,BLOCK)   
                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
                


        

# infinit loop bottom ----

