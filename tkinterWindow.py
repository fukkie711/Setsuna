from tkinter import *
from tkinter import ttk

def foo():
    print('Hello, %s!' % t.get())

root = Tk()
root.title('My First App')
frame1 = ttk.Frame(root)
label1 = ttk.Label(frame1, text='Your name:')

t = StringVar()

entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(frame1, text='OK', command=foo)

frame1.grid(row=0,column=0,sticky=(N,E,S,W))
label1.grid(row=1,column=1,sticky=E)
entry1.grid(row=1,column=2,sticky=W)
button1.grid(row=2,column=2,sticky=W)

for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

# ここでは画面だけ作成したい。
# この画面から、各処理を読み出す形にしたい。
import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("tyuusyutu")
root.geometry("500x400+400+200")

root.mainloop()
