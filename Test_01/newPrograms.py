# 1. Write a program to swap two numbers.
# a = 10
# b = 20
# # tem = a
# a = b
# b = tem
# print(f"The value of a is {a} and value b {b}")
from functools import reduce

# a = a + b
# b = a - b
# a = a - b
# print(f"The value of a is {a} and value b {b}")

# a, b = b, a
# print(f"The value of a is {a} and value b {b}")

# 2. How to check number is prime or not.
# a = eval(input("Enter a valid Number : "))
# flag = 0
# for i in range(1, a + 1):
#     if a % i == 0:
#         flag = flag + 1
# if flag == 2:
#     print(f"The entered Number {a} is Prime Number")
# else:
#     print(f"The entered Number {a} is Not Prime Number")

# for item in range(2, 101):
#     flag = 0
#     for i in range(1, item + 1):
#         if item % i == 0:
#             flag = flag + 1
#     if flag == 2:
#         print(item, end="   ")


# 3. How to find factorial of a number
# a = eval(input("Enter a valid Number : "))
# fact = 1
# for i in range(1, a + 1):
#     fact = fact * i
#
# print(f"The factorial of {a} is {fact}")

# a = eval(input("Enter a valid Number : "))
# b = a
# fact = 1
# while b >= 1:
#     fact = fact * b
#     b = b - 1
# print(f"The factorial of {a} is {fact}")

# def getFactorial(num):
#     if num <= 1:
#         return 1
#     return num * getFactorial(num - 1)
#
#
# fact = getFactorial(2)
# print(f"The factorial of number is {fact}")

# 4. Print Fibonacci series.
# a = 0
# b = 1
# print(a, end="  ")
# print(b, end="  ")
# for i in range(1, 10):
#     result = a + b
#     print(result, end="  ")
#     a = b
#     b = result

# 5. How to find the sum of elements in an array?
# aList = [1, 2, 3, 4, 5, 6]
# summ = reduce(lambda a, b: a + b, aList)
# print(summ)

# 6. How to find maximum and minimum elements in an array?
# aList = [1, 2, 3, 4, 5, 6, 4, 5, 7, 1, 0]
# maxi = aList[0]
# mini = aList[0]
# for i in aList:
#     if i > maxi:
#         maxi = i
#     if i < mini:
#         mini = i
# print(f"The maximum value in the list is {maxi} ,The minimum value in the list is {mini}")

# 7. How to find the length of the list?
# aList = [1, 2, 3, 4, 5, 6, 4, 5, 7, 1, 0]
# print(len(aList))
# count = 0
# for i in aList:
#     count = count + 1
# print(f"The lenght of List is {count}")

# 8. How to swap first and last elements in the list
# aList = [1, 2, 3, 4, 5, 6, 4, 5, 7, 1, 0]
# print(aList)
# num = aList.pop()
# num2 = aList.pop(0)
# aList.append(num2)
# aList.insert(num, 0)
# print(aList)

# 10. How to remove the Nth occurrence of a given word list?
# aStrList = ["a", "b", "c", "a", "d", "c", "c", "a"]
# print(aStrList)
#
# for item in aStrList:
#     count = 0
#     a = 0
#     for i in aStrList:
#         a = a + 1
#         if item == i:
#             count = count + 1
#         if count >= 2:
#             aStrList.pop(a-1)
#
# print(aStrList)

# aStrList = ["a", "b", "c", "a", "d", "c"]
# a = input("Enter str to be Searched : ")
# for item in aStrList:
#     if a == item:
#         print("The string is present in List", a)
#         break
# else:
#     print("The string is Not present in List", a)

# 12. How to clear the list?
# aStrList = ["a", "b", "c", "a", "d", "c"]
# print(aStrList)
# aStrList.clear()
# print(aStrList)

# 13. How to reverse a list?
# aStrList = ["a", "b", "c", "a", "d", "c"]
# print(aStrList)
# aStrList.reverse()
# print(aStrList)

# 14. How to clone or copy a list?
# aStrList = ["a", "b", "c", "a", "d", "c"]
# b=[]
# for items in aStrList:
#     b.append(items)
# print(aStrList)
# print(b)

# 15. How to count occurrences of an element in a list?
# aStrList = ["a", "b", "c", "a", "d", "c"]
#
# for item in aStrList:
#     repeat = aStrList.count(item)
#
#     print(f"The count of  {item} is {repeat}")

# 16. Find the sum of the elements in list

# aList = [1, 2, 3, 4, 5, 6, 4, 5, 7, 1, 0]
# summ = reduce(lambda a, b: a + b, aList)
# print(summ)

# 17. How to multiply all the numbers in the list?
# aList = [1, 2, 3, 4, 5]
# mul = reduce(lambda a, b: a * b, aList)
# print(mul)

# 18. How to find the smallest and largest numbers on the list?
# 19. How to find the second largest number in a list?
aList = [1, 2, 3, 4, 5]
max = aList[0]
for item in aList:
    if item > max:
        max = item
max2=
