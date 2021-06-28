# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox
import tkinter as tk

window = Tk()


size = 55
padding = 5
gameboard_start = 40

total_size = (size * 8) + (padding * 2) + (gameboard_start * 2)

C = Canvas(window, bg = "gray", height = total_size, width = total_size)

# coord = 10, 50, 240, 210


for x, letter in enumerate('ABCDEFGH'):
    start_x = (x * size) + gameboard_start
    start_y = (0 * size) + gameboard_start
    C.create_text(start_x + (size/2),start_y-18,fill="darkblue",font="Ariel 20 bold", text=letter, justify=tk.CENTER, width=30)

for x, letter in enumerate('ABCDEFGH'):
    start_x = (x * size) + gameboard_start
    start_y = (9 * size) + gameboard_start
    C.create_text(start_x + (size/2),start_y-30,fill="darkblue",font="Ariel 20 bold", text=letter, justify=tk.CENTER, width=30)

for y, letter in enumerate('12345678'):
    start_x = (0 * size) + gameboard_start
    start_y = (y * size) + gameboard_start
    C.create_text(start_x-18,start_y + (size/2),fill="darkblue",font="Ariel 20 bold", text=letter, justify=tk.CENTER, width=30)

for y, letter in enumerate('12345678'):
    start_x = (8 * size) + gameboard_start
    start_y = (y * size) + gameboard_start
    C.create_text(start_x+15,start_y + (size/2),fill="darkblue",font="Ariel 20 bold", text=letter, justify=tk.CENTER, width=30)

for x in range(8):
    for y in range(8):
        fill_color = '#8B4513' if (x + y) % 2 else 'white' 
        start_x = (x * size) + gameboard_start
        start_y = (y * size) + gameboard_start
        rect = C.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill=fill_color, width=0)
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')

C.pack()
window.mainloop()