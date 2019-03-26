## Flask-REST API

### Files

    |_flask-restful
    |__app.py
    |_app.py
    |_README.mf

### Basic Flask App
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

app.run(port=5000)
```

#### This is a example of a basic flask app that will return hello wordl as http response on index.

### A Simple Store API using Flask
 **Flask import and creating an app**
```python
from flask import Flask,jsonify,request
app = Flask(__name__)
```
**Creating a resourse for store requests**
```python
stores = [
    {
        'name':'FirstStore',
        'items':[
            {
                'name':'Chair',
                'price':'300',
            }
        ]
    }
]
```
**Defualt index method that will return a simple hello**
```python
@app.route("/")
def index():
    return "Hello"
```
**Creating A New Store Using POST Method**
```python
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[],
    }
    stores.append(new_store)
    return jsonify(new_store)
```
To create a store make a simple POST request on /store. This will create a new store dictionary , append it into resource array and return it as a JSON string.

Here **jsonify** method will convert dict into a plain JSON string.

**Getting Store Info Using GET method and url path parsing**
```python
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return ("No Store Found")
```

While creating method for handling GET request take URL variable as argument like here it is **name**. This method will return store information as JSON string.

**Getting Whole Store Resource as JSON**
```python
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})
```
**Creating an item using POST request**
```python
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item(name):
    item = request.get_json()
    for store in stores:
        if name == store['name']:
            store['items'].append(item)
            return jsonify(store)
    return "No Store Found"
```
**Request an item from an store**
```python
@app.route('/store/<string:name>/item')
def get_item(name):
    return "Hello"

app.run(port=8080)

```
