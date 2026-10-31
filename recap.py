# # comments
# name = input("ENTER YOUR NAME ? ")

# print(f"WELLCOME SIR {name}")

# print(126>130)
# print((456 == 456) != (235 == 236))
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# print(True and bool(0))

# num1 = int(input("ENTER YOUR FIRAST NUMBER :- "))
# num2 = int(input("ENTER YOUR SEOUND NUMBER :- "))

# if num1 >= num2:
#     print(F"THE NUMBER {num1} IS GREATER ")
# else:
#     print(F"THE NUMBER {num2} IS GREATER ")



# gender = input("ENTER YOUR GENDER  :- ")

# if gender == "male":
#     print("WELLCOME SIR")
# else:
#     print("WELLCOME MADIUM")

# name = input("ENTER YOUR NAME :- ")
# age = int(input("ENTER YOUR AGE :- "))

# if age >= 18 :
#     print(f"hello {name} you are a valid voter")
# else:
#     print(f"hello {name} you are a not valid voter")

# temp = int(input("TELL ME THE TEMPERATURE :- "))

# if temp <= 0 :
#     print("Freezing Cold")
# elif temp <= 10 :
#     print("VERY Cold")
# elif temp <= 20 :
#     print("Cold")
# elif temp <= 30 :
#     print("pleasent")
# elif temp <= 40 :
#     print("HOt")
# else:
#     print("VERY hot")

# for i in range(1,11,1):
#     print(i)
# a = 0
# while a == 10 :
#     a += 1

# print(a)

# get = int(input("ENTER A NUMBER TO GET HELLO :- "))
# value = ""
# for i in range(get):
#     value += "hello"
# print(value)


# num = int(input("ENTER A NUMBER :- "))

# for i in range(num,num*11,num):
#     print(i)

# num = int(input("ENTER A NUMBER :- "))

# result = 0
# for i in range(1, num+1):
#     result += i

# print(result)


# a = 1
 
# while a <= 100:
#     print(a)
#     a = a + 1


# def pro(d,c):
#     print(f"the proucat of numbers is {d*c}")

# pro(3,3)
# a = "dada"
# result = ""
# for i in range(len(a)-1, -1, -1):
#     result = result + a[i]

# print(result)



# def rev(data):
#     result = ""
#     for i in range(len(data)-1, -1, -1):
#         result = result + data[i]

#     if result == data:
#         print("this string is parandrom")
#     else:
#         print("this string is not parandrom")


# rev("naman")
# rev("sohail")


# a =[1,2,-3,-4,-512,-31,9]
 
# positive_list = []
# negative_list = []
# for i in a:
#     if i > 0:
#         positive_list(i)
#     elif i < 0:
#         negative_list(i)

# print(f"Positive elements: {positive_list}")
# print(f"Negative elements: {negative_list}")

# num = 3

# print(num)
# for i in range(1,3):
#     num = num + 5
#     print(num)


from pathlib import Path
import os


def showfile():
    path = Path('.') 
    items = [f for f in path.iterdir() if f.is_file()]
    for i , item in enumerate(items ,start=1):
        print(f"{i+1}  :   {item.name}")

def creaetfile():
    try :
        showfile()
        name = input("ENTER THE NAME OF FILE YOU WANT TO CREATE :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("WRITE SOMETHNG IN FIEL YOU HAVE CREATED ")
                fs.write(data)
            print("FILE CREATD SUCCESFULL")
        else:
            print(f"{name} THSI FILE NAME IS ALREADY EXSIT TRY AGIAN")
    except Exception as err:
        print(f"THERE IS AN EORROR WITH NAME OF {err}")


def updatefile():
    try:
        showfile()
        name = input("TELL ME THE NAME OF FLIE YOU WANT TO UPDATE ")
        p = Path(name)
        if p.exists():
            with open(p,"a") as fs:
                data = input("WRITE SOMETHNG IN FIEL YOU HAVE CREATED ")
                fs.write(data)
            print("FILE IS UPDATED SUCCESSFULY")
        else:
            print(f"{name} THSI FILE NAME IS not EXSIT TRY AGIAN")

    except Exception as err:
        print(f"THERE IS AN EORROR WITH NAME OF {err}")


def readfile():
    try:
        showfile()
        name = input("TELL ME THE NAME OF FLIE YOU WANT TO READ ")
        p = Path(name)
        if p.exists():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("FILE IS READED SUCCESSFULY")
        else:
            print(f"{name} THSI FILE NAME IS not EXSIT TRY AGIAN")

    except Exception as err:
        print(f"THERE IS AN EORROR WITH NAME OF {err}")


def deletefile():
    try:
        showfile()
        name = input("TELL ME THE NAME OF FLIE YOU WANT TO DELETE  ")
        p = Path(name)
        if p.exists():
            os.remove(p) 
            print("FILE IS DELETED SUCCESSFULY")
        else:
            print(f"{name} THSI FILE NAME IS not EXSIT TRY AGIAN")

    except Exception as err:
        print(f"THERE IS AN EORROR WITH NAME OF {err}")



print("PRESS 1 TO CREATE A FILE ")
print("PRESS 2 TO UPDATE A FILE ")
print("PRESS 3 TO READ A FILE ")
print("PRESS 4 TO DELETE A FILE ")

check = int(input("TELL ME YOUR RESPONSE :- "))

if check == 1:
    creaetfile()

if check == 2:
    updatefile()


if check == 3:
    readfile()
    

if check == 4:
    deletefile()
    