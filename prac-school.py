import tkinter as tk
import random
root = tk.Tk()
root.geometry("900x1000")
frame = tk.Frame()
frame.master.title("Hello! How are you?")
canvas= tk.Canvas(frame)
x1 = 30
y1 = 30
x2 = 70
y2 = 70
color= ("blue","red","yellow","purple","green","lightblue")
for k in range(10):
    for i in range (10):
        canvas.create_oval(x1,y1,x2,y2,fill=random.choice(color))
        x1 += 50
        y1 += 50
    x2 += 50
    y2 += 50
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()