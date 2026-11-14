import json
import random
import string
from pathlib import Path


class Bank:
    database = Path(__file__).parent / "data.json"
    data = []


    @staticmethod
    def update():
        with open(Bank.database,"w")as fs:
            fs.write(json.dumps(Bank.data))

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print(f"NO FILE EXIST WITH THIS NAME ")
    except Exception as err:
        print(f"THERE IS AN ERROR WITH NAME OF {err}")

    @staticmethod
    def account_No_generator():
        alphabat = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits , k=3)
        spacial = random.choice("!@#$%^&*")
        data = alphabat + num + [spacial]
        random.shuffle(data)
        return"".join(data)
    
    def createaccount(self):
        info ={
            "name" : input("ENTER YOUR NAME :- "),
            "age" : int(input("ENTER YOUR AGE :- ")),
            "email" : input("ENTER YOUR EMAIL :- "),
            "pin" : int(input("ENTER YOUR PIN :- ")),
            "account" : Bank.account_No_generator(),
            "balance" : 0,
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4 :
            print("YOU CAN'T CREATE ACCOUNT ")
        else:
            print("YOUR ACCOUNT IS CREATED SUCCESFULLY ")
            for i in info :
                print(f" {i}   :  {info[i]}")
            print("NOTE DOWN YOUR ACCOUNT NUMBER ")

            Bank.data.append(info)
            Bank.update()



    def depositmoney(self):
        accnumber = input("ENTER YOUR ACCOUNT NUMBER :- ")
        password = int(input("ENTER YOUR ACCOUNT PIN :- "))
        userdata = [i for i in Bank.data if i['account'] == accnumber and i['pin'] == password]
        if not userdata :
            print("NO ACCOUNT FOUND WITH THIS DEATILS ")
        else:
            ammount = int(input("ENTER YOUR AMMOUNT YOU HAVE TO DEPOSIT :- "))
            if ammount > 10000 or ammount <0:
                print("YOU CAN ONLY DEPOSITE AMOUNT IN RANGE OF 0 TO 10000")
            else:
                userdata[0]['balance'] += ammount
                Bank.update()
                print("YOU AMMOUNT IS DEPOSITED SUCESFULLY")
    

    def withdrowmoney(self):
        accnumber = input("ENTER YOUR ACCOUNT NUMBER :- ")
        password = int(input("ENTER YOUR ACCOUNT PIN :- "))
        userdata = [i for i in Bank.data if i['account'] == accnumber and i['pin'] == password]
        if not userdata:
            print("NO ACCOUNT FOUND WITH THIS DEATILS ")
        else:
            ammount = int(input("ENTER YOUR AMMOUNT YOU HAVE TO withdrow :- "))
            if userdata[0]['balance'] < ammount:
                print("YOU HAVE NO BALANCE")
            else:
                userdata[0]['balance'] -= ammount
                Bank.update()
                print("YOU AMMOUNT IS withdrow SUCESFULLY")


    def showdeatils(self):
        accnumber = input("ENTER YOUR ACCOUNT NUMBER :- ")
        password = int(input("ENTER YOUR ACCOUNT PIN :- "))
        userdata = [i for i in Bank.data if i['account'] == accnumber and i['pin'] == password]
        if not userdata:
            print("NO ACCOUNT FOUND WITH THIS DEATILS ")
        else:
            print(f"YOR DEATIALS ARE ")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")



    def updatedeatils(self):
        accnumber = input("ENTER YOUR ACCOUNT NUMBER :- ")
        password = int(input("ENTER YOUR ACCOUNT PIN :- "))
        userdata = [i for i in Bank.data if i['account'] == accnumber and i['pin'] == password]
        if not userdata:
            print("NO ACCOUNT FOUND WITH THIS DEATILS ")
        else:
            print("YOU CAN ONLY CHANGE NAME , EMAIL AND PIN")
            newdata = {
                "name" : input("ENTER YOUR  NEW NAME OR PRESS ENTER TO SKIP :- "),
                "email" : input("ENTER YOUR  NEW EMAIL OR PRESS ENTER TO SKIP :- "),
                "pin" : input("ENTER YOUR  NEW PIN OR PRESS ENTER TO SKIP :- "),
            }
            if newdata['name'] == "":
                newdata['name'] = userdata[0]['name']

            if newdata['email'] == "":
                newdata['email'] = userdata[0]['email']

            if newdata['pin'] == "":
                newdata['pin'] = userdata[0]['pin']

            newdata['age'] = userdata[0]["age"]
            newdata['account'] = userdata[0]["account"]
            newdata['balance'] = userdata[0]["balance"]

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
                
            Bank.update()
            print("YOUR DEATIALS IS UPDATED SUCCESFULLY")


    def deleteaccount(self):
        accnumber = input("ENTER YOUR ACCOUNT NUMBER :- ")
        password = int(input("ENTER YOUR ACCOUNT PIN :- "))
        userdata = [i for i in Bank.data if i['account'] == accnumber and i['pin'] == password]
        if not userdata:
            print("NO ACCOUNT FOUND WITH THIS DEATILS ")
        else:
            check = input("PRESS 1 TO DELETE ACCOUNT OR PRESS 2 TO LEAVE ACCOUNT :- ")

            if check == "n" or check == "N":
                pass
                print("YOUR ACCOUNT IS EXISTS NOT DELETED")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("YUOR ACCOUNT IS DELETED SUCCESFULLY")
                Bank.update()        
user = Bank()
print("PRESS 1 TO  CREATE A ACCOUNT ")
print("PRESS 2 TO  DEPOSIT IN ACCOUNT ")
print("PRESS 3 TO  WITHDROW MANEY FROM ACCOUNT ")
print("PRESS 4 TO  SEE DEATIAL OF ACCOUNT ")
print("PRESS 5 TO  UPDATE  ACCOUNT DEATIALS ")
print("PRESS 6 TO  DELETE  ACCOUNT ")

response = int(input("TELL ME YOUR RESPONSE :- "))

if response == 1:
    user.createaccount() 


if response == 2:
    user.depositmoney() 

if response == 3:
    user.withdrowmoney()


if response == 4:
    user.showdeatils()


if response == 5:
    user.updatedeatils()


if response == 6:
    user.deleteaccount()
    