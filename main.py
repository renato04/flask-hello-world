from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
  return 'Hello World'

def results():
  #req = request.get_json(force=True)

  #action = req.get('queryResult').get('action')

  return {'fulfillmentText': 'This is a response from webhook.'}

class WebHook(Resource):
  def get(self):
    return results()
     

api.add_resource(WebHook, '/webhook')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
