from tkinter import *
from tkinter import ttk

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
