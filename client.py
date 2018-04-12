import os
import getpass
import time
import requests

########
#CLASSES
########
 
class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.quantity = quantity
      
    def editItemName(self, itemName):
        self.name = itemName

    def editItemQuantity(self, quantity):
        self.quantity = quantity
      
class Invoice:
    def __init__(self, staffId, InventoryRecordId, Quantity, Items, date):
        self.id = staffId
        self.item = InventoryRecordId #What's the purpose of InventoryRecordId? Is it the invoice number?
        self.Quantity = []
        self.Items = []
        self.InvoiceDate = date
        
class Account:
    def __init__(self, id, employeeId, login, pwd, slt, isAdm):
        self.id = id #is there a difference between id & employeeId?
        self.employeeId = employeeId
        self.login = login #if this refers to the act of a user logging in to their account, shouldn't this be a function & not an attribute?
        self.pwd = pwd
        self.slt = slt #what does this represent?
        self.isAdm = isAdm    
        
class Employee:
    def __init__(self, id, fname, mname, lname, dob, email, phone, date):
        self.id = id
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.dob = dob
        self.email = email
        self.phone = phone
        self.login = login
        self.pwd = pwd
        self.slt = slt
        self.isAdm = isAdm
        self.date = date

class Notification:
    def __init__(self, id, title, message):
        self.id = id
        self.title = title
        self.message = message
        
#INVENTORY CLASS NOT INCLUDED, THE INVENTORY WOULD BE AN SQLLITE FILE RATHER THAN A PYTHON OBJECT
#THE SQLLITE FIEL WOULD STORE ALL ACCOUNTS, NOTIFICATIONS, 




#FUNCTIONS

'''
database = [
    [   
        {"id":"", 
        "fname":"", "mname":"", "lname":"", "dob":"", "eml":"", "fname":"", "fname":"", "fname":"", "fname":"", "fname":""}
    
    ],
    
    [
        
    
    ],
    
    [
        
    
    ]
]
'''

isAdmin = False

def login(id, password):
    r = requests.post(url+"login", data={'id': id, 'password': password})
    if(r.text == "1"):
        if id == "admin":
            isAdmin = True
        return 1
    return 0

def logout():
    global running
    isAdmin = False
    running = False
    os.system('reset || cls')
    

def search(query, sorting, sortBy):
    r = requests.get(url+"search?query="+query)
    if sorting == 123:
        print("")
    else:
        print("")
    results = []
    return results


def mainMenu():
    print("Select an option shown below: ")
    print(" 1] Search Item")
    print(" 2] Add Item")
    print(" 3] Add Account")  
    print(" 4] Remove Item") 
    print(" 5] Remove Account") 
    print(" 6] View Orders") 
    print(" 7] Log Off\n") 

def adminMenu():
    print("Select an option shown below: ")
    print(" 1] Search Item")
    print(" 2] Place Order")
    print(" 3] View Notifications")  
    print(" 4] Log Off\n") 

def title():
    print("=========================")
    print("CARIMAC INVENTORY EXPRESS")
    print("=========================\n")


url = ""
def connect(ip, port):
    try:
        body = requests.get('http://'+ip+":"+port+"/").text
        global url
        url = "http://"+ip+":"+port+"/"
        return 1
    except:
        return 0
    



 
#VARIABLES

order = []
choice = 0

if __name__ == "__main__":
    while True:
        #PROGRAM LOOP START
        title()
        ip , port = "" , ""
        while connect(ip, port) == False:
            ip = input("Enter Host Ip: ")
            port = input("Enter Host Port: ")
            print("\nConnecting...")
            if connect(ip, port) == False:
                print("\nCould not connect to host machine. Please ensure that the server is running and try again.\n")
        print("\nCONNECTION ESTABLISHED\n")
        username =  input("Enter Username: ")
        password = getpass.getpass("Enter Password: ")
        if login(username, password):
            #LOGIN SUCCESSFUL
            running = True
            while(running):
                os.system('reset || cls')
                print("Logged in as: "+username+"\n")
                if(isAdmin):
                    adminMenu()
                    while(True):
                        try:                
                            choice = int(input("Choice: "))
                            if choice < 1 or choice > 4:
                                raise Exception()
                            break
                        except:
                            print("\nInvalid Selection\n")
                            
                        if(choice == 7):
                            logout()
                        
                        if(choice == 1):
                            query = input("Enter the search query :")
                else:
                    mainMenu()
                    while True:
                        try:                
                            choice = int(input("Choice: "))
                            if choice < 1 or choice > 4:
                                raise Exception()
                            break
                        except:
                            print("\nInvalid Selection\n")
                            mainMenu()
                    if choice == 4:
                        #LOG OUT
                        logout()       
                        break      
                    if choice == 1:
                        query = raw_input("Enter Search Query: ")
                        print (search)
                    if choice == 2:
                        #COMPLETE OPTION 2
                        print()
                    if choice == 3:
                        #COMPLETE OPTION 2
                        print()
        else:
            print("Failed to login\n")
