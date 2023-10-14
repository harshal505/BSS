# 1. Write a program to swap two numbers.
# a = 10
# b = 20
# print(f"a value before swap: {a},b value before swap :{b}")
# a = a + b
# b = a - b
# a = a - b
# print(f"a value after swap: {a},b value after swap :{b}")
from functools import reduce

# 2. How to check number is prime or not.
# 3. 4. Print Fibonacci series.
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)
# for item in range(1, 20):
#     result = num1 + num2
#     print(result)
#     num1 = num2
#     num2 = result

# 5. How to find the sum of elements in an array?
# a = [1, 2, 3, 4, 5, 6]
# result = 0
# for item in a:
#     result = result + item
#
# print(result)
# 6. How to find maximum and minimum elements in an array?
# a = [9, 2, 3, 4, 5, 6, 5, 9, 4, 3]
# maxi = a[0]
# mini = a[0]
# for item in a:
#     if maxi < item:
#         maxi = item
#     if mini > item:
#         mini = item
# print(maxi, mini)

# 7. How to find the length of the list?
# a = [9, 2, 3, 4, 5, 6, 5, 9, 4, 3]
# num=0
# for item in a:
#     num=num+1
# print(f"The length of list : {num}")

# 8. How to swap first and last elements in the list
# 9. How to swap any two elements in the list?
# a = ["ab", 2, True, 4, 5, False, 5, None, 4, True]
# temp = a[0]
# a[0] = a[-1]
# a[-1] = temp
# print(a)

# 10. How to remove the Nth occurrence of a given word list?
# a = ["a", "b", "c", "d", "e", "f"]
# b = eval(input("Enter the index number which want to remove : "))
# a.pop(b)
# print(a)

# 11. How to search an element in the list?
# a = ["ab", 2, True, "abcd", 4, 5, False, 5, None, 4, True]
# b = input("enter the element to be search : ")
# num = 0
# for item in a:
#     if b.isnumeric():
#         c = eval(b)
#         if c == item:
#             print("the search is successful", item, "Indexed in : ", num)
#             break
#     elif b.isalpha():
#         if b == item:
#             print("the search is successful", item, "Indexed in : ", num)
#             break
#     else:
#         print("the search is successful", item, "Indexed in : ", num)
#         break
#
#     num = num + 1

# 12. How to clear the list?
# a = ["ab", 2, True, "abcd", 4, 5, False, 5, None, 4, True]
# for item in range(0, len(a)):
#     a[item] = ""

# print(a)

# 13. How to reverse a list?
# a = ["ab", 2, True, "abcd", 4, 5, False, 5, None, 4, True]
# c = a.reverse()
# print(a)
# for items in range(0, len(a)):
#     temp = a[items]
#     a[items] = a
# 14. How to clone or copy a list?
# a = ["ab", 2, True, "abcd", 4, 5, False, 5, None, 4, True]
# b = a
# print(b)
# 15. How to count occurrences of an element in a list?
# a = ["ab", 2, True, "abcd", 4, 5, False, 5, 2, None, 4, True]
#
# for item in a:
#     b = a.count(item)
#     print(f"the count of {item} is {b}")
# 17. How to multiply all the numbers in the list? #
# a = [1, 2, 3, 4, 5]
# result = 1
# for item in a:
#     result = result * item
#
# print(result)
# 19. How to find the second_largest number in a list?#
# a = [1, 2, 3, 4, 5]
# for item in a:
#     maxi = item
#     if item>maxi:
#         maxi=item
#
#
#     for items in a:
#         mazi2=item

# 2. How to check number is prime or not.
# num = eval(input("Enter the valid Number"))
# flag = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         flag = flag + 1
#
# if flag == 2:
#     print("The number is prime Number", num)
# else:
#     print("The number is not prime Number", num)

# for item in range(1, 101):
#     flag = 0
#     for i in range(1, item + 1):
#         if item % i == 0:
#             flag = flag + 1
#     if flag == 2:
#         print(item, end="  ")

# for item in range(1, 6):
#     for i in range(1, item + 1):
#         print("*", end="")
#
#     print("\n")

# num = 5
# for item in range(6):
#     for i in range(num):
#         print(num, end="")
#     num = num - 1
#     print("\n")

# num = 5
# for item in range(6):
#     for i in range(num):
#         print("*", end="")
#     num = num - 1
#     print("\n")

# ageV = lambda age: age > 18
# print(ageV(19))
# print((lambda age: age > 18)(17))
# print((lambda age: "Age is above" if age > 18 else "Age is below")(17))
# print((lambda age: "Age is above" if age > 18 else "Age is below")(20))

# Odd or Even No
# NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# EvenList = list(filter(lambda item: item % 2 == 0, NumberList))
# print(EvenList)
#
# OddList = list(filter(lambda item: item % 2 == 1, NumberList))
# print(OddList)
#
# print(list(map(lambda item: "yes" if item % 2 == 0 else "No", NumberList)))

# NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# sumR = reduce(lambda a, b: a + b, NumberList)
# print(sumR)
# Multi = reduce(lambda a, b: a * b, NumberList)
# print(Multi)


# Numb = eval(input("Enter the valid No : "))
#
#
# def getFactorial(Numb):
#     if Numb <= 1:
#         return 1
#     return Numb * getFactorial(Numb - 1)
#
#
# Fact = getFactorial(Numb)
# print(Fact)

a = "mamxmcmqm"
for items in a:
    if items.find("m", 1):
        print("%", end="  ")
    else:
        print(items, end="  ")

# print(b)
#     print("%", end="  ")
# else:
#     print(item, end="  ")
