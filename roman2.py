# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "blue", height = 250, width = 300)

# coord = 10, 50, 240, 210

for x in range(8):
    for y in range(8):
        size = 30
        start_x = x * size
        start_y = y * size
        # start_y = y * 20
        print(start_x, start_x+size)
        oval = C.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill='white')
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')

C.pack()
top.mainloop()