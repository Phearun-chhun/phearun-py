# 1
# import tkinter as tk 
# import random
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)
# root.configure(bg="yellow")
# x1 = 50
# x2 = 90
# y1 = 50
# y2 = 90
# oval = canvas.create_oval(50,50,200,200,fill="blue",tags="oval")
# square = canvas.create_rectangle(300,50,450,200,fill="red",tags="square")
# rectangle =canvas.create_rectangle(50,250,450,400,fill="orange",tags="rectangle")
# def myEventOfCircle(even):
#     print("user has clicked on circle ")
# def myEventOfRectangle(even):
#     print("user has clicked on rectangle  ")
# def myEventOfSquare(even):
#     print("user has clicked on square")
# canvas.tag_bind("oval", "<Button-1>",myEventOfCircle)
# canvas.tag_bind("rectangle", "<Button-1>",myEventOfRectangle)
# canvas.tag_bind("square", "<Button-1>",myEventOfSquare)
# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()
# 2
# import tkinter as tk 
# import random
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)
# numOfRandom = random.randrange(0,9)
# x1 = 50
# x2 = 90
# y1 = 50
# y2 = 90
# for i in range(9):
#     if i == numOfRandom :      
#         canvas.create_oval(x1,y1,x2,y2,fill="blue",outline="",tags="PNCTaraget")
#     else:
#         canvas.create_oval(x1,y1,x2,y2,fill="blue",outline="")
#     x1 = x2+10  
#     x2 += 50
# y1 = y2 +10
# y2 += 50
# x1 = 50
# x2 = 90
# def secretCircle(event):        
#         canvas.create_text(x2+200,y2+300,text="You win!",font=("Purisa",27))          
# canvas.tag_bind("PNCTaraget", "<Button-1>",secretCircle)
# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()
# 3
# import tkinter as tk 
# import random
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)
# numOfRandom = random.randrange(0,9)
# x1 = 50
# x2 = 90
# y1 = 50
# y2 = 90
# for i in range(9):
#     if i == numOfRandom :
      
#         canvas.create_oval(x1,y1,x2,y2,fill="blue",outline="",tags="PNCTaraget")
#     else:
#         canvas.create_oval(x1,y1,x2,y2,fill="blue",outline="")
#     x1 = x2+10  
#     x2 += 50
# y1 = y2 +10
# y2 += 50
# x1 = 50
# x2 = 90
# def secretCircle(event):
#         x1 = 50
#         x2 = 90
#         canvas.create_text(x2+200,y2+300,text="You win!",font=("Purisa",27))
#         canvas.delete("PNCTaraget")
#         for i in range(9):
#             if i == numOfRandom:
#                 canvas.create_oval(x1,40,x2,80,fill="yellow",outline="",tags="PNCTaraget")        
#             x1 = x2+10  
#             x2 += 50            
# canvas.tag_bind("PNCTaraget", "<Button-1>",secretCircle)
# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()