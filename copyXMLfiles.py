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

# from2 = 'r' + target # 接続前に有効化
drive = r"C:\Users\T15015\PycharmProjects\PatentApp"
print(drive)
save = r"C:\Users\T15015\PycharmProjects\save"
print(save)
print("operation_start\n")

os.chdir(drive) # カレントディレクトリを走査対象に移動
path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納
for x in path_list: # 拡張子.xml格納リストを網羅表示
    fromdir = drive + '\\' + x
    # ↑ driveがディレクトリ、xがファイル名 ↑
    print(fromdir) # カレントディレクトリと接続して表示(絶対パス)
    # open(from2 + '\\' + x, 'r', 'utf_8')
    #file = open(fromdir, 'r', 'utf_8')
    #file.write
    fin = codecs.open(fromdir, 'r', 'euc_jp')
    fout = codecs.open(fromdir, 'a', 'utf_8')
    #print(%d"変換" fromdir)
print("end")
# * + * + * + * + * + * + * + * + * + * +

# STEP-2-
#2-1 必要な情報のみを抜き出す
#2-2 カンマ区切りにして.csv化
#2-3 指定したファイル名で上書き保存
