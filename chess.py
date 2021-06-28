from tkinter import *
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x= 500, y=470)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=500, y=500)
window.title('Chess')
window.geometry("800x600+10+10")


size = 55
padding = 5

C = Canvas(window, bg = "blue", height = (size * 8) + padding + padding, width = (size * 8) + padding + padding)

# coord = 10, 50, 240, 210


for x in range(8):
    for y in range(8):
        fill_color = 'white' if (x + y) % 2 else '#8B4513' 
        start_x = (x * size) + padding
        start_y = (y * size) + padding
        rect = C.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill=fill_color, width=0)
#arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
#line = C.create_line(10,10,200,200,fill = 'white')

C.pack()
window.mainloop()