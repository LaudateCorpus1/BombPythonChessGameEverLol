# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()


size = 50
padding = 5

C = Canvas(top, bg = "blue", height = (size * 8) + padding + padding, width = (size * 8) + padding + padding)

# coord = 10, 50, 240, 210

for x in range(8):
    for y in range(8):
        start_x = (x * size) + padding
        start_y = (y * size) + padding
        rect = C.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill='white')
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')

C.pack()
top.mainloop()