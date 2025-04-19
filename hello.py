# def alcohol(age, money):
#     if age >= 18 and money >= 10:
#         return "you cabn buy a drink"
#     elif age < 18 and money >=10:
#         return "you can buy a drink but you are not allowed to drink it"
#     elif age >= 18 and money < 10:
#         return "you are old enough to drink but you don't have enough money"
#     else:
#         return "you are not old enough to drink and you don't have enough money"
# print(alcohol(18, 6))
# def nl():
#     print("\n")
# nl()
# vegetables = ["cucumber", "spinach", "cabbage"]
# for x in vegetables:
#     print(x)
# nl()

# for num in range(1, 11):
#     print(num)
# nl()

# word = "hello"
# for letter in word:
#     print(letter)
# nl()

# num = 1
# while num < 20:
#     print(num)
#     num += 1

# password = ""
# while password != "secret":
#     password = input ("enter the correct password")
# print("you have entered the correct password")

# ""x = float(input("enter a number"))
# o = input("enter an operator")
# y= float(input("enter another number"))
# if o == "+":
#     print(x + y)
# elif o == "-":
#     print(x - y)
# elif o == "*":      
#     print(x * y)
# elif o == "/":
#     print(x / y)
# elif o == "%":
#     print(x % y)
# elif o == "**":
#     print(x ** y)
# elif o == "//":
#     print(x // y)
# elif o == "sqrt":
#     print(x ** 0.5)
# elif o == "sin":
#     import math
#     print(math.sin(x))
# elif o == "cos":                
#     import math
#     print(math.cos(x))
# else:
#     print("invalid operator")""
# drinks = [[ "rum", 6],["whiskey", 10],[ "vodka", 8],["gin", 7]]
# drinks.insert(2,["gin",7])
# print(drinks[2])
# food = {"kebab" : 10, "chicken" : 11}
# listfood = list(food.keys())[1]
# food.pop(listfood)
# sentence = "192. 168. 1. 254"
# listitem = sentence.split()
# print(listitem)
# spaceitem = '-'.join(listitem)
# print(spaceitem)
# person = {'name' : 'ali', 'age' : 29}
# person['country'] = "Iran"
# print(person)
import sys
print(sys.version)