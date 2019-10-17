from flask import Flask , jsonify
from products import products
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProductName(product_name):
     productFound =  [p for p in products if p['name'] == product_name ]
     return jsonify(productFound[0])
   

if __name__ == '__main__':
    app.run(debug= True, port= 4000)
