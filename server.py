import os
import getpass
#import sqlite3
import requests
from flask import Flask, request, jsonify


#VARIABLES
#db = sqlite3.connect("cmac.db").cursor()





#FUNCTIONS
def login(username, password):
    return 1

def search(string, sorting, sortBy):
    if sorting == 123:
        print("")
    else:
        print("")
    results = []
    return results




#CLASSES
        
class Database:
    def __init__(self):
        self.tables = {"employees":[], "invoices":[], "items":[]}
          
    def addItem(self, item):
        self.tables["items"].append(item)
        
    def removeItem(self, itemIndex):
        self.tables["items"][itemIndex] = ""
        
    def searchForItem(self, item):
        results = []
        for i in self.tables["items"]:
            if item in i:
                results.append(i)
        return results
    
class Item:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
    
    def editItemName(self, name):
        self.name = name
        
    def editItemQuantity(self, quantity):
        self.quantity = quantity

'''
class UserAccount:
    def __init__(self):
'''


#SERVER
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return "This is the home page"

@app.route('/login', methods=['GET','POST'])
def login():
    #URL
    #http://127.0.0.1:4000/?login=username&password=password
    #FOR GET REQUESTS
    print (dict(request.args))
    #FOR POST REQUESTS
    print (dict(request.form))     
    return "This is the login page"
    
    
@app.route('/register', methods=['GET','POST'])
def register():
    return "This is the register page"
    
    
@app.route('/search', methods=['GET','POST'])
def search():
    return "This is the search page"  
    

@app.route('/invoice', methods=['GET','POST'])
def invoice():
    return "This is the invoice page"
    

if __name__ == "__main__":
    db = Database()
    #db.showdb()
    #print(db.db)
    #app.run(host='127.0.0.1', port=4000)


    

