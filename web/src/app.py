from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "shop-catalog-api"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/", methods=['GET'])
def get_available_apis():
    return "<a href='/swagger'>Swagger</a>"


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
    product = {"name": "test_product"}
    return product


if __name__ == "__main__":
    app.run(host="0.0.0.0")
