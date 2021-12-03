# ==========practice1==========
# 1
# import tkinter as tk 
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)
# canvas.create_rectangle(100,100,500,500,fill="red")
# canvas.create_rectangle(140,140,460,460,fill="blue")
# canvas.create_rectangle(180,180,420,420,fill="green")
# canvas.create_rectangle(220,220,380,380,fill="orange")
# canvas.create_rectangle(260,260,340,340,fill="green")
# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()
#2
# import tkinter as tk 
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)
# canvas.create_oval(100,100,500,500,fill="red")
# canvas.create_oval(140,140,460,460,fill="blue")
# canvas.create_oval(180,180,420,420,fill="green")
# canvas.create_oval(220,220,380,380,fill="orange")
# canvas.create_oval(260,260,340,340,fill="green")
# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()
#3
import tkinter as tk 
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("PNC UI GAME")

canvas = tk.Canvas(frame)
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
x1 = 50
x2 = 90
y1 = 50
y2 = 90
for i in range(9):
    for k in range(9):
        canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors),outline="")
        x1 = x2+10
        x2 += 50
    y1 = y2 +10
    y2 += 50
    x1 = 50
    x2 = 90
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()