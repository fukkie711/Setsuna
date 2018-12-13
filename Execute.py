# Execute.py

# 本モジュールは、機能α、機能βに対してアドレスを指示する本アプリのメインモジュールである。
# 本モジュールにより、進捗状況を示すパラメータ[progress]をtkinterWindows.pyに受け渡す(return)。

# ＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊
# [モジュール読み込み]
import os,sys,tkinter,time # os,sys,tkinterモジュール読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
# from copyXMLfiles import translate # translate関数を読み込み
from tkinter.constants import *
import csv
from Function import Function_A, Function_B

# [宣言部]


# [メインコード]
def translate_exe(drive, drive_add, save_add): # translate_exeの開始 # drive_add::演算する.xml # save_add::保存先のディレクトリ
    todir = ""
    to_dir = Function_A(drive, drive_add, save_add) # ＥＵＣ－ＪＰへのエンコードを行う。
    print(to_dir)
    print(save_add)
    Function_B(save_add, todir) # 情報の抜き取りを行い、CSVに書き出す。読み込み先も保存先も同じなので引数は１つ # todir ：： エンコード後の新xmlの絶対パス
    return
# ＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊
