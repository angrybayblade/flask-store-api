from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

stores = [
    {
        'name':'store1',
        'items':[
            {
                'name':'chair',
                'price':20,
            }
        ]
    }
]

class Store(Resource):
    def get(self,name):
        for store in stores:
            if store['name'] == name:
                return store
        return {'Massege':'Store Not Found'}

    def post(self,name):
        stores.append({
            "name":name,
            "items":[]
        })
        return stores

    def delete(self,name):
        for i in range(len(stores)):
            if name == stores[i]['name']:
                del(stores[i])
                return stores
        return {"Message":"No Store Found"}    

class Item(Resource):
    def get(self,store,name):
        return {"Store":store,"name":name}
    
    def post(self,store,name):
        for i in range(len(stores)):
            if stores[i]['name'] == store:
                stores[i]['items'].append({"name":name,"price":0})
                return stores[i]
        return {"Message":"No Store Found"}

    def delete(self, store, name):
        for i in range(len(stores)):
            if stores[i]['name'] == store:
                for j in range(len(stores[i]["items"])):
                    if stores[i]["items"][j]['name'] == name:
                        del(stores[i]["items"][j])
                        return stores[i]
                return {"Message":"No item found"}
                
        return {"Message": "No Store Found"}

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:store>/<string:name>')

app.run(port=5000)
