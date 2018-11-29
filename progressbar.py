import os,sys,tkinter # os,sys,tkinterモジュール読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み

#def prbar(q):

    #root = Tk()

    #frame = ttk.Frame()
    #pb = ttk.Progressbar(frame, length=300, mode='determinate')
    #frame.pack()
    #pb.pack()
    #pb.start(25)

    #root.mainloop()

root = Tk()
q = 0
for q in range(10000):

    frame = ttk.Frame()
    pb = ttk.Progressbar(frame, length=300, mode='determinate', value=q, maximum=10000)
    frame.pack()
    pb.pack()
    pb.start(100)

root.mainloop()
