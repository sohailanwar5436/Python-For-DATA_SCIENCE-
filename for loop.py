# create a increaing counter
num1 = int(input("enter a number to start to counting :-"))
num2 = int(input("enter a number to stop to counting :-"))
for i in range(num1,num2+1,1):
    print(i)

# create a decreaing counter
num1 = int(input("enter a number to start to counting :-"))
num2 = int(input("enter a number to stop to counting :-"))
for i in range(num1,num2,-1):
    print(i)


# create a table gernater
num1 = int(input("enter a number for creating table :-"))
for i in range(num1,num1*10+1,num1):
    print(i)


#create a loop for geting straing element
data = "my name is sli and my age is 16. i am student of class 10"
print(len(data))
for i in range(len(data)):
    print(data[i])


# break in Look
for i in range(1,11,1):
     if i < 4:
        continue
     print(i)
    
# test 1 from python Book

num = int(input("enter number for print hello :- "))

for i in range(1, num+1):
    print("hello" * i)

#task 2 from python book 
  
num = int(input("give a number to get counting : "))

for i in range(1,num+1):
    print(i)


# task 3 from python book 

num = int(input("give a number : "))

for i in range(num,1-1,-1):
    print(i)

# task 4 from python book 

num = int(input("give a number to print the table  : "))

for i in range(num,num*10+1,num):
    print(i)

#task 4 print sum of odd number

num = int(input("give a number : "))

get = 0
for i in range(1,num+1):
    get += i
    print(f"your sum is equal to {get}")


#sum of even and odd
num = int(input("give a number : "))
even = 0
odd =0
for i in range(1,num+1):
    if i%2 == 0:
        even += i
    else:
        odd += i

print(f"Final even sum = {even}")
print(f"Final odd sum = {odd}")


# ai question solution
num = int(input("give a number : "))
on2 = 0
on3 = 0
for i in range(1, num+1):
    if i%2 == 0:
        on2 += i
    elif i %3 == 0:
        on3 += i
print(f"{num} is equal to divide in {on2}")
print(f"{num} is equal to divide in {on3}")


# task 5 from python book 
num = int(input("Give a number: "))

print(f"Factors of {num} are:")
for i in range(1, num+1):
    if num % i == 0:   
        print(i)       
