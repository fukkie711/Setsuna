# 参照元フォルダ（下の階層も含む）からXMLファイルを探し
# そのXMLファイルの文字コードをUTF-８に変換しながら
# 保存先フォルダにコピー

# * + * + * + * + * + * + * + * + * + * +

# STEP-1-
#1-1 参照ドライブ(変数target)下の拡張子.xmlをコピー
#1-2 *** UTF-8への変換 ***
#1-3 参照先(変数save)にペースト

# coding: utf-8
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み

#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
drive = r"C:\Users\T15015\PycharmProjects\PatentApp"
print(drive)
save = r"C:\Users\T15015\PycharmProjects\save"
print(save)
print("operation_start\n")

os.chdir(drive) # カレントディレクトリを走査対象に移動
path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納

for x in path_list: # 拡張子.xml格納リストを網羅表示
    fromdir = drive + '\\' + x # 操作対象絶対パス
    # ↑ driveがディレクトリ、xがファイル名 ↑
    print(fromdir) # ↑の表示(確認)
    y = os.path.basename(fromdir) # 操作対象のファイル名取得
    todir = save + '\\' + y # 保存先ディレクトリの絶対パス
    print(todir) # の表示(確認)
    # ↓ 変換&新規出力
    ff = codecs.open(fromdir, 'r', encoding='utf-8') # 元ファイルを読み込み
    fout_utf = open(todir, 'w', encoding='utf-8') # UTFでの新ファイルを新規作成
    for row in ff: # 元ファイルから１行ずつ読みだして
        fout_utf.write(row) # コピー先新ファイルに書き出す
    ff.close() # ffを閉じる
    fout_utf.close() # fout_utfを閉じる
print("end")
# * + * + * + * + * + * + * + * + * + * +

# STEP-2-
#2-1 必要な情報のみを抜き出す
#2-2 カンマ区切りにして.csv化
#2-3 指定したファイル名で上書き保存
