# # how to deal with error of   division by zero 
# input1 = int(input("tell me a number"))

# try:
#     print(10/input1)

# except Exception  as error:
#     print(f"there is an error {error} ")

# print("i have compelate my task")

# # error of dividing by string 
# input1 = input("tell me a number")

# try :
#      print( 5/ input1)

# except Exception as err:
#     print(f"there is an error is {err}")


# print(6*input1)


# # USE CASE OF ELSE Exception
# input1 = int(input("tell me a number"))

# try :
#      print( 5/ input1)

# except Exception as err:
#     print(f"there is an error is {err}")

# else : 
#     print("nice there is no error found ")

# print(6*input1)



# # USE CASE OF FINALLY Exception
# input1 = int(input("tell me a number"))

# try :
#      print( 5/ input1)

# except Exception as err:
#     print(f"there is an error is {err}")

# else : 
#     print("nice there is no error found ")

# finally :
#     print("I Wil run IS THERE ERROE OR NOT")
# print(6*input1)


# # how to create a error by your self useing raise
# age = int(input("tell yur age :-  "))

# if age < 18:
#     raise ValueError(f"your age is not perfact for CNIC ")
# else:
#     print("yes your age is perfact fro CNIC")

# print("your CNIC is in procees  ")


# # solving question from AI
# input1 = input("Tell a list of integers (space separated): ")

# try:

#     if not input1.strip():
#         raise ValueError("List cannot be empty!")

#     numbers = [int(x) for x in input1.split()]

#     total = sum(numbers)
#     count = len(numbers)

#     print(f"You entered: {numbers}")

# except ValueError as error:
#     print(f"There is an error: {error}")

# except Exception as error:
#     print(f"Unexpected error: {error}")

# else:
#     print("Average of numbers is:", total / count)

# finally:
#     print("Program execution finished.")
