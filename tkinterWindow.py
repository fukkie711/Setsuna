import os,sys,tkinter,time # os,sys,tkinterモジュール読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from copyXMLfiles import translate # translate関数を読み込み
from tkinter.constants import *

# 参照ボタンのイベント
# reference_bクリック時の処理
filepath1 = "" # filepath1変数の初期化
filepath2 = "" # filepath2変数の初期化
def reference_b_clicked(): # reference_b_clickedの関数を定義
    fTyp = [("","*")] # 表示オプション
    filepath1 = tkinter.filedialog.askdirectory() # directoryを選択する
    file1.set(filepath1)# filepath1をsetに変換する
    return filepath1# filepath1に返す

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
    sss = file1.get() # 参照先ディレクトリの絶対パス
    fff = file2.get() # 保存先ディレクトリの絶対パス
    sss = r"" + sss + "" # row文字列にして代入
    fff = r"" + fff + "" # row文字列にして代入
    translate(sss, fff) # copyXMLのtlanslate関数を実行
    messagebox.showinfo('Filereference_b Tool', u'参照ファイルは↓↓\n' + sss
    + u'\n\n参照ファイルは↓↓\n' + fff) # 確認ダイアログ

    # プログレスバーの作成
    progress_bar = ttk.Progressbar(
        frameP,
        orient=HORIZONTAL,
        length=400,
        mode='indeterminate')
    progress_bar.configure(maximum=100, value=0)
    progress_bar.grid(row=1, column=0, sticky=(N,E,S,W))
    progress_bar.start(100)

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
    frameP.columnconfigure(0, weight=1);
    frameP.rowconfigure(0, weight=1);

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10) # widgetをグループ化
    frame2.grid(sticky=(N,W,S,E)) # 配置指定

    # 参照ボタンの作成
    reference_b = ttk.Button(root, text=u'参照', command=reference_b_clicked) # ボタン処理
    #reference_b.grid(row=0, column=3) # ボタンの配置
    reference_b.place(x=449, y=27)
    # 保存ボタンの作成
    strage_b = ttk.Button(root, text=u'保存', command = strage_b_clicked) # ボタン処理
    strage_b.place(x=449, y=87) # ボタンの配置

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar() # StringVarの作成
    s.set('< 参照先 >') # ラベルに値をセット

    label1 = ttk.Label(frame1, textvariable=s) # StringVarの指定
    label1.grid(row=0, column=0) # ラベルの配置

    v = StringVar() # StringVarの作成
    v.set('< 保存先 >') # ラベルに値をセット

    label2 = ttk.Label(frame3, textvariable=v) # StringVarの指定
    label2.grid(row=0, column=0) # ラベルの配置


    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar() # StringVarの作成
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=60) # StringVarの指定とラベルの幅指定
    file1_entry.grid() # ラベルの配置

    # 参照ファイルパス表示ラベル2の作成
    file2 = StringVar() # StringVarの作成
    file2_entry = ttk.Entry(frame3, textvariable=file2, width=60) # StringVarの指定とラベルの幅指定
    file2_entry.grid() # ラベルの配置

    # 開始ボタンの作成
    start_b = ttk.Button(frame2, text='開始', command = start_b_clicked) # ボタン処理
    start_b.pack(side=LEFT) # 左つめする

    # 一時停止ボタンの作成
    stop_b = ttk.Button(frame2, text='一時停止') # ボタン処理
    stop_b.pack(side=LEFT) # 左つめする

    # キャンセルボタンの作成
    cancel_b = ttk.Button(frame2, text='キャンセル') # ボタン処理
    cancel_b.pack(side=LEFT) # 左つめする

    # 終了ボタンの作成
    end_b = ttk.Button(frame2, text='終了', command=end_b_clicked) # ボタン処理
    end_b.pack(side=LEFT) # 左つめする

    root.mainloop() # 実行内容の処理の終了位置
