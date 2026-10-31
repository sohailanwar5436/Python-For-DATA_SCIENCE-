# class First:
#     vir = 12 #this is a atribute

#     def hi(self): #METHORD
#         print("HELLO WORLD")

#     print("I AM RUNED")

# print(First().vir)

# First().hi()




# class First:
#     vir = 12 #this is a atribute

#     def hi(self): #METHORD
#         print("HELLO WORLD")

#     print("I AM RUNED")

# obj = First()

# print(obj.vir)
# obj.hi()



# class car:
#     def __init__ (self, body, color ,sest):
#         self.body = body
#         self.color = color
#         self.sest = sest
    
#     def see(self):
#             print(f"your car body is :{self.body}, and color is : {self.color}, and setes requrid is {self.sest} ")

# lambo = car("metal","green",2)
# toyota = car("iron","white",4)




# class data:
#     name = 'i am sohail'

#     def age(self):
#         print("my age  is 21")


# class show(data):
#     pass

# see = data()
# see2 = show()

# print(see.name)   # prints: i am sohail
# see2.age()  


# class animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"your name is {self.name}")

# class human(animal):
#     pass

# animal = human("loin")
# person = human("ali")

# person.show()
# animal.show()

# class car1:
#     d = "I AM A BOX OF CAR 1"

#     def car(self):
#         print("I am function of class 1")

    
# class car2(car1):
#     pass

# obj = car1()
# obj2 = car2()

# print(obj2.d)
# obj2.car()


# class family:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f"hello I am your {self.name}")

# class grand(family):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
        
#     def show(self):
#         print(f"hello I am your {self.name} , {self.age}")

# obj1 = family("father")
# obj2 = grand("mather",45)
# obj1.show()
# obj2.show()

# class shop1:
#     def __init__(self, material):
#         self.material = material


# class shop2(shop1):   # shop2 inherits shop1
#     def __init__(self, material, product):
#         super().__init__(material)   # sirf parent ka argument pass karo
#         self.product = product


# class shop3(shop2):   # shop3 inherits shop2
#     def __init__(self, material, product, employ):
#         super().__init__(material, product)   # dono parent arguments pass karo
#         self.employ = employ

#     def show(self):
#         print(f"SHOP MATERIAL {self.material}, PRODUCT REQUIRED {self.product}, and GIVEN EMPLOY {self.employ}")


# obj1 = shop3("leather", 5, 9)
# obj2 = shop3("IRON", 32, 756)
# obj1.show()
# obj2.show()



# class parent:
#     def __init__(slef,name):
#         slef.name = name


# class child(parent) :
#     pass
#     def display(slef,name):
#         print(f"my father name is {slefname}")

# obj = child("anwar")

# obj.display()


# class student:
#     def __init__(self,book,pin,color):
#         self.book = book
#         self.pin = pin
#         self.color = color

#     def show(self):
#         print(f"NAME = {self.book} , PIN = {self.pin} , AND PIN COLOR IS {self.color}")


# ali = student("history",3,"black")
# sohail = student("math",6,"white")

# ali.show()
# sohail.show()

# class animal:
#     def __init__(self,name):
#         self.name = name 

#     def show(self):
#         print(f"HELLO YOUR NAME IS {self.name}")


# class human(animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
        
#     def show(self):
#         print(f"HELLO YOUR NAME IS {self.name}, {self.age}")


# person1 = human("ali",19)
# person2 = animal("lion")
# person1.show()
# person2.show()


# MULTIPUL LEVEL INHRITANCE 

# class factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

#     def show(self):
#         print(f"MATERIAL = {self.material} and ZIPS =  {self.zips}")

# class islfactory(factory):
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips)
#         self.color = color

#     def show(self):
#         print(f"MATERIAL = {self.material} and ZIPS =  {self.zips} AND COLOR = {self.color}")


# class kpkfactory(islfactory):
#     def __init__(self,material,zips,color,poket):
#         super().__init__(material,zips,color)
#         self.poket = poket

#     def show(self):
#         print(f"MATERIAL = {self.material} and ZIPS =  {self.zips} AND COLOR = {self.color} AND POKET = {self.poket}")

# bag = kpkfactory("lather",4,"black",8)

# bag.show()

        
# from abc import ABC,abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def zips(self):
#         pass

# class factory(abstract):
#     def __init__(self,material):
#         self.material = material

#     def show(self):
#         print(f"MATIRAL = {self.material}")

# obj = factory("lather")

# obj.show()