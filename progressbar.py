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
for q in range(100):
    frame = ttk.Frame()
    pb = ttk.Progressbar(frame, orient=HORIZONTAL, length=300, mode='determinate')
    pb.configure(maximum=100, value=q)
    frame.pack()
    pb.pack()
<<<<<<< HEAD
    pb.start(100)

=======
    #pb.start(100)
>>>>>>> dd3dddbaa79a87c5c982b720582a032def925fe3
root.mainloop()
