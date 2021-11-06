from flask import Flask, request, redirect, render_template
from pymongo import MongoClient
import search

app = Flask(__name__,  template_folder='templates') #reference this file

cluster = "mongodb+srv://kennywang01:Go2java2@cluster0.ztnht.mongodb.net/cruddb?retryWrites=true&w=majority"

client = MongoClient(cluster)

db = client.cruddb

crudcollect = db.crudcollect


@app.route('/', methods=['POST', 'GET']) # maps url to the following function
def index():
    if request.method == 'POST':
        item_content = request.form['content']

        avg_price = 0
        avg_rating = 0
        item = {"name": item_content, "avg-price": avg_price, "avg-rating": avg_rating}

        try:
            crudcollect.insert_one(item)
            return redirect('/')
        except: 
            return "Error: Failed to insert into DB"

    else:
        allItems = list(crudcollect.find())
        print(allItems)
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)