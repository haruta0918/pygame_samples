# demo for text display by freetype
# pygame.freetype module is a replacement for pygame.font
# for loading and rendering fonts.
# freefontは、fontを置き換えるもの。こっちを使いましょう。

import pygame
import pygame.freetype


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()
screen = pygame.display.set_mode((320, 120))  # display Surfaceの生成。
pygame.display.set_caption('freetype demo')

# font1: Fontオブジェクト。指定文字サイズで全文字のビットマップデータをレンダリングして作成。
# text1: Surfaceオブジェクト。Fontオブジェクトから必要な文字のビットマップデータを切り出して作成。
# screen: display Surfaceオブジェクト。ウィンドウになる。
# font1から、text1を作り(render)、screenに複写(blit)する。


# フォントファイルを指定する場合
# font1 = pygame.freetype.Font('hack-fonts/Hack-Regular.ttf', 36)
# システムにインストールされているフォントの名前を指定する場合
# font1 = pygame.freetype.SysFont('natume', 18)
font1 = pygame.freetype.Font('fonts/natumemozi.ttf', 18)
font2 = pygame.freetype.Font('fonts/hack-fonts/Hack-Bold.ttf', 24)

screen.fill((250, 180, 250))
message1 = 'Letus Play Lunar-Lander game!!'


# text_surfaceにrenderしてから、blitする方法
# （テキストオブジェクト(Surface)に対して追加で行う処理がある場合など。）
# text1, rect1 = font1.render('Hello World!', (0, 0, 0))  # rect1は使わないので読み捨て。
text1, rect1 = font1.render(message1, CYAN)  # rect1は使わないので読み捨て。
print(rect1, text1.get_width(), text1.get_height(), text1.get_rect())
font1.antialiased = True  # アンチエイリアスを行う。（指定しなくても、デフォルト設定はTrue）
screen.blit(text1, (20, 12))

# スクリーンに直接render_toする方法
font2.antialiased = False  # アンチエイリアス、文字の平滑化は行わない。
font2.render_to(screen, (20, 48), 'How are you today?', (0, 0, 0))

# レンダリングされた結果を反映
pygame.display.flip()

# 何もしない無限ループ。ctrl-cやウィンドウを閉じたときの終了処理のみ。
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
