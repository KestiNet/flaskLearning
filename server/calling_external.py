from flask import Flask, escape
import request

app = Flask(__name__)

@app.route("/")
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.JSON?q=Michael Chrichton")
    if res.status_code == 200:
        return {"message" : res.JSON()}
    elif res.status_code ==404:
        return {"message" : "Something went wrong!"}, 404
    else:
        return {"message" : "Server error!"}, 500
