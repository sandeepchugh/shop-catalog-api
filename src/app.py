import json

from flask import Flask, jsonify
from src.config import ConfigurationSettings
from src.product_handler import ProductHandler

app = Flask(__name__)

config = ConfigurationSettings()
product_handler = ProductHandler(config)


@app.route("/api/v1/products/categories/<category_name>", methods=['GET'])
def get_all_products(category_name):
    """
    Gets all products
    :return:
    """
    products = product_handler.get_products_by_category(category_name)
    # TODO: add exception handling
    return jsonify(products)


@app.route("/api/v1/products/<product_id>", methods=['GET'])
def get_product_by_id(product_id):
    """
    Gets all products
    :return:
    """
    product = product_handler.get_product_by_id(product_id)
    # TODO: add exception handling
    return product

