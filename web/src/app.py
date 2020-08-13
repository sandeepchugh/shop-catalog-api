import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_available_apis():
    return "<a href='/api/v1/catalog/products'>Products</a>"


@app.route("/api/v1/catalog/products", methods=['GET'])
def get_all_products():
    """
    Gets all products
    :return:
    """
    return jsonify(hello="world")


@app.route("/api/v1/catalog/products/<product_id>", methods=['GET'])
def get_product_by_id(product_id):
    """
    Gets all products
    :return:
    """
    product = {"name":"test_product"}
    return product


if __name__=="__main__":
    app.run(host="0.0.0.0")