import os
import getpass
import sqlite3
from flask import Flask, request


#VARIABLES
db = sqlite3.connect("cmac.db").cursor()





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
class Item:
    def __init__(self, id, name, price, stock):
        seld.id = id
        self.name = name
        self.price = price
        self.stock = stock
        
        



#SERVER
app = Flask(__name__)

@app.route('/')
def index():
    print (request.__dict__)
    return "This is the home page"

@app.route('/login')
def login():
    return "This is the login page"
    
@app.route('/register')
def register():
    return "This is the register page"
    
@app.route('/search')
def search():
    return "This is the search page"  
    
@app.route('/invoice')
def invoice():
    return "This is the invoice page"
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4000)


    

