# 1
# import tkinter as tk 
# import random
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("PNC UI GAME")
# canvas = tk.Canvas(frame)
# number = [1,2,3,4,5,6,7,8,9,10]
# numOfRandom = random.choice(number)
# x1 = 50
# x2 = 90
# y1 = 50
# y2 = 90
# for i in range(10):
#     canvas.create_oval(x1,y1,x2,y2,fill="blue")
#     if numOfRandom == i :
#           canvas.create_oval(x1,y1,x2,y2,fill="red")
#     x1 += 39
#     x2 += 39
#     y1 = 50
#     y2 = 90
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
# number = [1,2,3,4,5]
# numOfRandom = random.choice(number)
# x1 = 54
# x2 = 90
# y1 = 54
# y2 = 90
# for i in range(5):
#     for k in range (5):
#         canvas.create_oval(x1,y1,x2,y2,fill="blue",outline="")
#         if k == i :
#             canvas.create_oval(x1,y1,x2,y2,fill="red",outline="")
#         x1 = x2+4
#         x2 += 39
#     x1 =54
#     x2 =90 
#     y1 = y2 +4
#     y2 += 39
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
# colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple']
# x1 = 50
# x2 = 90
# y1 = 50
# y2 = 90
# for i in range(10):      
#     for k in range(10):
#         if i == 0 or i == 9 or k == 0 or k == 9:
#             canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(colors))
#         elif i % 2 ==1  and k % 2 == 1 :
#             canvas.create_rectangle(x1,y1,x2+50,y2+50,fill=random.choice(colors))
#         x1 = x2+10
#         x2 += 50
#     y1 = y2 +10
#     y2 += 50
#     x1 = 50
#     x2 = 90
# canvas.pack(expand=True,fill="both")
# frame.pack(expand=True,fill="both")
# root.mainloop()