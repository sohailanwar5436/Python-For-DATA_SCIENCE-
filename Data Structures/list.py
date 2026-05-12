# # indexing and celicing of list
# number =[12,54,56,66,44,32,55,87,76,43]
# print(number[0:4])
# #print the revers of list
# print(number[9:0:-1])



# # methord to loop on list 
# number =[12,54,56,66,44,32,55,87,76,43]

# # First way: using indexing
# for i in range(len(number)):
#     print(number[i])  

# #secounnd way : diractly geting
# for i in number:
#     print(i)

# # methord in list 

# #1. append
# num = [1,2,3,4,5,]
# num.append(6)
# print(num)

# # 2. insert 
# num = [1,2,4,5,]
# num.insert(3,3)
# print(num)


# #  3. extend 
# num = [1,2,4,5]
# num.extend([6,7,8,9,10])
# print(num)

# #  4. remove
# num = [1,2,3,4,5]
# num.remove(4)
# print(num)


# # 5 . pop
# num = [1,2,3,4,5]
# num.pop(3)
# print(num)


# # 6. index
# num = [1,2,3,4,5]
# pos = num.index(3)   
# print(pos)

# # 7. count
# num = [1,2,3,4,5,4,6,4,2,5,3,4]
# cont = num.count(4)
# print(cont)

# # 8. sort
# num = [1,2,3,4,5]
# num.sort()
# print(num)

# # 9. revers
# num = [1,2,3,4,5,4,6,4,2,5,3,4]
# num.reverse()
# print(num)


# # 10 . copy
# num = [1,2,3,4,5,4,6,4,2,5,3,4]
# cpy =num.copy()
# print(cpy)

# # 11. clear 
# num = [1,2,3,4,5,4,6,4,2,5,3,4]
# new = num.clear()
# print(new)



# # task 1 from python book seprate positive and nagitive number from list 
# number = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45]

# for i in number :
#     if i <= 0:
#         print(f"nagitive number are : {i}")

# for i in number :
#     if i > 0 :
#         print(f"positive number are : {i}")

# # task 2 from python book find the mean of list
# num = [1,2,3,4,5,4,6,4,2,5,3,4]
# sum = 0
# for i in num:
#     sum = sum + i

# mean = sum / len(num)
# print("Mean of list elements is", mean)

# # task 3 from python book find the largest 
# num = [23,43,52,54,87,76,75,3,23,46,63]

# store = num[0]
# for i in num :
#     if i > store :
#         store = i
#         ind = num.index(i)   

# print(f"largest number of list is {store} and index {ind}")


# # task from AI  findthe smallest

# num = [23,43,52,54,87,76,75,3,23,46,63]

# smaller = num[0]
# for i in num :
#     if i < smaller :
#         smaller = i
#         ind = num.index(i)   

# print(f"your smallest number is {smaller} and index {ind}")




# # task 4 from python book  find the scound largest number

# num = [23,43,52,54,87,76,75,3,23,46,63]

# largest = num[0]
# seclargest = num [0]

# for i in num :
#     if i >  largest:
#         seclargest = largest
#         largest = i
#         ind = num.index(i)   
#     elif i > seclargest:
#         seclargest = i

# print(f"your largest number is {largest} and secounnd largest {seclargest} index {ind}")





# # task find the smallest and secound smallest number from list

# num  = [43,34,33,78,85,66,67,53,87]

# smallest = num[0]
# sec_smallest = num[0]

# for i in num:
#     if i < smallest:
#         sec_smallest = smallest
#         smallest = i
#     elif i < sec_smallest:
#         sec_smallest = i

# print(f"the smallest number of list is {smallest} and the second smallest is {sec_smallest}")



# # task 5 check is the list sorted or not 
# num = [23,53,52,11,34,32,443]

# for i in range(len(num) - 1):
#     if num[i] > num[i + 1]:
#         print("your list is not sorted")
#         break
# else:
#     print("yes this list is sorted")


# # solveing the question from AI  
# number = [3, -1, 7, -5, 2, -9, 0, 4]

# for i in number :
#     if i <= 0:
#         print(f"nagitive number are : {i}")

# for i in number :
#     if i > 0 :
#         print(f"positive number are : {i}")



# # last task from Ai 
# value  = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45, 10, -5, 20, -15, 30, -25]
# newvalue = []
# for i in value :
#     if i not in newvalue:
#      newvalue.append(i)
# print(f'Now the list is clear {newvalue}')

# #part 2 of this question
# list2 = newvalue
# even = []
# odd = []
# for i in list2:
#     if i % 2 == 0 :
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'Even number of list is : {even}')
# print(f'Odd number of list is  : {odd}')

# # part 2 of same question  sum of even and product of odd 
# Neweven = even
# Newodd = odd
# Sum_of_even = 0
# product_of_odd = 1
# for i in Neweven:
#     Sum_of_even = Sum_of_even + i
# for i  in Newodd:
#     product_of_odd = product_of_odd * i
# print(f"the sum of even number is {Sum_of_even}")
# print(f"the product of odd number is {product_of_odd}")