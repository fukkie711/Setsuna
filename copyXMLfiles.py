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
from2 = r"C:\Users\T15015\PycharmProjects" # 仮のパス、接続前に削除

print("operation_start")
os.chdir(from2) # カレントディレクトリを走査対象に移動
path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納
for x in path_list: # 拡張子.xml格納リストを網羅表示
    print(from2 + '\\' + x) # カレントディレクトリと接続して表示
    # ↑ from2がディレクトリ、xがファイル名 ↑
    fin = codecs.open(x, 'r', 'euc_jp')
    fout = codecs.open(x, 'w', 'utf_8')
print("end")
# * + * + * + * + * + * + * + * + * + * +

# STEP-2-
#2-1 必要な情報のみを抜き出す
#2-2 カンマ区切りにして.csv化
#2-3 指定したファイル名で上書き保存
