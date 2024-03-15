from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

list_of_messages = []


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/messages', methods=['GET'])
def messages():
    response = jsonify(list_of_messages)
    return response


@app.route('/messages', methods=['POST'])
def save_messages():
    request_data = request.get_json()
    request_text = request_data['text']
    list_of_messages.append(request_text)
    return ''


app.run(debug=True)
