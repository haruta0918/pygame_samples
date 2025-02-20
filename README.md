# pygame_samples

 - demo_01.py: pygameの超簡単なデモ。
 - demo_02.py: 7セグのシミュレーション、各セグメントを2ブロックで構成。Seven_segクラス使用。
 -  ![スクリーンショット 2025-01-16 182647](https://github.com/user-attachments/assets/01e49458-5eaf-4e9f-a5c4-5ff23854cd5c)
 - demo_03.py: LCD_fontsを使用した、時計(時間のほかに、年月日を表示)
 - ![スクリーンショット 2025-01-16 182742](https://github.com/user-attachments/assets/3ae9dd7e-4fff-4466-adef-4d31b9a83a8d)
 - demo_LCD_font_01.py: 5x7のLCDフォント制作用。LCD_fontクラス使用。 -
 - demo_LCD_font.py: 5x7のLCDフォント、完成版。
 - どうやってやったか
 - ①https://github.com/Naohiro2g/dotmatrix_font    からオリジナルフォントを作る
 - ②fontsの中に出来上がったfont.txtを入れる
 - ③LCD_font_pg.pyの最初の0,1,2を表示させているものを消して、
 - with open("fonts/font.txt", encoding="utf-8") as f:
 - LCD_font_styles = f.read().split('\n')
 - に変える　そして45行目を
 - if LCD_font_styles[int(code*7+y)][x] == "1":
 - に変える
 - ④demo_LCD_font.pyに戻り、34行目の％のところを自分の作った文字数-1に変える
 - また大量に文字を作った場合には、ウィンドウの大きさを変えないと全部映らないため、17行目の値を大きくする(1500くらいまでがおすすめ)
        
![2025-01-16154917-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/0a5dbc7b-a15f-4aaa-b718-6cb85f919cb7)

 - demo_freetype.py: pygame.freetypeでテキスト表示。（新しい方式）
 - どうやってやったか
 - <フォントを変えたいとき>
 - ・fontsフォルダーの中に、自分の使いたいフォントのttfファイルを入れて、32,33行目にある、メッセージ1とメッセージ2のフォントを指定しているところで、fonts/○○(ファイル名)○○(文字の大きさ指定)に変える
 - <内容を変えたいとき>
 - ・36行目と49行目に書いてある赤文字になっているところを表示させたい文字に変える
 - ![スクリーンショット 2025-01-16 174146](https://github.com/user-attachments/assets/28d3a725-dad9-4b76-ad92-94748193b360)
 - demo_freetype.py: pygame.fontでテキスト表示。（古い方式）

 - demo_openmoji.py: オープンソースの絵文字、openmojiのデモ。キー操作のデモ。
 - seven_seg_pg.py: Seven_segクラス
 - demo_02.pyやdemo_03.py用のファイル
 - lcd_font_pg.py: LCD_fontクラス
 - demo_LCD_font.pyのためのファイル
 - 表示するときのフォントのttfファイルを参照をしたりするファイル
 - ＜demo_LCD_font.pyやdemo_03.pyのマインクラフトでの表示＞
 - 時計バージョン
 - ①マインクラフトで表示するのは数字だけのため、使うフォントを
 - with open("fonts/font_sevnseg.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')
   で,sevnseg.txtにする
   ②import sys
   from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
がマイクラリモコンに必要なため、すべて、1番最初ところに入れる
③mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)
    mc.postToChat('kadai #8  時計(完成)')
   を入れることで、マイクラリモコン(mc)の定義や、チャット欄にkadai #8  時計(完成)が表示される
   その後、X=-48
Y=121
for y in range(9):
            Y-=1
            X=-48
            for x in range(49):
                X+=1
                mc.setBlock(X, Y,-8,param.SMOOTH_QUATZ) 

X=-49
Y=122
for y in range(11):
            Y-=1
            X=-49
            for x in range(51):
                X+=1
                mc.setBlock(X, Y,-7,param.DIAMOND_BLOCK)
 で、背景を作り、
 display1.update_col(col=0, code=dt_now.hour // 10)
        display1.update_col(col=1, code=dt_now.hour % 10)
        display1.update_col(col=2, code=10)
        display1.update_col(col=3, code=dt_now.minute // 10)
        display1.update_col(col=4, code=dt_now.minute % 10)
        display1.update_col(col=5, code=10)
        display1.update_col(col=6, code=dt_now.second // 10)
        display1.update_col(col=7, code=dt_now.second % 10)
        で時、分、秒が更新されているので、更新したものを常に出せるように、
        Y=120
        X=-5
        print(code)
        # 秒
        code=dt_now.second % 10
        X=-5
        Y=120
        for y in range(7):
            Y-=1
            X=-5
            for x in range(5):
                X+=1
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    BLOCK= BLOCKON
                    mc.setBlock(X, Y,-7,BLOCK)   
                else:
                    BLOCK= BLOCKOFF
                    これは、秒数の一の位だけだが、これを、他すべてでも行い、毎回変更できるように、すべての範囲を
                    X=-48
        Y=121
        for y in range(9):
                    Y-=1
                    X=-48
                    for x in range(49):
                        X+=1
                        mc.setBlock(X, Y,-7,param.AIR) で消している
   

 - 文字バージョン
 - 今のままだと表示する文字が数字のみなので、with open のところをオリジナルのひらがなファイルを作るか、LCDfontで使ったfont_txtに変え、必要最低限のコードだけにするために、
 - BLOCKON=param.SMOOTH_QUATZ
X=47
Y=120
for y in range(7):
    Y-=1
    X=47
    for x in range(5):
        X+=1
        if LCD_font_styles[int(code*7+y)][x] == "1":
                BLOCK= BLOCKON
                mc.setBlock(X, Y,-7,BLOCK)
   みたいに、文字を表示する部分と、表示する文字を指定する
   code=
   のところと、インポートやフォントを開いている上17行、mcの定義をしている
   mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)
    mc.postToChat('kadai #ラスト  文字表示')
lcd1 = LCD_font(mc)
   のあたりだけ残して、他をすべて消す
   code指定と、文字の表示するところの座標を変えれば、文章も作ることができる
