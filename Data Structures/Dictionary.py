# # Dictionary is a commbination of key and value key is use befor : and value become after 
# dis = {1:"sohail"}
# print(type(dis)) 
# # key are in oder and canot same but value can same 


# # geting value from dictionary
# data = {1 : 10 , 2 : 20 , 3 :30 }
# # i can print by key 
# print(data[2])


# # task 1 from python book
# dis1 = {1:20, 2:40 ,3:60}
# dis2 = {4:80, 5:100, 6:120}

# dis1.update(dis2)
# print(dis1)


# #task 2 from python book 
# dis = {1:2 , 2 : 3, 3: 4}
# sum = 0
# for i in dis:
#     sum = sum + dis[i]

# print(sum)

# # find the frequncy of elementin list use dictionary
# data = [1,1,1,2,2,2,2,3,3,3,3,3]
# dis = {}
# for i in data:
#     if i in dis.keys():
#         dis[i] += 1
#     else:
#         dis[i] = 1

# print(dis)



# #combine 2 dictionary but same add them 

# dis1 = {1:20, 2:40 ,3:60}
# dis2 = {4:80, 5:100, 6:120}

# for i in dis2:
#     if i in dis1:
#         dis1[i] += dis2[i]
#     else:
#         dis1[i] = dis2[i]

# print(f"dictionary 1 is equal : {dis1}")
