import os,sys,tkinter,time # os,sys,tkinterモジュール読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from copyXMLfiles import translate # translate関数を読み込み

# 参照ボタンのイベント
# button1クリック時の処理
filepath1 = "" # filepath1変数の初期化
filepath2 = "" # filepath2変数の初期化
def button1_clicked(): # button1_clickedの関数を定義
    fTyp = [("","*")] # 表示オプション
    filepath1 = tkinter.filedialog.askdirectory() # directoryを選択する
    file1.set(filepath1)# filepath1をsetに変換する
    return filepath1# filepath1に返す

# button3クリック時の処理
def button3_clicked(): # button3_clickedの関数を定義
    fTyp = [("","*")] #表示オプション
    filepath2 = tkinter.filedialog.askdirectory() # directoryを選択する
    file2.set(filepath2) # filepath2をsetに変換する
    return filepath2 # filepath2に返す

# button4クリック時の処理（終了ボタン）
def button4_clicked(): # button4_clickedの関数を定義
    tkmsg.askquestion(message = u'本当に終了しますか？ by Shin') # 確認ダイアログ

# button2クリック時の処理 (開始ボタン)
def button2_clicked(): # button2_clickedの関数を定義
    sss = file1.get() # 参照先ディレクトリの絶対パス
    fff = file2.get() # 保存先ディレクトリの絶対パス
    sss = r"" + sss + "" # row文字列にして代入
    fff = r"" + fff + "" # row文字列にして代入
    translate(sss, fff) # copyXMLのtlanslate関数を実行
    while judge == 0:
        messagebox.showinfo('FileReference Tool', u'参照ファイルは↓↓\n' + sss
        + u'\n\n参照ファイルは↓↓\n' + fff) # 確認ダイアログ
        pbbar(progress)
    messagebox.showinfo('FileReference Tool', u'抽出完了') # 終了メッセージ
if __name__ == '__main__': # 該当のスクリプトファイルがコマンドラインから実行された場合
    # rootの作成
    root = Tk() # 実行内容の処理の開始位置
    root.title('抽出プログラム') # ウインドウのタイトル
    root.geometry("550x200+400+200") # ウインドウのサイズ

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10) # windowの枠組み
    frame1.grid() # 枠組みの配置

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked) # ボタン処理
    button1.grid(row=0, column=3) # ボタンの配置

    frame3 = ttk.Frame(root, padding=10) # windowの枠組み
    frame3.grid() # 枠組みの配置

    # 参照2ボタンの作成
    button4 = ttk.Button(root, text=u'保存', command=button3_clicked) # ボタン処理
    button4.grid(row=1, column=3) # ボタンの配置

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



    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10) # widgetをグループ化
    frame2.grid(row=2) # 配置指定

    # 開始ボタンの作成
    button2 = ttk.Button(frame2, text='開始', command=button2_clicked) # ボタン処理
    button2.pack(side=LEFT) # 左つめする

    # 一時停止ボタンの作成
    button5 = ttk.Button(frame2, text='一時停止') # ボタン処理
    button5.pack(side=LEFT) # 左つめする

    # キャンセルボタンの作成
    button6 = ttk.Button(frame2, text='キャンセル') # ボタン処理
    button6.pack(side=LEFT) # 左つめする

    # 終了ボタンの作成
    button3 = ttk.Button(frame2, text='終了', command=button4_clicked) # ボタン処理
    button3.pack(side=LEFT) # 左つめする

    root.mainloop() # 実行内容の処理の終了位置
