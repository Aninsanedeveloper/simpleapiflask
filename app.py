from flask import Flask , jsonify
from products import products
app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/products')
def getProducts():
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug= True, port= 4000)
