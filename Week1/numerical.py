# print(round(8 / 3, 2)) round numbers
# print(8 // 3) - makes this into an integer when divided 
# print(type(4 / 2)) - division will always become a float unless you do it like below
# print(2 // 2)

# score = 0
# height = 1.8
# isWinning = True
# #f-string converting data types into strings
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# print("welcome to the ticket buyer")
# age = int(input("how old are you?"))
# if age >= 18:
#     print("your ticket is $12")
# else:
#     print("your ticket is $10 ")


print("Thank you for choosing Python Pizza")
size = input("What size do you want? S, M, or L")
if size == "S":
    price = 15
    print("That'll be $15")
elif size == "M":
    price = 20
    print("That'll be 20")
elif size == "L":
    price = 25
    print("That'll be $25")
addPepp = input("do you want to add pepporoni?")
if addPepp == "Y":
    price += 3
exCheese = input("do you want extra cheese?")
if exCheese == "Y":
    price +=2
    
print(f"Your total is ${price}")

# age = "10"
# # print(type(age))
# NewAge = int(age)
# print(NewAge + 20)12
