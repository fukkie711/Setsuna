
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def create_xml_list(xxx): # create_xml_list関数：：
    drive = xxx
    os.chdir(drive) # カレントディレクトリを走査対象に移動
    path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納
    list_max = len(path_list) # 変換するxmlファイルの総数を取得
    return path_list, list_max # リスト[path_list]と総数list_maxを返す

def Function_A(drive, drive_add, save_add):
    fromdir = drive + '\\' + drive_add # 変数fromdir::操作対象絶対パス
    y = os.path.basename(fromdir) # 変数y::操作対象のファイル名取得
    todir = save_add + '\\' + y # 変数todir::保存先ディレクトリの絶対パス
    ff = codecs.open(fromdir, 'r', encoding='euc-jp') # 元ファイルを読み込み
    fout_utf = open(todir, 'w', encoding='utf-8') # UTFでの新ファイルを新規作成
    for row in ff: # 元ファイルから１行ずつ読みだして
        row = row.replace('<?xml version="1.0" encoding="EUC-JP"?>', '') # 一行目
        fout_utf.write(row) # コピー先新ファイルに書き出す
    ff.close() # ffを閉じる
    fout_utf.close() # fout_utfを閉じる
    return todir

def Function_B(xml_path):
    print(xml_path)






    return
