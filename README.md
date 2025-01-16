# pygame_samples

 - demo_01.py: pygameの超簡単なデモ。
 - demo_02.py: 7セグのシミュレーション、各セグメントを2ブロックで構成。Seven_segクラス使用。
 - demo_LCD_font_01.py: 5x7のLCDフォント制作用。LCD_fontクラス使用。
 - demo_LCD_font.py: 5x7のLCDフォント、完成版。
 - やり方
 - ①https://github.com/Naohiro2g/dotmatrix_fontからオリジナルフォントを作る
 - ②LCD_font_pg.pyの最初の0,1,2を表示させているものを消して、
 - with open("fonts/font.txt", encoding="utf-8") as f:
        LCD_font_styles = f.read().split('\n')
   に変えて、45行目を
   if LCD_font_styles[int(code*7+y)][x] == "1":
   に変える
   ③demo_LCD_font.pyに戻り、34行目の％のところを自分の作った文字数-1に変える
   また大量に文字を作った場合には、ウィンドウの大きさを変えないと全部映らないため、17行目の値を大きくする
![2025-01-16154917-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/0a5dbc7b-a15f-4aaa-b718-6cb85f919cb7)

 - demo_freetype.py: pygame.freetypeでテキスト表示。（新しい方式）
 - demo_freetype.py: pygame.fontでテキスト表示。（古い方式）
 - demo_openmoji.py: オープンソースの絵文字、openmojiのデモ。キー操作のデモ。
 - seven_seg_pg.py: Seven_segクラス
 - lcd_font_pg.py: LCD_fontクラス
