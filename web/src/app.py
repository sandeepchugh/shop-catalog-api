import json

from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object("src.config.Config")


@app.route("/", methods=['GET'])
def get_all_products():
    """
    Gets all products
    :return:
    """
    return jsonify(hello="world")

#
# @app.route("/web/v1/products/<product_id>", methods=['GET'])
# def get_product_by_id(product_id):
#     """
#     Gets all products
#     :return:
#     """
#     product = product_handler.get_product_by_id(product_id)
#     # TODO: add exception handling
#     return product

