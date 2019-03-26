from flask import Flask,jsonify,request

app = Flask(__name__)

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

@app.route("/")
def index():
    return "Hello"

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[],
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return ("No Store Found")

@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item(name):
    item = request.get_json()
    for store in stores:
        if name == store['name']:
            store['items'].append(item)
            return jsonify(store)
    return "No Store Found"
    
@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return "No Store Found"
    
app.run(port=8080)
