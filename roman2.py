# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

window = Tk()


size = 55
padding = 5

C = Canvas(window, bg = "blue", height = (size * 8) + padding + padding, width = (size * 8) + padding + padding)

# coord = 10, 50, 240, 210


for x in range(8):
    for y in range(8):
        fill_color = '#8B4513' if (x + y) % 2 else 'white' 
        start_x = (x * size) + padding
        start_y = (y * size) + padding
        rect = C.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill=fill_color, width=0)
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')

C.pack()
window.mainloop()