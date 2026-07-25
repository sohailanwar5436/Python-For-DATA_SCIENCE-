from pathlib import Path
import os

def showfile():
    path = Path('.') 
    items = [f for f in path.iterdir() if f.is_file()]
    for i , item in enumerate(items ,start=1):
        print(f"{i+1}  :   {item.name}")

def createfile():
    try :
        showfile()
        name = input("tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as sf:
             data = input("write something in your file :- ")
             sf.write(data)

            print("FILE IS CREATED SUCCESFULLY ")
        else:
            print("THIS NAME FILE ALREADY EXSIT")

    except Exception as error :
        print(f"THERE IS AN ERROR {eorro}")

def readfile():
    try :
         showfile()
         name = input("tell the name of file you want to read  :- ")
         p = Path(name)
         if p.exists :
             with open(p,"r") as sf:
                 data = sf.read()
                 print(data)

             print("DATA READED SUCCES")
         else:
             print(f"{name} IS NOT EXSIT ")
    except Exception as err:
        print(f"THERE IS AN ERROR {err}")

            

def updatefile():
    try :
        showfile()
        name = input("GIVE THE NAME OF FILE YOU WANT TO UPDATE :- ")
        p = Path(name)

        if p.exists() :
            updata = input("write what you want to update :- ")
            with open(p,"a") as sf :
               sf.write(updata)
 
            print("DATA UPDATED SUCCESFULLY")         
        else :
            print(f"THERE IS NO FILE NAME WITH {name}")

    except Exception as error :
        print(f"THERE IS AN ERROR {error}")


def deletefile():
    try :
        showfile()
        name = input("WHICH FILE YOU WANT TO DELETE :- ")
        p = Path(name)
        if p.exists():
            os.remove(p)
            
            print("FILE IS DELETED SUCCESFULLY ")
        else:
            print("THERE IS NOT ANY FILE WITH THIS NAME ")

    except Exception as error:
        print(f"THERE IS AN ERROR {error}")
    
print("press 1 to create a file")
print("press 2 to read a file")
print("press 3 to update a file")
print("press 4 to delete  a file")

check = int(input("WHAT IS YOUR CHOISE :- "))

if check == 1:
    createfile()

if check == 2 :
    readfile()

if check == 3:
    updatefile()


if check == 4:
    deletefile()