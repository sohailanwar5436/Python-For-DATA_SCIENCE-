# num = int(input("tell a number to sprate it : "))

# while num > 0 :
#     print(num % 10)
#     num //= 10

# give = int(input("give to revers : "))

# resave = 0
# while give > 0:
#     resave = resave * 10 + give % 10
#     give //= 10

# print("Reversed number:", resave)


# num = int(input("give a number : "))
# original = num
# resave = 0

# while num > 0 :
#     resave = resave * 10 + num % 10
#     num //= 10

# if original == resave :
#     print("the number is pallindromic number")
# else:
#     print("the number is not pallindromic number")

# import random

# # Step 1: Generate random number
# num = random.randint(1, 10)
# trise = 0

# # Step 2: Loop until correct guess
# while True:
#     guess = int(input("Guess the number between 1 to 10: "))
#     trise += 1
    
#     if guess == num:
#         print(f"Yes! You guessed the number in {trise} tries.")
#         break
#     else:
#         print(f"Wrong guess! You have used {trise} tries.")


# num = int(input("give a number : "))
# org = num
# for i in range(num,num*10+1,num):
#     print(i)

# total = 0
# while org >0:
#     total += org 
#     print(total) 
#     org -=1

# num = int(input("Give a number: "))
# org = num
# sum_of_factors = 0

# for i in range(1, num):
#     if num % i == 0:
#         print(i)  
#         sum_of_factors += i

# if sum_of_factors == org:
#     print(f"Yes, {org} is a perfect number")
# else:
#     print(f"No, {org} is not a perfect number")