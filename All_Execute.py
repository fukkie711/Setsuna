import os,sys,tkinter,time, csv # os,sys,tkinterモジュール読み込み
from tkinter import * # tkinter全ロード
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from tkinter.constants import *
from All_Function import Function_A, Function_B, Function_C # 各機能を読み込み
from All_Function import Function_A_dash # 追加機能読み込み
from time import *
import random

# [宣言部]
list_csv = [] # リストの初期化
progress = 0 # 変数の宣言、カウント０

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
    #
    sss = r"" + file1.get() + ""# 参照先ディレクトリの絶対パス
    fff = r"" + file2.get() + ""# 保存先ディレクトリの絶対パス
    complete_file = 0 # 変数の初期化
    list_max = 0 # 変数の初期化
    path_list = [] # リストの初期化

    # xmlアドレス抽出部
    path_list, list_max = Function_A(sss) # 対象ドライブからxmlファイルの絶対パスを再帰的検索する関数。リストと総数を返す。
    # print("総数：：" + str(list_max)) # テスト用コード

    # エンコード&情報抽出、進捗割合変数演算部
    while complete_file <= list_max - 1: # list_max以下であればループ
        ope_file = path_list[complete_file] # 次の演算予定のファイルアドレスが格納されているリスト番号を読み出し
        absolute = Function_B(sss, ope_file, fff) # [変換]
        Function_C(fff, absolute) # [抽出]
        complete_file = complete_file + 1 # カウントアップ
        progress = round((complete_file / list_max) * 100, 1) # 再演算
        # print(str(progress) + "%完了") # テスト用コード
        progress_bar.configure(value = progress) # プログレスバーに演算結果を代入
        show.configure(text= (str(progress) + "%完了")) # 進捗割合テキストに演算結果を代入
        progress_bar.update() # プログレスバーを更新
        show.update() # 進捗割合テキストを更新

    Function_A_dash(sss, ope_file, fff)
if __name__ == '__main__': # 該当のスクリプトファイルがコマンドラインから実行された場合
    # rootの作成
    root = Tk() # 実行内容の処理の開始位置
    root.title('抽出プログラム') # ウインドウのタイトル
    root.geometry("550x200+450+250") # ウインドウのサイズ

    # Frame_refの作成
    # Frame_reference つまり参照先系ウィジェット
    frame_ref = ttk.Frame(root, padding=10) # windowの枠組み
    frame_ref.grid(row=0,column=0,stick=(S)) # 枠組みの配置

    # Frame_strの作成
    # Frame_strage　つまり保存先系ウィジェット
    frame_str = ttk.Frame(root, padding=10) # windowの枠組み
    frame_str.grid(row=1,column=0) # 枠組みの配置

    # Frame_PBの作成
    # Frame_ProgressBar　つまりプログレスバーウィジェット
    frame_pb= ttk.Frame(root, padding=10) # 枠組み定義
    frame_pb.grid(sticky=(W,E)) # 配置指定
    frame_pb.columnconfigure(0, weight=1)
    frame_pb.rowconfigure(0, weight=1)

    # Frame_butの作成
    # Frame_button　つまりボタン系ウィジェット
    frame_but = ttk.Frame(root, padding=10) # widgetをグループ化
    frame_but.grid(sticky=(N,W,S,E)) # 配置指定

    # [Front]プログレスバー(determinate_mode)
    progress_bar = ttk.Progressbar( # TkinterProgressbarウィジェットを使用
        frame_pb, # 配置フレーム指定
        orient=HORIZONTAL, # 左詰め配置
        length=400, # ウィジェット幅指定
        mode='determinate') # 確定的モード
    progress_bar.configure(maximum=100, value = progress) # 定義
    progress_bar.grid(row=1, column=0, sticky=(N,E,S,W)) # 配置指定

    # 進捗割合ラベル
    show = tkinter.Label(text="0%完了") #
    show.place(x=471, y=132)

    # 《参照》選択ボタンの作成
    reference_b = ttk.Button(root, text=u'参照', command=reference_b_clicked) # 内容定義
    reference_b.place(x=449, y=27) # 二次元配置指定

    # 《保存》選択ボタンの作成
    strage_b = ttk.Button(root, text=u'保存', command = strage_b_clicked) # 内容定義
    strage_b.place(x=449, y=87) # 二次元配置指定

    # 《参照先》ラベルの作成
    s = StringVar() # StringVarの作成
    s.set('< 参照先 >') # ラベルに値をセット
    label1 = ttk.Label(frame_ref, textvariable = s) # StringVarの指定、定義
    label1.grid(row=0, column=0) # 配置指定

    # 《保存先》ラベルの作成
    v = StringVar() # StringVarの宣言、作成
    v.set('< 保存先 >') # ラベルに値をセット
    label2 = ttk.Label(frame_str, textvariable=v) # StringVarの指定、定義
    label2.grid(row=0, column=0) # 配置指定

    # 《参照ファイルパス》ラベルの作成
    file1 = StringVar() # StringVarの宣言、作成
    file1_entry = ttk.Entry(frame_ref, textvariable=file1, width=60) # StringVarの指定とラベルの幅指定
    file1_entry.grid() # ラベルの配置

    # 《保存ファイルパス》ラベルの作成
    file2 = StringVar() # StringVarの宣言、作成
    file2_entry = ttk.Entry(frame_str, textvariable=file2, width=60) # StringVarの指定とラベルの幅指定
    file2_entry.grid() # 配置指定

    # 《開始》ボタンの作成
    start_b = ttk.Button(frame_but, text='開始', command = start_b_clicked) # 定義
    start_b.pack(side=LEFT) # 左つめする

    # 《一時停止》ボタンの作成
    stop_b = ttk.Button(frame_but, text='一時停止') # ボタン処理
    stop_b.pack(side=LEFT) # 左つめする

    # 《キャンセル》ボタンの作成
    cancel_b = ttk.Button(frame_but, text='キャンセル') # ボタン処理
    cancel_b.pack(side=LEFT) # 左つめする

    # 《終了》ボタンの作成
    end_b = ttk.Button(frame_but, text='終了', command=end_b_clicked) # 定義
    end_b.pack(side=LEFT) # 左つめする

    root.mainloop() # 実行内容の処理の終了位置
