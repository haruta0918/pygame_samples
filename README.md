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
 - demo_02.pyやdemo_03.py用のファイル - 
 - lcd_font_pg.py: LCD_fontクラス
 - demo_LCD_font.pyのためのファイル
 - 表示するときのフォントのttfファイルを参照をしたりするファイル
 - ＜demo_LCD_font.pyやdemo_03.pyのマインクラフトでの表示＞
 - 時計バージョン(demo_03_minecraft.py)
 -![無題の動画 ‐ Clipchampで作成 (1)](https://github.com/user-attachments/assets/3ff12523-9cda-4a5e-912c-a066b8d0adf2)
 - pygameで表示していたものをminecrftでも表示させるために、minecraft_remote_itkidsからparam.MCJE.pyとmc(マイクラリモコン)の定義と、最低限のインポートを、マイクラリモコンで、ブロックを一つ置くものから取ってくる
 - また、pygameで時刻をcodeにあてはめているのが
 -'''
 -   display1.update_col(col=0, code=dt_now.hour // 10)
 -  で、それを、ドットで表示させる部分は、lcd_font.pg.pyにある
 -  ''' for y in range(7):
            for x in range(5):
                if LCD_font_styles[int(code*7+y)][x] == "1":
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
 -  でこれをマインクラフトで表示させるには、colorのところを、setblockにかえて、ブロック名と、座標にする(XYZの変数を作って、変化させることで、5×7を作る)
 -  またこれだと、ブロックが消えないので、elseのところにも同じものを作って、ブロックをparam.AIRにすると、いらないところだけ、消すことができる
 -  文字バージョン(demo_03 _minecraft_v_new.py)
 -  基本的に、時計と同じ
 -  ただ、今のままだと表示する文字が数字のみなので、with open のところをオリジナルのひらがなファイルを作るか、LCDfontで使ったfont_txtに変え、時刻をcodeにしているところなどがいらない
 -  そのため、必要最低限の、インポート系、mc定義、setblockと一応postChatのところだけ残す
 -  このままだと、codeが何も指定されていないので、
 -  '''
 -  disp_msg = "2DJMV389"
 -  i = 0
 -  msg=(ord(disp_msg[i]))
 -  code = msg
 -  のように、文字をASCIIに変換して、それをcodeにすることで、マイクラでも表示したい文字が表示できる
 -  ただし、このままだと、codeに一番最初の文字しか、入らないので、
 -  最初にcount=1にして、繰り返す回数をcountにすることで、それぞれにあった、ASCIIのcodeになり、最終的に、
 -  '''
 -Z=45
Y=133
X=50
Yorizin=Y
Zorizin=Z
Xorizin=X
BLOCKON=param.SMOOTH_QUATZ
count=0
for i in range (len(disp_msg)):
    count+=1
    for i in range(count):
        msg=(ord(disp_msg[i]))
    code = msg
    Z=Zorizin
    X=Xorizin
    Y=Yorizin
    for y in range(7):
        Y-=1
        Z=Zorizin
        for x in range(5):
            Z-=1
            if LCD_font_styles[int(code*7+y)][x] == "1":
                BLOCK = BLOCKON
                mc.setBlock(X, Y,Z,BLOCK)
            else :
                BLOCK =BLOCKOFF
                mc.setBlock(X, Y,Z,BLOCK)

                # 桁の原点
                # ドットの原点座標
                
                # ドットを描く
    Zorizin-=9
 -  
 -                  
 -                  になった
    
 
                    
                        
 -                  


           


        
        
    
   
   
   
    
    
        
    



 

 
   

  
  
   
 
  - 
