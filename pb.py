from tkinter import *
from time import *

root = Tk()
root.option_add('*font', ('FixedSys', 14))

buff = StringVar()
buff.set('')

Label(textvariable = buff).pack()

# 時刻の表示
def show_time():
    buff.set(strftime('%I:%M:%S'))
    root.after(1000, show_time)

show_time()
root.mainloop()
