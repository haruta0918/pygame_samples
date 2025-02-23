# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg

import pygame
import pygame.freetype
# import time
from lcd_font_pg_seven_seg_mc import LCD_font_mc
import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
mc =Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)

display1 = LCD_font_mc(mc)
display1.init_col(BLOCK_SIZE=5, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display1.init_row(X_ORG=8, Y_ORG=35, COL_INTV=6)
dt_now = datetime.now()
display2 = LCD_font_mc(mc)
display2.init_col(BLOCK_SIZE=5, BLOCK_INTV=6, COLOR_ON=GREEN, COLOR_OFF=DARK_GRAY)
display2.init_row(X_ORG=8, Y_ORG=20, COL_INTV=6)
dt_now = datetime.now()

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。

        mc.setblock(col=0, code=dt_now.hour // 10)
        display1.update_col(col=1, code=dt_now.hour % 10)
        display1.update_col(col=2, code=10)
        display1.update_col(col=3, code=dt_now.minute // 10)
        display1.update_col(col=4, code=dt_now.minute % 10)
        display1.update_col(col=5, code=10)
        display1.update_col(col=6, code=dt_now.second // 10)
        display1.update_col(col=7, code=dt_now.second % 10)
        display2.update_col(col=0, code=int(str(dt_now.year)[0]))
        display2.update_col(col=1, code=int(str(dt_now.year)[1]))
        display2.update_col(col=2, code=int(str(dt_now.year)[2]))
        display2.update_col(col=3, code=int(str(dt_now.year)[3]))
        display2.update_col(col=4, code=11)
        display2.update_col(col=5, code=int(str(dt_now.month)[0]))
        display2.update_col(col=6, code=11)
        display2.update_col(col=7, code=int(str(dt_now.day)[0]))
        display2.update_col(col=8, code=int(str(dt_now.day)[1]))

       
        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
