# STEP-1-
#1-1 参照ドライブ(変数target)下の拡張子.xmlをコピー
#1-2 *** UTF-8への変換 ***
#1-3 参照先(変数save)にペースト
#1-4 tkinterWindow.pyとの接続

# * + * + * + * + * + * + * + * + * + * +

import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def translate(x,y): # tlanslate関数の宣言

    # drive = r"C:\Users\T15015\PycharmProjects\test_area\drive"
    drive = x
    print(drive)
    # save = r"C:\Users\T15015\PycharmProjects\test_area\save"
    save = y
    print(save + "\n")

    os.chdir(drive) # カレントディレクトリを走査対象に移動
    path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納

    list_max = len(path_list) # 変換するxmlファイルの総数を取得
    count = 0 # 変換終了変数countの初期化
    print("残り" + str(list_max))
    print("-*-*-*-*-*-operation_start-*-*-*-*-*-\n")

    for x in path_list: # 拡張子.xml格納リストを網羅表示
        fromdir = drive + '\\' + x # 変数fromdir::操作対象絶対パス
        print("変換対象：：" + fromdir) # ↑の表示(確認)
        y = os.path.basename(fromdir) # 変数y::操作対象のファイル名取得
        todir = save + '\\' + y # 変数todir::保存先ディレクトリの絶対パス
        print("保存先：：" + todir) # ↑の表示(確認)
        # ↓ 変換&新規出力
        ff = codecs.open(fromdir, 'r', encoding='euc-jp') # 元ファイルを読み込み
        fout_utf = open(todir, 'w', encoding='utf-8') # UTFでの新ファイルを新規作成
        for row in ff: # 元ファイルから１行ずつ読みだして
            fout_utf.write(row) # コピー先新ファイルに書き出す

        ff.close() # ffを閉じる
        fout_utf.close() # fout_utfを閉じる
        count = count + 1 # カウントアップ
        progress = round((count / list_max) * 100, 1) # 変数progress:進捗割合
        print(str(progress) + "%完了") # 小数点第一位で切り捨て

    print("\n-*-*-*-*-*-operation_end-*-*-*-*-*-")
# * + * + * + * + * + * + * + * + * + * +

# STEP-2-
#2-1 必要な情報のみを抜き出す
#2-2 カンマ区切りにして.csv化
#2-3 指定したファイル名で上書き保存
