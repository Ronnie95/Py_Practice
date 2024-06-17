# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:          missing ==
#     print("This is an even number")
# else:
#     print("This is an odd number")

# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# year = input()  missing int input

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

# year = int(input())  #missing int input

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")

target = int(input())
for number in range(1, target + 1):
    if number % 3 == 0 or number % 5 == 0:
        print("fizz buzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])