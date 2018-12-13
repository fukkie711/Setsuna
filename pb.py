import os,sys,tkinter,time # os,sys,tkinterモジュール読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from copyXMLfiles import translate # translate関数を読み込み
from tkinter.constants import *
root = Tk()

root.title('Progress')
root.columnconfigure(0, weight=1);
root.rowconfigure(0, weight=1);

    # Frame
frame1 = ttk.Frame(root, padding=10)
frame1.grid(sticky=(N,W,S,E))
frame1.columnconfigure(0, weight=1);
frame1.rowconfigure(0, weight=1);


    # プログレスバー (確定的)
pb = ttk.Progressbar(
    frame1,
    orient=HORIZONTAL,
    length=200,
    mode='determinate')
for pbval in range(10000):
    print(pbval)
    pb.configure(maximum=10000, value=pbval)
pb.grid(row=0, column=0, sticky=(N,E,S,W))

root.mainloop()

def pb_bar(x, y):
    progress_bar = ttk.Progressbar(frameP,orient=HORIZONTAL,length=400,mode='determinate')
    progress_bar.configure(maximum=100, value = x )
    progress_bar.grid(row=1, column=0, sticky=(N,E,S,W))
