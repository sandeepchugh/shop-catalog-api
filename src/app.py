from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Product(Resource):
    def get(self):
        return {'Hello':'World'}


api.add_resource(Product,"/")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')