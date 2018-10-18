import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# 参照ボタンのイベント
# button1クリック時の処理
def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)

# button2クリック時の処理
def button2_clicked():
    messagebox.showinfo('FileReference Tool', u'参照ファイルは↓↓\n' + file1.get())

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('抽出')
    root.geometry("550x400+400+200")

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=1, column=0)

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # Startボタンの作成
    button2 = ttk.Button(frame2, text='Start', command=button2_clicked)
    button2.pack(side=LEFT)
    #button2.place(x=50, y=20)

    # Cancelボタンの作成
    button3 = ttk.Button(frame2, text='Cancel', command=quit)
    button3.pack(side=LEFT)
    #button3.place(x=50, y=50)

    root.mainloop()
