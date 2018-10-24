import os,sys,tkinter
import tkinter.messagebox as tkmsg
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from copyXMLfiles import translate

# 参照ボタンのイベント
# button1クリック時の処理
filepath1 = ""
filepath2 = ""
def button1_clicked():
    fTyp = [("","*")]
    #iDir = os.path.abspath(os.path.dirname(__file__))
    #file1path1 = filedialog.askdireatory()
    #filepath1 = filedialog.askdirectory(filetypes = fTyp,initialdir = iDir)
    filepath1 = tkinter.filedialog.askdirectory()
    file1.set(filepath1)
    return filepath1

# button3クリック時の処理
def button3_clicked():
    fTyp = [("","*")]
    #iDir = os.path.abspath(os.path.dirname(__file__))
    filepath2 = tkinter.filedialog.askdirectory()
    file2.set(filepath2)
    return filepath2

# button4クリック時の処理（終了ボタン）
def button4_clicked():
    tkmsg.askquestion(message = u'本当に終了しますか？ by Shin')

    #if(result == messageboxresult.yes){
     # command = guit
    #}else if(result == messageboxresult.no){

    #}

# button2クリック時の処理 (開始ボタン)
def button2_clicked():
    sss = file1.get() # 参照先ディレクトリの絶対パス
    fff = file2.get() # 保存先ディレクトリの絶対パス
    messagebox.showinfo('FileReference Tool', u'参照ファイルは↓↓\n' + sss
    + u'\n\n参照ファイルは↓↓\n' + fff) # 確認ダイアログ
    sss = r"" + sss + "" # row文字列にして代入
    fff = r"" + fff + "" # row文字列にして代入
    translate(sss, fff) # copyXMLのtlanslate関数を実行

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('抽出プログラム')
    root.geometry("550x400+400+200")

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # 参照2ボタンの作成
    button4 = ttk.Button(root, text=u'参照2', command=button3_clicked)
    button4.place(x=446, y=52)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('< ファイル >')

    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=60)
    file1_entry.grid()

    # 参照ファイルパス表示ラベル2の作成
    file2 = StringVar()
    file2_entry = ttk.Entry(frame1, textvariable=file2, width=60)
    file2_entry.grid()

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # 開始ボタンの作成
    button2 = ttk.Button(frame2, text='開始', command=button2_clicked)
    button2.pack(side=LEFT)

    # 一時停止ボタンの作成
    button5 = ttk.Button(frame2, text='一時停止')
    button5.pack(side=LEFT)

    # キャンセルボタンの作成
    button6 = ttk.Button(frame2, text='キャンセル')
    button6.pack(side=LEFT)

    # 終了ボタンの作成
    button3 = ttk.Button(frame2, text='終了', command=button4_clicked)
    button3.pack(side=LEFT)

    root.mainloop()
