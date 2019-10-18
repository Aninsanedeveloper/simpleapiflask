from flask import Flask , jsonify , render_template , request
from products import products
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products' , methods =['POST'])
def postProducts():
    newItem = {
        "name" : request.json['name'],
        "price": request.json['price'],
        "marca": request.json['marca']
    }
    products.append(newItem)
    return jsonify({"message": "NEW LIST", "products": products})

@app.route('/products/<string:product_name>')
def getProductName(product_name):
     productFound =  [p for p in products if p['name'] == product_name ]
     if (len(productFound) > 0):
         return jsonify({"the product that we found is ": productFound[0]})
     return jsonify({"message": "Ohhh product doesnt exist! "})

@app.route('/products/<string:product_name>', methods=['PUT'])
def fixProduct(product_name):
    item = [ i for i in products if product_name == i['name']]
    if (len(item) > 0):
        item[0]['name'] = request.json['name']
        item[0]['price'] = request.json['price']
        item[0]['marca'] = request.json['marca']
        return jsonify(item)
    return jsonify({"message": "items match not found", "products": products})
     
   

if __name__ == '__main__':
    app.run(debug= True, port= 4000)
