# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.font as font

class FontChart(tk.Frame):

    MAX_ROWS = 36
    FONT_SIZE = 8

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        r = 0
        c = 0

        for color in FONTS:
            label = tk.Label(self, text=color,
                             font=(color, self.FONT_SIZE, "bold"))
            label.grid(row=r, column=c, sticky="ew")
            r += 1

            if r > self.MAX_ROWS:
                r = 0
                c += 1

        self.pack(expand=1, fill="both")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Named Font Chart")
    FONTS = list(font.families(root))
    app = FontChart(root)
    root.mainloop()
