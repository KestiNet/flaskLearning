from flask import Flask, jsonify, make_response

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"

@app.route("/no_content")
def no_content():
    return jsonify({"message": "No content found"}), 204

@app.route("/exp")
def index_explicit():
    resp = make_response(jsonify({"message": "Hello World"}))
    resp.status_code = 200
    return resp
