# ここでは画面だけ作成したい。
# この画面から、各処理を読み出す形にしたい。
import sys
import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("抽出")
root.geometry("500x400+400+200")

#ラベル
Static1 = tkinter.Label(text=u'test')
#Static1 = tkinter.Label(font=20)
Static1.place(x=50, y=50)

Static2 = tkinter.Label(text=u'test2')
Static2.place(x=50, y=100)

#ボタン
Button = tkinter.Button(text=u'参照1')
Button.place(x=300, y=50)

Button = tkinter.Button(text=u'参照2')
Button.place(x=300, y=100)

root.mainloop()
