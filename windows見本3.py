# ここでは画面だけ作成したい。
# この画面から、各処理を読み出す形にしたい。
import os
import sys
import tkinter
from tkinter import font
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#botan1クリック時の処理
def botan1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)

#botan2クリック時の処理
def botan2_clicked():
    messagebox.showinfo('FileReference Tool', u'参照ファイルは\n' + file1.get())

if __name__=='__main__':

 #rootの作成
 root = tkinter.Tk()
 root.title("抽出")
 root.geometry("500x400+400+200")
 root.resizable(False, False)

 #Frame1の作成
 frame1 = ttk.Frame(root, padding=50)
 frame1.place(x=50, y=50)
 frame1.grid()

 #ボタン１
# def openfile(event):
    #FOLDER = r'C:\Users\T15015'
    #import subprocess
    #subprocess.Popen(['explorer', FOLDER])

 button1 = tkinter.Button(text=u'参照1')
 button1.place(x=300, y=50)
 #button1.bind("<Button-1>",openfile)

 #ボタン２
 #def openfile(event):
    #FOLDER = r'C:\Users\T15015'
    #import subprocess
    #subprocess.Popen(['explorer', FOLDER])

 button2 = tkinter.Button(text=u'参照2')
 button2.place(x=300, y=100)
 #button2.bind("<Button-1>",openfile)

 #ラベル
 s = StringVar()
 s.set('ファイル>>')
 static1= ttk.Label(frame1, textvariable=s)
 static1.place(x=50, y=50)

 #参照ファイルパス表示ラベルの作成
 file1 = StringVar()
 file_entry = ttk.Entry(frame1, textvariable=file1, width=30)
 file_entry.grid()

 file2 = StringVar()
 file_entry = ttk.Entry(frame1, textvariable=file2, width=30)
 file_entry.grid()

 #Frame3の作成
 frame3 = ttk.Frame(root, padding=(0,5))
 frame3.grid()

 #Startボタンの作成
 button3 = ttk.Button(frame3, text='Start', command=botan1_clicked)
 button3.pack(side=LEFT)

 #Cancelボタンの作成
 button4 = ttk.Button(frame3, text='Cancel', command=quit)
 button4.pack(side=LEFT)

 root.mainloop()
