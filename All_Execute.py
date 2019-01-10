import os,sys,tkinter,time, csv # os,sys,tkinterモジュール読み込み
from tkinter import * # tkinter全ロード
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from tkinter.constants import *
from All_Function import create_xml_list, Function_A, Function_B
from time import *
import random

# [宣言部]
list_csv = []
progress = 0

# 参照ボタンのイベント
# reference_bクリック時の処理
filepath1 = "" # filepath1変数の初期化
filepath2 = "" # filepath2変数の初期化
def reference_b_clicked(): # reference_b_clickedの関数を定義
    fTyp = [("","*")] # 表示オプション
    filepath1 = tkinter.filedialog.askdirectory() # directoryを選択する
    file1.set(filepath1) # filepath1をsetに変換する
    return filepath1 # filepath1に返す

# strage_bクリック時の処理(保存ボタンの挙動)
def strage_b_clicked(): # strage_b_clickedの関数を定義
    fTyp = [("","*")] #表示オプション
    filepath2 = tkinter.filedialog.askdirectory() # directoryを選択する
    file2.set(filepath2) # filepath2をsetに変換する
    return filepath2 # filepath2に返す

# end_bクリック時の処理（終了ボタン）
def end_b_clicked(): # end_b_clickedの関数を定義
    if messagebox.askyesno('確認ダイアログ', u'本当に終了しますか？'): # 確認ダイアログ
        quit() # アプリの強制終了
    else:
        pass # 何もしない

# start_bクリック時の処理 (開始ボタン)
def start_b_clicked(): # start_b_clickedの関数を定義
    sss = r"" + file1.get() + ""# 参照先ディレクトリの絶対パス
    fff = r"" + file2.get() + ""# 保存先ディレクトリの絶対パス
    complete_file = 0
    list_max = 0
    path_list = []
    # xmlアドレス抽出部
    path_list, list_max = create_xml_list(sss) # 対象ドライブからxmlファイルの絶対パスを再帰的検索する関数。リストと総数を返す。
    print("総数：：" + str(list_max))
    # エンコード&情報抽出、進捗割合変数演算部
    while complete_file <= list_max - 1: # list_max以下であればループ
        ope_file = path_list[complete_file] # 次の演算予定のファイルアドレスが格納されているリスト番号を読み出し
        absolute = Function_A(sss, ope_file, fff)
        Function_B(fff, absolute)
        complete_file = complete_file + 1
        progress = round((complete_file / list_max) * 100, 1)
        print(str(progress) + "%完了") # テスト用コード
        progress_bar.configure(value=progress)
        show.configure(text= (str(progress) + "%完了"))
        progress_bar.update()
        show.update()
if __name__ == '__main__': # 該当のスクリプトファイルがコマンドラインから実行された場合
    # rootの作成
    root = Tk() # 実行内容の処理の開始位置
    root.title('抽出プログラム') # ウインドウのタイトル
    root.geometry("550x200+450+250") # ウインドウのサイズ

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10) # windowの枠組み
    frame1.grid(row=0,column=0,stick=(S)) # 枠組みの配置

    frame3 = ttk.Frame(root, padding=10) # windowの枠組み
    frame3.grid(row=1,column=0) # 枠組みの配置

    frameP= ttk.Frame(root, padding=10)
    frameP.grid(sticky=(W,E))
    frameP.columnconfigure(0, weight=1)
    frameP.rowconfigure(0, weight=1)

    framePB = ttk.Frame(root, padding = 10)
    framePB.grid(sticky = (W,E))
    framePB.columnconfigure(0, weight = 1)
    framePB.rowconfigure(0, weight = 1)

    # プログレスバー(determinate_mode)
    progress_bar = ttk.Progressbar(
        frameP,
        orient=HORIZONTAL,
        length=400,
        mode='determinate')
    progress_bar.configure(maximum=100, value=progress)
    progress_bar.grid(row=1, column=0, sticky=(N,E,S,W))

    # 進捗割合ラベル
    show = tkinter.Label(text="0%完了")
    show.place(x=471, y=132)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10) # widgetをグループ化
    frame2.grid(sticky=(N,W,S,E)) # 配置指定

    # 《参照》選択ボタンの作成
    reference_b = ttk.Button(root, text=u'参照', command=reference_b_clicked) # ボタン処理
    #reference_b.grid(row=0, column=3) # ボタンの配置
    reference_b.place(x=449, y=27)

    # 《保存》選択ボタンの作成
    strage_b = ttk.Button(root, text=u'保存', command = strage_b_clicked) # ボタン処理
    strage_b.place(x=449, y=87) # ボタンの配置

    # 《参照先》ラベルの作成
    s = StringVar() # StringVarの作成
    s.set('< 参照先 >') # ラベルに値をセット
    label1 = ttk.Label(frame1, textvariable=s) # StringVarの指定
    label1.grid(row=0, column=0) # ラベルの配置

    # 《保存先》ラベルの作成
    v = StringVar() # StringVarの作成
    v.set('< 保存先 >') # ラベルに値をセット
    label2 = ttk.Label(frame3, textvariable=v) # StringVarの指定
    label2.grid(row=0, column=0) # ラベルの配置

    # 《参照ファイルパス》ラベルの作成
    file1 = StringVar() # StringVarの作成
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=60) # StringVarの指定とラベルの幅指定
    file1_entry.grid() # ラベルの配置

    # 《保存ファイルパス》ラベルの作成
    file2 = StringVar() # StringVarの作成
    file2_entry = ttk.Entry(frame3, textvariable=file2, width=60) # StringVarの指定とラベルの幅指定
    file2_entry.grid() # ラベルの配置

    # 《開始》ボタンの作成
    start_b = ttk.Button(frame2, text='開始', command = start_b_clicked) # ボタン処理
    start_b.pack(side=LEFT) # 左つめする

    # 《一時停止》ボタンの作成
    stop_b = ttk.Button(frame2, text='一時停止') # ボタン処理
    stop_b.pack(side=LEFT) # 左つめする

    # 《キャンセル》ボタンの作成
    cancel_b = ttk.Button(frame2, text='キャンセル') # ボタン処理
    cancel_b.pack(side=LEFT) # 左つめする

    # 《終了》ボタンの作成
    end_b = ttk.Button(frame2, text='終了', command=end_b_clicked) # ボタン処理
    end_b.pack(side=LEFT) # 左つめする

    root.mainloop() # 実行内容の処理の終了位置
