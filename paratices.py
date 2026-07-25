# first = "hi my name is sohail"
# second = "my age is 32"
# date = 31

# # print(f"{first}, {second}, {date}")

# a = "go"
# b = "come"
# print(f"i want to {a} to home and i will {b} back tommoro")

# num1 = int(input("enter first number :- "))
# num2 = int(input("enter secound number :-"))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 % num2)
# print(num1 ** num2)

# num = int(input("enter a number :- "))
# num += 10
# num /= 2
# num *= 3
# # num //=2
# # # 
# # print(num)

# num = int(input("give a number to print helloo :- "))

# for i in range(num,num+1,1):
#     print("hello"*num)


# num = int(input("enter a number :- "))

# if num > 50 :
#     print("big number")
# else :
#     print("small number")


# num1 = int(input("enter a number :- "))
# num2 = int(input("enter a number :- "))

# if num1>num2:
#     print(f"{num1} is greater" )
# else:
#     print(f"{num2} is greater" )

# num = int(input("enter a number to check even or odd :- "))

# if num % 2 == 0 :
#     print("your number is even ")
# else:
#     print("your number is odd ")


# text = input("the your text :- ")

# for i in range(len(text)):
#     print(text[i])

# n = int(input("Enter how many times to print: "))

# for i in range(0,n,1):
#     print("Hello World")


# n = int(input("Enter a number :-  "))

# for i in range(0,n+1,1):
#     print(i)



# n = int(input("Enter a number :-  "))

# for i in range(n+1,0,-1):
#     print(i)


# n = int(input("Enter a number :-  "))

# for i in range(n,n*11,n):
#     print(i)

# Sum of natural numbers up to n terms

# n = int(input("Enter a number: "))

# total = 0
# for i in range(1, n+1):
#     total += i

# print(total)



# n = int(input("Enter a number: "))

# total = 1
# for i in range(1, n+1):
#     total *= i

# print(total)


# n = int(input("Enter a number: "))
# sumeven = 0
# sumodd = 0

# if n % 2 == 0:
#     # Sum of even numbers up to n
#     for i in range(2, n+1, 2):
#         sumeven += i
#     print(sumeven)
# else:
#     # Sum of odd numbers up to n
#     for i in range(1, n+1, 2):
#         sumodd += i
#     print(sumodd)


# num1 = int(input("enter a number to start counting :- "))
# num2 = int(input("enter a number to stop counting :- "))

# for i in range(num1,num2+1,1):
#     print(i)

# num1 = int(input("enter a number to start counting :- "))
# num2 = int(input("enter a number to stop counting :- "))

# for i in range(num1,num2+1,-1):
#     print(i)


# text = input("enter the sraing :- ")

# for i in range(len(text)):
#     print(i)

# num = int(input("Enter a number: "))
# add = 0

# for i in range(1,num-1):
#     if num % i == 0:
#         add += i

# if add == num :
#     print("yes the number is parfact ")
# else:
#     print("No the number is not parfact ")


# n = int(input("enter a number :- "))

# for i in range(2,n-2):
#     if n % i ==0 :
#         print("number is not prime")
#     else:
#         print("number is  prime")
# Program to print each character of a string

# text = input("Enter a string: ")

# for i in range(len(text)): um
#     print(text[i])           

# num = int(input("enter a number  :- "))

# for i in range(1,num):
#     if num % 3 == 0:
#         print(num)

# num = int(input("enter a number :- "))

# while num > 0 :
#     print(num % 10)
#     num =num // 10


# num = int(input("enter the number :- "))
# start = 0

# while start <= num:
#     print(start)
#     start = start +1


# num = int(input("enter a number :- "))

# while num > 0:
#     print(num % 10)
#     num = num // 10

# num = int(input("enter a number :- "))
# rev =0 
# while num > 0:
#     rev = rev *10 + num % 10 
#     num = num//10

# print(rev)


# num = int(input("enter a number :- "))
# save = num
# rev = 0
# while num >0 :
#     rev = rev * 10 + num % 10 
#     num =num  // 10


# if save == rev :
#     print(f"the number {save} is a parfact")
# else:
#     print(f"the number {save} is not parfact")

# import random 

# num = random.randint(1, 10)

# tries = 0
# while True:
#     guess = int(input("Please guess the number: "))
#     tries = tries + 1
#     if num == guess:
#         print(f"You guessed the right number in {tries} tries!")
#         break
#     elif num < guess:
#         print("Move lower than your guess.")
#     elif num > guess:
#         print("Move higher than your guess.")
#     else:
#         print("try again to guess.")



# num = int(input("Enter a number: "))

# add = 0
# while num > 0:
#     digit = num % 10   
#     add = add + digit      
#     num = num // 10        

# print("Sum of digits =", add)


# num = int(input("enter the number :- "))

# while num > 0:
#     digat = num % 10
#     num = num // 10
#     if digat % 2 == 0 :
#         print(f"your number is even {digat}") 
#     else:
#         print(f"your number is odd {digat}") 


# num = int(input("enter A NUMBER :- "))
# while num > 0:
#     digat = num % 10
#     num = num // 10
#     digat = digat * digat * digat 

# print(digat)


# import random

# num = random.randint(1,10)

# tries = 0
# while True:
#     guess = int(input("guess the number :- "))
#     if num == guess :
#         tries = tries + 1
#         print(f"you guessed the numer in {tries} trise ")
#         break
#     elif num < guess :
#         tries = tries + 1
#         print("move lower then number ")
#     elif num > guess :
#         tries = tries + 1
#         print("move higer then number")



# def sum(a,b):
#     print(f"the sum of your number is {a + b} ")


# sum(12,34)
# sum(10,10)
# sum(50,30)
# sum(40,10)\


# def intro(name,age):
#     print(f"my name is {name} and my age is {age}")

# intro(age = 24,name ="sohail")


# def check(string):
#     rev = ""
#     for i in range(len(string)-1, -1, -1):
#         rev = rev + string[i]

#     if rev == string:
#         print(f"{string} is palindromic")
#     else:
#         print(f"{string} is not palindromic")

# check("naman")


# string = "hello sir "
# print(string[0:10:1])


# note = [1,2,3,4,5,6,7,8]

# for i in range(len(note)):
# #     print(note[i])


# l = [1,-3,2,-1,4,5,-6,-86,43]

# print("all positive number of your list is : ")
# for i in range(len(l)):
#     if i >= 0:
#         print(l[i])

# print("all nagitive number of your list is : ")

# for i in range(len(l)):
#     if i <= 0:
#         print(i)




# l = [12,-34,2 ,43,-21,20,-30,-10,23,-239,23,32]


# print("All positive number of ist are : ")

# for i in l:
#     if i >= 0:
#         print(i)


# print("All nagitive number of ist are : ")

# for i in l:
#     if i <= 0:
#         print(i)


# l = [12,54,42,34,23,32]

# add = 0

# for i in l:
#     add = add + i

# print(add/len(l))


# l = [12,54,42,34,23,32]


# lowest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] < lowest :
#         lowest = l[i]
#         index = i

# print(lowest , index)

# numbers = [7, 15, 28, 42, 693, 89, 101, 256, 333, 51]

# largest = numbers[0]
# seclargest = numbers[0]

# for i in numbers:
#     if i > largest:
#         seclargest = largest
#         largest = i
#     elif i > seclargest:
#         seclargest = i

# print(f"Largest number is {largest} and Second largest is {seclargest}")

# num = [2,3,4,5,44]

# for i in range(len(num)-1):
#     if num[i] <= num[i + 1]:
#         continue
#     else:
#         print("your list is not sorted ")
#         break
# else:
#         print("your list is  sorted ")


# nums = [1,2,3,2,4,5,1,6,7,5]
# new = []
# for i in nums:
#     if i not in new :
#         new.append(i)
    
# print(new)

# nums = [12, 7, 9, 20, 33, 42, 55]

# even = []
# odd = []
# for i in nums :
#     if i % 2 == 0:
#         even.append(i)
#     elif i % 2 != 0:
#         odd.append(i)

# print(f"even number are : {even} and odd number are : {odd}") 


# nums = [12, 7, 9, 20, 33, 42, 55]
# revers = []
# for i in range(len(nums)-1,-1,-1):
#     revers.append(nums[i])

# print(revers)


# nums = [1223, 754, 957, 2800, 33453, 424, 89055]
# sum = 0
# for i in nums :
#     sum = i % 10 
# nums = [10, 25, 3, 89, 45, 67]
# largest = nums[0]
# seclargest = nums[0]

# for i in nums:
#     if i > largest:
#         seclargest = largest
#         largest = i
#     elif i > seclargest :
#         seclargest = i

# print(seclargest)



# nums = [10, 25, 3, 89, 45, 67]

# for i in range(len(nums)-1):
#     if nums[i] < nums[i + 1]:
#         continue
#     else:
#         print("your list is noot sorted")
#         break

# else:
#     print("yourlist is sorted" )


# dis  = {1 : 10,  2 : 20 , 3 : 30 , 4 : 40 , 5 : 50}

# sum = 0

# for i in dis:
#     sum = sum + dis[i]

# print(sum)


# data = [1,1,1,2,3,2,2,3,3,4,5,5,5,3,4,5,3]

# dist = {}
# for i in data :
#     if i in dist.keys():
#         dist[i]  += 1
#     else:
#         dist[i] = 1

# print(dist)

# dist1: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# dist2: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# for i in dist2:
#     if i in dist1.keys():
#         dist1[i] += dist2[i]
#     else:
#         dist1[i] = dist2[i]

# print(dist1)

# num  = int(input("enter a number to divide by 10 :- "))

# try:
#     print(10/num)
# except Exception as error:
#     print(f"sorry the is an  error with the name of {error}")

# print("yes your code is runned success fully")


# file = open("testing.py" , 'a')

# file.write("i am the xcibfdjbbhf ljvfbjlfvf ")

# file.close()


