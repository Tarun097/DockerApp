from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        responseBody = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret"
            }
        ]
        return responseBody, 200, {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials" : "true" }


api.add_resource(Users, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)