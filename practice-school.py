#==========DAY-1==========
#1
# number = int(input())
# result = False
# if (1 < number and number <10) or (30 < number and number<50) or(77 < number and number <100):
#     result =True
# print(result)
#4
# number =  str(input())
# result = False
# for i in range(len(number)):
#     if number[i] =="!":
#         result = True
# print(result)   
#5
# number = eval(input())
# result = "FAIL"
# numOfNumber = 0
# for i in range(len(number)):
#     numOfNumber += number[i]
#     if (numOfNumber /len(number))>= 50:
#         result = "PASS"
# print(result)
#6
# boolean =  eval(input())
# result = 0
# for i in range(len(boolean)):
#     if boolean[i] == True:
#         result += 1
# print(result)  
#7
# start = int(input())
# for num in range(start+1):
#     if num % 2 == 0:
#         print(num, end = " " )
#==========DAY-2==========
#2
# letter = str (input())
# result = False
# for i in range(len(letter)):
#     if (letter[i]== "A" or letter[i]== "a") or (letter[i]== "B" or letter[i]== "b") or (letter[i]== "C" or letter[i]== "c") or (letter[i]== "D" or letter[i]== "d"):
#         result = True
# print(result)
#3
# arr = []
# for i in range(3):
#     number = int(input())
#     if number >= 10 and number<= 50 :
#         arr.append(number)
# print(arr)
#1 
# arr = eval (input())
# res = []
# findOne = False
# findTwo = False
# for i in range(len(arr)):
#     if arr[i] == 1 and not findOne :   
#         one = i
#         findOne = True
#     elif arr[i] == 0 and not findTwo and findOne :   
#         two = i
#         findTwo  = True
# for k in range(len(arr)):
#     if findTwo and findOne and k > one and two >k:
#         res.append(arr[k])
# print(res)
#4
# letter = str(input())
# car = letter.lower()
# for i in range(len(letter)):
#     if letter[0] == " ":
#         car = letter.capitalize()
# print(car)
#5
# materials = eval(input())
# totalPrice = 0
# for key in materials:
#     if key["quality"] =="Good":
#         totalPrice += key["retail-price"]*key["quantity"]
# print(totalPrice)
#6
arr = eval(input())
