## Introduction To RESTful APIs and Test First Method

[Postman Collection For App](https://www.getpostman.com/collections/6ee02736c01b5bde4fec)

### Creating A Resource
```python
from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Store(Resource):
    def get(self,*args):
        """
        GET Request Handler
        """
        return response
```

### Adding Resource Endpoint

```python
api.add_resource(Store,"/store/")
app.run(port=5000)
```

### Test First Method
- Create test cases for every end point before implementation.
- Use Postman to test end points.
- Save the test cases for more tests.

#### Here we re going to implement following endpoints

- **/store/\<string:name>** 
  - **GET** will return store as JSON.
  - **POST** will create a store.
  - **DELETE** will delete the store if exists.
- **/item/\<string:store>/\<string:name>**
  - **GET** will return perticular item.
  - **POST** will create a new item
  - **DELETE** will delete the item if exist.