#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
root = tk.Tk()
b = tk.Button(root, text = 'You')
b.pack()
i = 0
def OnClick():
    global i
    if i == 0:
        b.config(state = 'disabled')
    else:
        b.config(state = 'normal')
    i = 1 - i


c = tk.Button(root, text = 'Me', command = OnClick)
c.pack()
tk.mainloop()
