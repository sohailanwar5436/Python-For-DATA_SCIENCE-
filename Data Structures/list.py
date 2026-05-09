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

# methord in list 

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



# #task 1 from python Book 
# num = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45]
# num.sort(key=lambda x: x < 0)
# print("Positive numbers:", num[:5])
# print("Negative numbers:", num[5:])


# task 2 from book 
num = [10, -5, 20, -15, 30, -25, 40, -35, 50, -45]
new = 0
for i in range(0,10):
    new += i
print(new%9)