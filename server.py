import os
import getpass
import sqlite3
from flask import Flask, request, jsonify


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

@app.route('/', methods=['GET','POST'])
def index():
    print (request.form)  
    return "This is the home page"

@app.route('/login', methods=['GET','POST'])
def login():
    #URL
    #http://127.0.0.1:4000/?login=username&password=password
    #FOR GET REQUESTS
    print (''.join(dict(request.args)['r']))  
    #FOR POST REQUESTS
    print (''.join(dict(request.form)['r']))    
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
    app.run(host='127.0.0.1', port=4000)


    

